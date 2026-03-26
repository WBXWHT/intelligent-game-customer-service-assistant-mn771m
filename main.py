import json
import time
import random
from datetime import datetime
from typing import Dict, List, Optional

class IntelligentGameCustomerService:
    """智能游戏客服助手核心类"""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        """初始化客服助手
        
        Args:
            model_name: 使用的大模型名称
        """
        self.model_name = model_name
        self.conversation_history = []  # 存储对话历史
        self.common_questions = {  # 常见问题知识库
            "登录问题": ["无法登录", "账号密码错误", "忘记密码"],
            "游戏问题": ["卡顿", "闪退", "无法连接服务器"],
            "充值问题": ["充值未到账", "退款申请", "支付失败"],
            "账号问题": ["账号被封", "修改密码", "绑定手机"]
        }
        
    def simulate_llm_call(self, user_input: str) -> str:
        """模拟大模型API调用（实际项目中替换为真实API）
        
        Args:
            user_input: 用户输入的问题
            
        Returns:
            str: AI生成的回复
        """
        # 模拟API调用延迟
        time.sleep(0.5)
        
        # 基于常见问题知识库生成回复
        for category, questions in self.common_questions.items():
            for question in questions:
                if question in user_input:
                    return f"检测到{category}：{question}。建议您尝试重启游戏或联系客服专员处理。"
        
        # 如果不在知识库中，生成通用回复
        responses = [
            "感谢您的咨询。我已理解您的问题，正在为您查找最佳解决方案。",
            "这个问题我需要进一步确认，请您提供更多详细信息。",
            "建议您查看游戏内的帮助中心，或联系在线客服获取专属支持。",
            "我已记录您的问题，我们的客服团队会尽快与您联系。"
        ]
        return random.choice(responses)
    
    def optimize_prompt(self, user_input: str) -> str:
        """优化多轮对话的Prompt
        
        Args:
            user_input: 原始用户输入
            
        Returns:
            str: 优化后的Prompt
        """
        # 添加上下文信息
        context = "你是一个专业的游戏客服助手，请用友好、专业的语气回答玩家问题。"
        
        # 添加对话历史
        if self.conversation_history:
            history_text = "\n".join([f"用户：{h['user']}\n助手：{h['assistant']}" 
                                    for h in self.conversation_history[-3:]])  # 最近3轮对话
            context += f"\n\n之前的对话：\n{history_text}"
        
        # 添加当前问题
        optimized_prompt = f"{context}\n\n当前问题：{user_input}\n请回答："
        return optimized_prompt
    
    def process_query(self, user_input: str) -> Dict:
        """处理用户查询
        
        Args:
            user_input: 用户输入的问题
            
        Returns:
            Dict: 包含回复和统计信息的字典
        """
        start_time = time.time()
        
        # 优化Prompt
        optimized_prompt = self.optimize_prompt(user_input)
        
        # 模拟调用大模型
        ai_response = self.simulate_llm_call(optimized_prompt)
        
        # 计算响应时间
        response_time = time.time() - start_time
        
        # 记录对话历史
        self.conversation_history.append({
            "user": user_input,
            "assistant": ai_response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # 生成统计信息
        stats = {
            "response_time": round(response_time, 2),
            "conversation_round": len(self.conversation_history),
            "model_used": self.model_name,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return {
            "response": ai_response,
            "stats": stats,
            "optimized_prompt": optimized_prompt
        }
    
    def get_performance_report(self) -> Dict:
        """生成性能报告
        
        Returns:
            Dict: 性能统计数据
        """
        if not self.conversation_history:
            return {"total_queries": 0, "avg_response_time": 0}
        
        total_time = sum([1.5] * len(self.conversation_history))  # 模拟计算总时间
        avg_time = total_time / len(self.conversation_history)
        
        return {
            "total_queries": len(self.conversation_history),
            "avg_response_time": round(avg_time, 2),
            "coverage_rate": "60%",  # 模拟覆盖60%的客服咨询
            "satisfaction_improvement": "25%"  # 模拟满意度提升25%
        }

def main():
    """主函数 - 智能游戏客服助手演示"""
    print("=" * 50)
    print("智能游戏客服助手 v1.0")
    print("=" * 50)
    
    # 初始化客服助手
    assistant = IntelligentGameCustomerService(model_name="gpt-3.5-turbo")
    
    # 模拟用户咨询场景
    test_queries = [
        "游戏登录不上去怎么办？",
        "充值后钻石没到账",
        "游戏总是卡顿",
        "账号被封了怎么解封？",
        "如何修改密码？"
    ]
    
    print("\n开始处理用户咨询...\n")
    
    # 处理每个测试查询
    for i, query in enumerate(test_queries, 1):
        print(f"【用户咨询 {i}】")
        print(f"用户：{query}")
        
        # 处理查询
        result = assistant.process_query(query)
        
        # 显示结果
        print(f"助手：{result['response']}")
        print(f"响应时间：{result['stats']['response_time']}秒")
        print(f"对话轮次：{result['stats']['conversation_round']}")
        print("-" * 40)
    
    # 显示性能报告
    print("\n📊 性能报告：")
    report = assistant.get_performance_report()
    for key, value in report.items():
        print(f"{key}: {value}")
    
    print("\n✅ 演示完成！")
    print("注：实际项目中需接入真实大模型API")

if __name__ == "__main__":
    main()