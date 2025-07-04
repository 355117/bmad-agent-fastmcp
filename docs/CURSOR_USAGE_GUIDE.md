# 在 Cursor 中使用 BMAD Agent FastMCP Service

## 🎯 双模式支持

BMAD Agent 现在支持两种 LLM 模式：

### 🔧 内置 LLM 模式（推荐）
- ✅ **使用 Cursor 内置 LLM**：直接利用 Cursor IDE 的 LLM 能力
- ✅ **无需外部 API**：不需要网络连接和 API 费用
- ✅ **响应更快**：即时响应，无网络延迟
- ✅ **深度集成**：与 Cursor 完美配合
- 🔧 **工作原理**：智能体工具返回角色提示，让 Cursor LLM 扮演专业角色

### 🌐 外部 API 模式（备选）
- ✅ **DeepSeek API**：使用专门的 LLM 模型
- ✅ **独立服务**：不依赖 IDE 的 LLM 能力
- ⚠️ **需要网络**：需要 API Key 和网络连接
- 🔧 **工作原理**：直接调用外部 API 获取智能体响应

## 🔄 模式切换

### 快速切换
```bash
# 切换到内置 LLM 模式（推荐）
python switch_llm_mode.py --builtin

# 切换到外部 API 模式
python switch_llm_mode.py --external

# 查看当前模式信息
python switch_llm_mode.py --info
```

### 环境变量控制
```bash
# 设置使用内置 LLM
set USE_BUILTIN_LLM=true

# 设置使用外部 API
set USE_BUILTIN_LLM=false
```

## 🚀 快速开始

### 1. 启动 FastMCP 服务

在 Cursor 的终端中运行：

```bash
# 确保在项目目录中
cd D:\234ffff

# 启动服务（内置 LLM 模式）
python bmad_agent_mcp.py
```

### 2. 配置 Cursor MCP

在 Cursor 的设置中添加 MCP 服务器配置：

**方法 1：使用配置脚本（推荐）**
```bash
python setup_cursor_mcp.py
```

**方法 2：手动配置**

打开 Cursor 设置 → MCP Servers，添加以下配置：

```json
{
  "bmad-agent": {
    "command": "python",
    "args": ["D:\\234ffff\\bmad_agent_mcp.py"],
    "cwd": "D:\\234ffff",
    "env": {
      "PYTHONPATH": "D:\\234ffff",
      "USE_BUILTIN_LLM": "true",
      "PYTHONIOENCODING": "utf-8",
      "PYTHONUNBUFFERED": "1"
    }
  }
}
```

### 3. 重启 Cursor

配置完成后重启 Cursor IDE，让 MCP 配置生效。

## 🎯 使用示例

### 基础使用

在 Cursor 中与 AI 对话时，可以直接使用 BMAD 智能体：

```
用户: "请列出所有可用的 BMAD 智能体"
AI: 调用 list_agents() 工具
返回: 10 个专业智能体的详细列表

用户: "使用产品经理分析一个电商平台的需求"
AI: 调用 call_agent_with_llm('pm', '分析电商平台需求') 工具
返回: 专业的产品需求分析
```

### 工作流程使用

```
用户: "启动全栈开发工作流程"
AI: 调用 start_workflow('greenfield-fullstack') 工具
返回: 工作流程已启动，显示当前步骤

用户: "推进到下一步"
AI: 调用 advance_workflow_step() 工具
返回: 工作流程推进到下一步骤
```

### LLM 模式切换

```
用户: "切换到 DeepSeek API 模式"
AI: 调用 switch_llm_mode('external') 工具
返回: 已切换到外部 API 模式

用户: "查看当前 LLM 模式信息"
AI: 调用 get_llm_mode_info() 工具
返回: 当前模式详细信息
```

## 🔧 高级配置

### 环境变量配置

创建 `.env` 文件：

```bash
# LLM 模式配置
USE_BUILTIN_LLM=true

# DeepSeek API 配置（可选）
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com

# 字符编码配置
PYTHONIOENCODING=utf-8
PYTHONUNBUFFERED=1

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=logs/bmad_agent.log
```

### Cursor 设置优化

在 Cursor 的 `settings.json` 中添加：

```json
{
  "mcpServers": {
    "bmad-agent": {
      "command": "python",
      "args": ["D:\\234ffff\\bmad_agent_mcp.py"],
      "cwd": "D:\\234ffff",
      "env": {
        "PYTHONPATH": "D:\\234ffff",
        "USE_BUILTIN_LLM": "true",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONUNBUFFERED": "1"
      }
    }
  },
  "mcp.timeout": 30000,
  "mcp.retries": 3
}
```

## 🐛 故障排除

### 常见问题

**1. 找不到智能体**
```bash
# 检查服务状态
python bmad_agent_mcp.py --test

# 验证 .bmad-core 目录
python validate_bmad_core.py
```

**2. 编码问题**
```bash
# 设置正确的编码
set PYTHONIOENCODING=utf-8
set PYTHONUNBUFFERED=1
```

**3. 路径问题**
```bash
# 检查 Python 路径
echo %PYTHONPATH%

# 设置正确的路径
set PYTHONPATH=D:\234ffff
```

### 调试模式

启用详细日志：

```bash
# 启动调试模式
python bmad_agent_mcp.py --debug

# 查看日志
type logs\bmad_agent.log
```

### 测试连接

```bash
# 测试 MCP 连接
python test_mcp_connection.py

# 测试智能体功能
python test_agent_functionality.py

# 测试 LLM 集成
python test_llm_integration.py
```

## 📊 性能优化

### 内置 LLM 模式优化

- ✅ **快速响应**：平均响应时间 < 1 秒
- ✅ **低资源占用**：内存使用 < 100MB
- ✅ **高并发支持**：支持多个并发请求

### 外部 API 模式优化

- 🔧 **连接池**：复用 HTTP 连接
- 🔧 **缓存机制**：缓存常用响应
- 🔧 **重试机制**：自动重试失败请求

## 🎯 最佳实践

### 1. 模式选择

- **日常开发**：使用内置 LLM 模式
- **复杂分析**：可切换到外部 API 模式
- **团队协作**：统一使用内置模式

### 2. 工作流程

- **新项目**：使用 greenfield 工作流程
- **现有项目**：使用 brownfield 工作流程
- **特定需求**：选择对应的专业智能体

### 3. 性能优化

- **批量操作**：使用工作流程而非单个智能体
- **缓存利用**：重复使用相同的智能体配置
- **资源管理**：定期清理日志和缓存

## 🔗 相关链接

- [项目结构说明](../PROJECT_STRUCTURE.md)
- [LLM 切换指南](LLM_SWITCH_GUIDE.md)
- [最终解决方案](FINAL_SOLUTION_REPORT.md)
- [故障排除指南](TROUBLESHOOTING.md)

---

**🎉 享受使用 BMAD Agent FastMCP Service 在 Cursor 中的强大功能！**