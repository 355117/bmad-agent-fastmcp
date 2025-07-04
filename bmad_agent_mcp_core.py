#!/usr/bin/env python3
"""
BMAD Agent FastMCP Service - Core Version

基于 .bmad-core 的智能体调用服务，支持：
- 智能体管理和调用
- 工作流程执行
- 任务管理
- 模板处理
- 状态跟踪
- 双 LLM 模式（Cursor 内置 + DeepSeek API）

这是核心版本，包含主要的 25 个 MCP 工具。
完整版本请参考项目中的 bmad_agent_mcp.py 文件。
"""

import asyncio
import json
import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import re

from fastmcp import FastMCP
from utils import BMADUtils, format_scan_report
from llm_client import initialize_llm_client, get_llm_client

# 初始化 FastMCP 应用
mcp = FastMCP("BMAD Agent Service")

# 全局配置
SCRIPT_DIR = Path(__file__).resolve().parent
BMAD_CORE_PATH = SCRIPT_DIR / ".bmad-core"
CONFIG_FILE = BMAD_CORE_PATH / "core-config.yaml"

# LLM 配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
USE_BUILTIN_LLM = os.getenv("USE_BUILTIN_LLM", "true").lower() == "true"

# 初始化 LLM 客户端
if USE_BUILTIN_LLM:
    initialize_llm_client()
else:
    initialize_llm_client(DEEPSEEK_API_KEY)

@dataclass
class AgentInfo:
    """智能体信息"""
    id: str
    name: str
    title: str
    icon: str
    description: str
    when_to_use: str
    role: str
    style: str
    identity: str
    focus: str
    dependencies: Dict[str, List[str]]

@dataclass
class WorkflowInfo:
    """工作流程信息"""
    id: str
    name: str
    description: str
    type: str
    project_types: List[str]
    sequence: List[Dict[str, Any]]

@dataclass
class TaskInfo:
    """任务信息"""
    name: str
    description: str
    agent: Optional[str]
    dependencies: List[str]
    outputs: List[str]

