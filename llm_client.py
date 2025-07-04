#!/usr/bin/env python3
"""
BMAD LLM 客户端 - 支持双模式

支持两种模式：
1. 内置 LLM 模式：使用 Cursor 内置 LLM（通过 MCP 协议）
2. 外部 API 模式：使用 DeepSeek API

可通过环境变量 USE_BUILTIN_LLM 控制模式切换
"""

import json
import logging
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 配置选项：是否使用内置 LLM（默认使用内置 LLM）
USE_BUILTIN_LLM = os.getenv("USE_BUILTIN_LLM", "true").lower() == "true"

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logger.warning("OpenAI SDK not available. Please install with: pip install openai")

@dataclass
class LLMResponse:
    """LLM 响应"""
    content: str
    usage: Dict[str, int]
    model: str
    finish_reason: str

class BMADLLMClient:
    """BMAD 专用 LLM 客户端 - 支持内置 LLM 和外部 API 双模式"""

    def __init__(self, api_key: str = None):
        """
        初始化 LLM 客户端

        Args:
            api_key: DeepSeek API Key（内置 LLM 模式下可选）
        """
        self.api_key = api_key
        self.use_builtin_llm = USE_BUILTIN_LLM

        if self.use_builtin_llm:
            logger.info("🔧 使用 Cursor 内置 LLM 模式")
            self.client = None
        else:
            if not api_key:
                raise ValueError("外部 API 模式需要提供 API Key")
            if OPENAI_AVAILABLE:
                self.client = OpenAI(
                    api_key=api_key,
                    base_url="https://api.deepseek.com"
                )
                logger.info("🌐 使用 DeepSeek API 模式")
            else:
                self.client = None
                logger.error("OpenAI SDK not available")

    def call_agent(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        task: str,
        context: Optional[Dict[str, Any]] = None,
        model: str = "deepseek-chat"
    ) -> Dict[str, Any]:
        """调用智能体执行任务"""

        if self.use_builtin_llm:
            # 内置 LLM 模式：返回角色提示让 Cursor LLM 处理
            return self._call_agent_builtin_llm(agent_id, agent_config, task, context)
        else:
            # 外部 API 模式：调用 DeepSeek API
            return self._call_agent_external_api(agent_id, agent_config, task, context, model)

    def _call_agent_builtin_llm(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """内置 LLM 模式：返回角色提示让 Cursor LLM 处理"""

        # 构建详细的角色提示
        role_prompt = self._build_builtin_llm_prompt(agent_id, agent_config, task, context)

        return {
            "success": True,
            "agent_id": agent_id,
            "task": task,
            "mode": "builtin_llm",
            "role_prompt": role_prompt,
            "response": f"""🤖 **{agent_config.get('title', agent_id)} {agent_config.get('icon', '🤖')}** 已激活

{role_prompt}

---

**请按照以上角色定义和要求来回答用户的问题。**""",
            "usage": {"total_tokens": 0, "prompt_tokens": 0, "completion_tokens": 0},
            "model": "cursor-builtin-llm",
            "finish_reason": "role_activated"
        }

    def _call_agent_external_api(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        task: str,
        context: Optional[Dict[str, Any]] = None,
        model: str = "deepseek-chat"
    ) -> Dict[str, Any]:
        """外部 API 模式：调用 DeepSeek API"""

        if not self.client:
            return {
                "success": False,
                "agent_id": agent_id,
                "task": task,
                "error": "OpenAI SDK not available. Please install with: pip install openai"
            }

        # 构建系统提示
        system_prompt = self._build_agent_system_prompt(agent_id, agent_config)

        # 构建用户消息
        user_message = self._build_user_message(task, context)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=4000,
                stream=False
            )

            choice = response.choices[0]

            return {
                "success": True,
                "agent_id": agent_id,
                "task": task,
                "mode": "external_api",
                "response": choice.message.content,
                "usage": response.usage.model_dump() if response.usage else {},
                "model": response.model,
                "finish_reason": choice.finish_reason
            }

        except Exception as e:
            logger.error(f"Agent call failed: {e}")
            return {
                "success": False,
                "agent_id": agent_id,
                "task": task,
                "error": str(e)
            }
    
    def _build_builtin_llm_prompt(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """为内置 LLM 构建详细的角色提示"""

        prompt_parts = [
            f"# 🎭 角色激活：{agent_config.get('title', agent_id)} {agent_config.get('icon', '🤖')}",
            "",
            "## 🎯 角色定义",
            f"**身份**：{agent_config.get('role', '专业智能体')}",
            f"**风格**：{agent_config.get('style', '专业、高效')}",
            f"**专长**：{agent_config.get('focus', '任务执行')}",
            f"**特征**：{agent_config.get('identity', '专业助手')}",
            "",
            "## 📋 任务要求",
            f"**具体任务**：{task}",
            ""
        ]

        if context:
            prompt_parts.extend([
                "## 📊 上下文信息",
                ""
            ])

            for key, value in context.items():
                if isinstance(value, (dict, list)):
                    value = json.dumps(value, ensure_ascii=False, indent=2)
                prompt_parts.append(f"**{key}**：{value}")

            prompt_parts.append("")

        prompt_parts.extend([
            "## 🔧 工作原则",
            "- 严格按照角色身份进行专业回答",
            "- 提供具体、可操作的专业建议",
            "- 遵循行业最佳实践和标准",
            "- 确保输出质量和准确性",
            "- 保持角色一致性和专业性",
            "",
            "## 📝 输出格式要求",
            "请按照以下专业格式提供响应：",
            "",
            "### 1. 🎯 任务理解",
            "简要确认对任务的理解和分析重点",
            "",
            "### 2. 🔍 专业分析",
            "基于你的专业角色进行深入分析",
            "",
            "### 3. 💡 解决方案",
            "提供具体的解决方案或建议",
            "",
            "### 4. 📈 实施建议",
            "给出可操作的实施步骤和注意事项",
            "",
            "### 5. ⚠️ 风险提示",
            "指出潜在风险和预防措施",
            "",
            "---",
            "",
            "**💼 请现在以上述角色身份，按照专业标准回答用户的问题。**"
        ])

        return "\n".join(prompt_parts)

    def _build_agent_system_prompt(self, agent_id: str, agent_config: Dict[str, Any]) -> str:
        """构建智能体系统提示"""
        
        prompt_parts = [
            f"# {agent_config.get('title', agent_id)} {agent_config.get('icon', '🤖')}",
            "",
            f"你是一个专业的 {agent_config.get('role', '智能体')}。",
            "",
            "## 身份和角色",
            f"- 角色: {agent_config.get('role', '专业智能体')}",
            f"- 风格: {agent_config.get('style', '专业、高效')}",
            f"- 身份: {agent_config.get('identity', '专业助手')}",
            f"- 专注领域: {agent_config.get('focus', '任务执行')}",
            "",
            "## 工作原则",
            "- 始终保持专业和高效",
            "- 提供具体、可操作的建议",
            "- 遵循最佳实践和行业标准",
            "- 确保输出质量和准确性",
            "",
            "## 输出格式",
            "请按照以下格式提供响应:",
            "1. **任务理解**: 简要确认你对任务的理解",
            "2. **执行方案**: 详细的执行步骤或建议",
            "3. **输出结果**: 具体的交付物或结果",
            "4. **后续建议**: 下一步的建议或注意事项",
            "",
            "请确保你的回答专业、详细且具有可操作性。"
        ]
        
        return "\n".join(prompt_parts)
    
    def _build_user_message(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        """构建用户消息"""
        
        message_parts = [
            f"## 任务要求",
            task,
            ""
        ]
        
        if context:
            message_parts.extend([
                "## 上下文信息",
                ""
            ])
            
            for key, value in context.items():
                if isinstance(value, (dict, list)):
                    value = json.dumps(value, ensure_ascii=False, indent=2)
                message_parts.append(f"**{key}**: {value}")
            
            message_parts.append("")
        
        message_parts.extend([
            "请根据你的专业角色和上述要求，提供详细的回答和建议。"
        ])
        
        return "\n".join(message_parts)
    
    def generate_document(
        self,
        template: str,
        context: Dict[str, Any],
        agent_id: str = "pm"
    ) -> Dict[str, Any]:
        """使用模板生成文档"""

        task = f"""
请基于以下模板和上下文信息生成一个完整的文档：

## 模板内容
{template}

请根据上下文信息填充模板，生成一个完整、专业的文档。确保：
1. 所有占位符都被适当的内容替换
2. 内容逻辑清晰、结构完整
3. 符合专业文档的标准和格式
4. 包含所有必要的细节和信息
"""

        agent_config = {
            "title": "Document Generator",
            "role": "文档生成专家",
            "style": "专业、详细、结构化",
            "identity": "专业文档撰写助手",
            "focus": "高质量文档生成"
        }

        return self.call_agent(agent_id, agent_config, task, context)

    def analyze_requirements(
        self,
        requirements: str,
        project_type: str = "web-app"
    ) -> Dict[str, Any]:
        """分析需求"""

        task = f"""
请分析以下项目需求，并提供详细的分析报告：

## 项目需求
{requirements}

## 项目类型
{project_type}

请提供：
1. 需求分析和理解
2. 功能模块分解
3. 技术栈建议
4. 架构设计建议
5. 开发计划建议
6. 风险评估
"""

        agent_config = {
            "title": "Business Analyst",
            "role": "业务分析师",
            "style": "分析性、系统性、前瞻性",
            "identity": "专业需求分析专家",
            "focus": "需求分析和项目规划"
        }

        context = {
            "project_type": project_type,
            "requirements": requirements
        }

        return self.call_agent("analyst", agent_config, task, context)

# 全局 LLM 客户端实例
llm_client = None

def initialize_llm_client(api_key: str = None):
    """
    初始化 LLM 客户端

    Args:
        api_key: DeepSeek API Key（内置 LLM 模式下可选）
    """
    global llm_client
    llm_client = BMADLLMClient(api_key)
    logger.info(f"✅ LLM 客户端初始化完成 - 模式: {'内置 LLM' if USE_BUILTIN_LLM else 'DeepSeek API'}")
    return llm_client

def get_llm_client() -> Optional[BMADLLMClient]:
    """获取 LLM 客户端实例"""
    return llm_client