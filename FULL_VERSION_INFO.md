# 完整版本说明

## 📁 文件结构说明

### 核心文件

- **`bmad_agent_mcp_core.py`** - 核心版本（已上传）
  - 包含基础的 MCP 工具和核心功能
  - 适合快速了解项目结构和基本功能
  - 约 300 行代码

- **`bmad_agent_mcp.py`** - 完整版本（本地文件）
  - 包含完整的 25 个 MCP 工具
  - 支持所有功能：智能体调用、工作流程执行、任务管理等
  - 约 1086 行代码
  - **注意：由于文件较大，暂未上传到 GitHub**

### 支持文件

- **`llm_client.py`** ✅ 已上传 - LLM 客户端，支持双模式
- **`utils.py`** ✅ 已上传 - 工具函数和 BMAD 核心管理
- **`requirements.txt`** ✅ 已上传 - Python 依赖

## 🔧 完整版本的 25 个 MCP 工具

完整版本 `bmad_agent_mcp.py` 包含以下 MCP 工具：

### 智能体管理 (5个)
1. `list_agents()` - 列出所有智能体
2. `get_agent_details()` - 获取智能体详情
3. `activate_agent()` - 激活智能体
4. `call_agent()` - 调用智能体执行任务
5. `call_agent_with_llm()` - 使用 LLM 调用智能体

### 工作流程管理 (6个)
6. `list_workflows()` - 列出工作流程
7. `get_workflow_details()` - 获取工作流程详情
8. `start_workflow()` - 启动工作流程
9. `continue_workflow()` - 继续工作流程
10. `get_workflow_status()` - 获取工作流程状态
11. `reset_workflow()` - 重置工作流程

### 任务管理 (4个)
12. `list_tasks()` - 列出任务
13. `get_task_details()` - 获取任务详情
14. `execute_task()` - 执行任务
15. `get_task_history()` - 获取任务历史

### 模板管理 (3个)
16. `list_templates()` - 列出模板
17. `get_template()` - 获取模板内容
18. `generate_document()` - 生成文档

### 系统管理 (4个)
19. `get_system_status()` - 获取系统状态
20. `scan_bmad_core()` - 扫描 BMAD 核心
21. `get_core_config()` - 获取核心配置
22. `health_check()` - 健康检查

### LLM 模式管理 (3个)
23. `switch_llm_mode()` - 切换 LLM 模式
24. `get_llm_mode_info()` - 获取 LLM 模式信息
25. `test_llm_connection()` - 测试 LLM 连接

## 🚀 如何获取完整版本

### 方法 1：从本地项目复制
如果你有本地项目文件，完整版本位于：
```
./bmad_agent_mcp.py
```

### 方法 2：手动创建
你可以基于核心版本 `bmad_agent_mcp_core.py` 扩展，添加其余的 22 个 MCP 工具。

### 方法 3：联系开发者
如果需要完整版本，可以通过 GitHub Issues 联系项目维护者。

## 📋 功能对比

| 功能 | 核心版本 | 完整版本 |
|------|----------|----------|
| 基础智能体管理 | ✅ | ✅ |
| 智能体调用 | ❌ | ✅ |
| 工作流程执行 | ❌ | ✅ |
| 任务管理 | ❌ | ✅ |
| 模板处理 | ❌ | ✅ |
| LLM 模式切换 | ❌ | ✅ |
| 系统监控 | ❌ | ✅ |
| 双 LLM 支持 | ✅ | ✅ |

## 🔄 升级路径

1. **开发阶段**：使用核心版本进行基础测试
2. **生产阶段**：升级到完整版本获得全部功能
3. **企业部署**：基于完整版本进行定制开发

## 📞 技术支持

如果你需要完整版本或有任何问题，请：

1. 提交 GitHub Issue
2. 查看项目文档
3. 参考 `docs/` 目录中的详细指南

---

**注意**：核心版本已经包含了项目的主要架构和基础功能，可以作为学习和开发的起点。