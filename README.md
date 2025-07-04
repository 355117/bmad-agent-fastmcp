# 🤖 BMAD Agent FastMCP Service

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-Compatible-green.svg)](https://github.com/jlowin/fastmcp)
[![Cursor IDE](https://img.shields.io/badge/Cursor-IDE-purple.svg)](https://cursor.sh/)

> 🚀 **企业级智能体调用服务** - 基于 FastMCP 框架的专业 AI 智能体系统，支持双 LLM 模式，提供 25+ 个专业 MCP 工具和 10 个专业智能体，与 Cursor IDE 无缝集成。

## 🌟 核心亮点

- **🤖 10 个专业智能体**：业务分析师、架构师、全栈开发者、产品经理、QA 工程师等
- **🔧 25+ 个 MCP 工具**：智能体管理、工作流程控制、任务执行系统
- **🔄 双 LLM 模式**：支持 Cursor 内置 LLM 和 DeepSeek API 动态切换
- **📋 6 个工作流程**：全栈开发、API 开发、数据分析等完整流程
- **🎯 即插即用**：与 Cursor IDE 无缝集成

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑环境变量（可选）
# USE_BUILTIN_LLM=true          # 使用内置 LLM（默认）
# DEEPSEEK_API_KEY=your_key     # DeepSeek API Key（可选）
```

### 3. 启动服务
```bash
python bmad_agent_mcp.py
```

### 4. Cursor 集成
参考 `docs/CURSOR_USAGE_GUIDE.md` 进行 Cursor IDE 集成配置。

## ⭐ 核心特性

- **🤖 10 个专业智能体**：业务分析师、架构师、开发者、产品经理等
- **🔧 25 个 MCP 工具**：智能体管理、工作流程控制、任务执行、模板处理
- **🔄 双 LLM 模式**：支持 Cursor 内置 LLM 和 DeepSeek API 动态切换
- **📋 6 个工作流程**：全栈开发、API 开发、数据分析等完整流程
- **🎯 即插即用**：与 Cursor IDE 无缝集成

## 🔄 LLM 模式切换

### 内置 LLM 模式（默认）
- ✅ 使用 Cursor IDE 内置 LLM
- ✅ 无需外部 API 调用
- ✅ 响应更快，无网络延迟
- ✅ 无 API 费用

### 外部 API 模式
- ✅ 使用 DeepSeek API
- ✅ 更强的推理能力
- ✅ 支持更复杂的任务
- ⚠️ 需要 API Key 和网络连接

### 切换方法
```python
# 在 Cursor 中使用
switch_llm_mode('builtin')   # 切换到内置模式
switch_llm_mode('external')  # 切换到外部模式
get_llm_mode_info()          # 查看模式信息
```

## 🛠️ 主要 MCP 工具

### 智能体管理
- `list_agents()` - 列出所有智能体
- `get_agent_details(agent_id)` - 获取智能体详情
- `activate_agent(agent_id)` - 激活智能体
- `call_agent_with_llm(agent_id, task)` - 调用智能体执行任务

### 工作流程
- `list_workflows()` - 列出所有工作流程
- `start_workflow(workflow_id)` - 启动工作流程
- `get_workflow_status()` - 获取工作流程状态
- `advance_workflow_step()` - 推进工作流程

### LLM 功能
- `switch_llm_mode(mode)` - 切换 LLM 模式
- `get_llm_mode_info()` - 获取模式信息
- `get_system_status()` - 获取系统状态

### 任务和模板
- `list_tasks()` - 列出所有任务
- `execute_task(task_id)` - 执行任务
- `list_templates()` - 列出所有模板
- `get_template(template_name)` - 获取模板内容

## 📊 项目结构

```
📂 根目录
├── 📄 bmad_agent_mcp.py      # 主服务文件
├── 📄 llm_client.py          # LLM 客户端
├── 📄 utils.py               # 工具函数
├── 📄 requirements.txt       # 依赖文件
├── 📂 .bmad-core/            # 核心数据目录
├── 📁 docs/                  # 文档目录
├── 📁 tests/                 # 测试目录
└── 📁 archive/               # 归档目录
```

## 📚 文档

- **📖 [项目结构说明](PROJECT_STRUCTURE.md)** - 详细的项目结构和文件说明
- **🔄 [LLM 切换指南](docs/LLM_SWITCH_GUIDE.md)** - LLM 模式切换详细指南
- **🎯 [Cursor 使用指南](docs/CURSOR_USAGE_GUIDE.md)** - Cursor IDE 集成指南
- **🔍 [最终解决方案](docs/FINAL_SOLUTION_REPORT.md)** - 完整的解决方案报告

## 🧪 测试

```bash
# 运行基础测试
python tests/simple_test.py

# 测试 MCP 工具
python tests/simple_mcp_test.py

# 测试 LLM 功能
python tests/quick_llm_test.py
```

## 🔧 配置

### Cursor IDE 配置
将以下配置添加到 Cursor 的 `settings.json`：

```json
{
  "mcpServers": {
    "bmad-agent": {
      "command": "python",
      "args": ["path/to/bmad_agent_mcp.py"],
      "cwd": "path/to/project",
      "env": {
        "PYTHONPATH": "path/to/project",
        "USE_BUILTIN_LLM": "true",
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

### 环境变量
```bash
USE_BUILTIN_LLM=true                # 使用内置 LLM
DEEPSEEK_API_KEY=your_key_here     # DeepSeek API Key（可选）
PYTHONIOENCODING=utf-8             # 字符编码
```

## 🎯 使用示例

### 在 Cursor 中使用

```
用户: "请列出所有可用的 BMAD 智能体"
AI: 调用 list_agents()
返回: 10 个专业智能体列表

用户: "请使用业务分析师分析电商平台需求"
AI: 调用 call_agent_with_llm('analyst', '分析电商平台需求')
返回: 专业的业务分析结果

用户: "请切换到 DeepSeek API 模式"
AI: 调用 switch_llm_mode('external')
返回: 已切换到外部 API 模式
```

## 🤝 贡献

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证

MIT License

## 📚 相关

- 📖 查看 `docs/` 目录中的详细文档
- 🧪 运行 `tests/` 目录中的测试文件
- 📋 查看 `logs/` 目录中的日志文件
- 📦 查看 `archive/` 目录中的历史文件

## 🎯 BMAD 方法论

本项目基于 [BMAD-METHOD](https://github.com/bmadcode/BMAD-METHOD) 构建，这是一个强大的业务模型和架构开发方法论。

### 🚀 Important: Keep Your BMad Installation Updated 

Stay up-to-date effortlessly! If you already have BMad-METHOD installed in your project, simply run:

```bash
npx bmad-method install
# OR
git pull
npm run install:bmad
```

### 📦 First Time Installation

If you're new to BMAD-METHOD, visit the official repository for complete installation and setup instructions:

👉 **[BMAD-METHOD Official Repository](https://github.com/bmadcode/BMAD-METHOD)**

The BMAD-METHOD provides:
- 🎯 Structured business analysis frameworks
- 🏗️ Architecture design patterns
- 📋 Project management templates
- 🔄 Workflow automation tools
- 📊 Quality assurance checklists

---

**🎉 享受使用 BMAD Agent FastMCP Service！**