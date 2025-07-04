# 📁 BMAD Agent FastMCP 项目结构

## 🎯 项目概述

BMAD Agent FastMCP Service 是一个基于 FastMCP 框架的智能体调用服务，支持双 LLM 模式（Cursor 内置 LLM + DeepSeek API），提供 25 个专业 MCP 工具和 10 个专业智能体。

## 📂 目录结构

```
bmad-agent-fastmcp/
├── 📁 .bmad-core/                    # 核心数据目录（不要修改）
│   ├── agents/                       # 10 个智能体配置
│   ├── workflows/                    # 6 个工作流程
│   ├── tasks/                        # 19 个任务定义
│   └── templates/                    # 11 个模板文件
│
├── 📄 bmad_agent_mcp.py             # 🔒 主服务文件（25个MCP工具）
├── 📄 llm_client.py                 # 🔒 LLM 客户端（双模式支持）
├── 📄 utils.py                      # 🔒 工具函数
├── 📄 requirements.txt              # 🔒 Python 依赖
├── 📄 .env                          # 🔒 环境变量配置
│
├── 📁 docs/                         # 📚 文档和说明文件
├── 📁 tests/                        # 🧪 测试文件
├── 📁 logs/                         # 📋 日志文件
├── 📁 archive/                      # 📦 归档文件
└── 📁 __pycache__/                  # 🔒 Python 缓存
```

## 🔒 核心文件（重要，不要移动）

### 主要文件

| 文件 | 描述 | 重要性 |
|------|------|--------|
| `bmad_agent_mcp.py` | 主服务文件，包含 25 个 MCP 工具 | ⭐⭐⭐⭐⭐ |
| `llm_client.py` | LLM 客户端，支持双模式切换 | ⭐⭐⭐⭐⭐ |
| `utils.py` | 核心工具函数和 BMADCore 类 | ⭐⭐⭐⭐⭐ |
| `requirements.txt` | Python 依赖包列表 | ⭐⭐⭐⭐ |
| `.env` | 环境变量配置 | ⭐⭐⭐⭐ |

### 数据目录

| 目录 | 描述 | 文件数量 |
|------|------|----------|
| `.bmad-core/agents/` | 智能体配置文件 | 10 个 |
| `.bmad-core/workflows/` | 工作流程定义 | 6 个 |
| `.bmad-core/tasks/` | 任务配置 | 19 个 |
| `.bmad-core/templates/` | 文档模板 | 11 个 |

## 🚀 快速开始

### 1. 核心文件检查
```bash
# 确保核心文件存在
ls bmad_agent_mcp.py llm_client.py utils.py requirements.txt
```

### 2. 环境配置
```bash
# 安装依赖
pip install -r requirements.txt

# 检查环境变量
cat .env
```

### 3. 启动服务
```bash
# 直接运行主服务
python bmad_agent_mcp.py
```

### 4. Cursor 集成
参考 `docs/CURSOR_USAGE_GUIDE.md` 进行 Cursor IDE 集成配置。

## 🔧 维护指南

### 重要文件保护

**🚨 绝对不要修改或删除：**
- `bmad_agent_mcp.py` - 主服务文件
- `llm_client.py` - LLM 客户端
- `utils.py` - 核心工具
- `.bmad-core/` - 数据目录
- `requirements.txt` - 依赖文件

### 安全修改

**✅ 可以安全修改：**
- `.env` - 环境变量（谨慎修改）
- `docs/` 目录下的文档
- `tests/` 目录下的测试文件
- `archive/` 目录下的归档文件

### 添加新功能

1. **新增 MCP 工具**：在 `bmad_agent_mcp.py` 中添加
2. **新增智能体**：在 `.bmad-core/agents/` 中添加配置文件
3. **新增工作流程**：在 `.bmad-core/workflows/` 中添加定义
4. **新增文档**：在 `docs/` 目录中添加

## 📊 项目统计

- **总文件数**：约 60+ 个文件
- **核心文件**：5 个关键文件
- **MCP 工具**：25 个专业工具
- **智能体**：10 个专业角色
- **工作流程**：6 个完整流程
- **支持模式**：双 LLM 模式

## 🎯 使用建议

1. **日常开发**：主要关注根目录的核心文件
2. **查看文档**：访问 `docs/` 目录
3. **运行测试**：访问 `tests/` 目录
4. **问题调试**：查看 `logs/` 目录
5. **历史参考**：查看 `archive/` 目录

## 🔄 版本管理

建议使用 Git 管理项目，重点跟踪：
- 所有核心文件
- `.bmad-core/` 目录
- `docs/` 目录中的重要文档
- 配置文件

**忽略文件**：
- `__pycache__/`
- `*.log`
- 临时测试文件

---

**📝 注意**：这个项目结构经过精心设计，确保了核心功能的稳定性和代码的可维护性。请遵循上述指南进行开发和维护。