class BMADCore:
    """BMAD 核心管理器"""
    
    def __init__(self):
        self.agents: Dict[str, AgentInfo] = {}
        self.workflows: Dict[str, WorkflowInfo] = {}
        self.tasks: Dict[str, TaskInfo] = {}
        self.templates: Dict[str, str] = {}
        self.current_agent: Optional[str] = None
        self.current_workflow: Optional[str] = None
        self.workflow_state: Dict[str, Any] = {}
        self.load_core_config()
        self.discover_agents()
        self.discover_workflows()
        self.discover_tasks()
        self.discover_templates()
    
    def load_core_config(self):
        """加载核心配置"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {}
    
    def discover_agents(self):
        """发现所有智能体"""
        agents_dir = BMAD_CORE_PATH / "agents"
        if not agents_dir.exists():
            return
        
        for agent_file in agents_dir.glob("*.md"):
            agent_id = agent_file.stem
            agent_info = self.parse_agent_file(agent_file)
            if agent_info:
                self.agents[agent_id] = agent_info
    
    def parse_agent_file(self, file_path: Path) -> Optional[AgentInfo]:
        """解析智能体文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取 YAML 配置
            yaml_match = re.search(r'```yaml\n(.*?)\n```', content, re.DOTALL)
            if not yaml_match:
                return None
            
            yaml_content = yaml_match.group(1)
            config = yaml.safe_load(yaml_content)
            
            agent_config = config.get('agent', {})
            persona_config = config.get('persona', {})
            dependencies = config.get('dependencies', {})
            
            return AgentInfo(
                id=agent_config.get('id', file_path.stem),
                name=agent_config.get('name', ''),
                title=agent_config.get('title', ''),
                icon=agent_config.get('icon', '🤖'),
                description=agent_config.get('description', agent_config.get('title', '')),
                when_to_use=agent_config.get('whenToUse', ''),
                role=persona_config.get('role', ''),
                style=persona_config.get('style', ''),
                identity=persona_config.get('identity', ''),
                focus=persona_config.get('focus', ''),
                dependencies=dependencies
            )
        except Exception as e:
            print(f"Error parsing agent file {file_path}: {e}")
            return None
    
    def discover_workflows(self):
        """发现所有工作流程"""
        workflows_dir = BMAD_CORE_PATH / "workflows"
        if not workflows_dir.exists():
            return
        
        for workflow_file in workflows_dir.glob("*.yaml"):
            workflow_info = self.parse_workflow_file(workflow_file)
            if workflow_info:
                self.workflows[workflow_info.id] = workflow_info
    
    def parse_workflow_file(self, file_path: Path) -> Optional[WorkflowInfo]:
        """解析工作流程文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            workflow_config = config.get('workflow', {})
            
            return WorkflowInfo(
                id=workflow_config.get('id', file_path.stem),
                name=workflow_config.get('name', ''),
                description=workflow_config.get('description', ''),
                type=workflow_config.get('type', ''),
                project_types=workflow_config.get('project_types', []),
                sequence=workflow_config.get('sequence', [])
            )
        except Exception as e:
            print(f"Error parsing workflow file {file_path}: {e}")
            return None
    
    def discover_tasks(self):
        """发现所有任务"""
        tasks_dir = BMAD_CORE_PATH / "tasks"
        if not tasks_dir.exists():
            return
        
        for task_file in tasks_dir.glob("*.md"):
            task_name = task_file.stem
            self.tasks[task_name] = TaskInfo(
                name=task_name,
                description=f"Task: {task_name}",
                agent=None,
                dependencies=[],
                outputs=[]
            )
    
    def discover_templates(self):
        """发现所有模板"""
        templates_dir = BMAD_CORE_PATH / "templates"
        if not templates_dir.exists():
            return
        
        for template_file in templates_dir.glob("*.md"):
            template_name = template_file.stem
            try:
                with open(template_file, 'r', encoding='utf-8') as f:
                    self.templates[template_name] = f.read()
            except Exception as e:
                print(f"Error reading template {template_file}: {e}")

# 全局 BMAD 核心实例
bmad_core = BMADCore()

# ============================================================================
# MCP 工具定义
# ============================================================================

@mcp.tool()
def list_agents() -> Dict[str, Any]:
    """列出所有可用的智能体"""
    agents_list = []
    for agent_id, agent in bmad_core.agents.items():
        agents_list.append({
            "id": agent.id,
            "name": agent.name,
            "title": agent.title,
            "icon": agent.icon,
            "description": agent.description,
            "when_to_use": agent.when_to_use,
            "role": agent.role
        })
    
    return {
        "success": True,
        "count": len(agents_list),
        "agents": agents_list,
        "message": f"找到 {len(agents_list)} 个智能体"
    }

@mcp.tool()
def get_agent_details(agent_id: str) -> Dict[str, Any]:
    """获取智能体详细信息"""
    if agent_id not in bmad_core.agents:
        return {
            "success": False,
            "error": f"智能体 '{agent_id}' 不存在"
        }
    
    agent = bmad_core.agents[agent_id]
    return {
        "success": True,
        "agent": asdict(agent)
    }

@mcp.tool()
def activate_agent(agent_id: str) -> Dict[str, Any]:
    """激活指定的智能体"""
    if agent_id not in bmad_core.agents:
        return {
            "success": False,
            "error": f"智能体 '{agent_id}' 不存在"
        }
    
    bmad_core.current_agent = agent_id
    agent = bmad_core.agents[agent_id]
    
    return {
        "success": True,
        "activated_agent": agent_id,
        "agent_info": {
            "title": agent.title,
            "icon": agent.icon,
            "role": agent.role,
            "description": agent.description
        },
        "message": f"✅ 智能体 '{agent.title} {agent.icon}' 已激活"
    }

# 注意：这是核心版本，完整的 25 个 MCP 工具请参考 bmad_agent_mcp.py 文件

if __name__ == "__main__":
    print("🚀 BMAD Agent FastMCP Service (Core Version)")
    print(f"📁 BMAD Core Path: {BMAD_CORE_PATH}")
    print(f"🤖 发现 {len(bmad_core.agents)} 个智能体")
    print(f"🔄 发现 {len(bmad_core.workflows)} 个工作流程")
    print(f"📋 发现 {len(bmad_core.tasks)} 个任务")
    print(f"📄 发现 {len(bmad_core.templates)} 个模板")
    print(f"🔧 LLM 模式: {'内置 LLM' if USE_BUILTIN_LLM else 'DeepSeek API'}")
    print("\n✅ 服务已启动，等待 MCP 连接...")
    
    # 运行 FastMCP 服务
    mcp.run()