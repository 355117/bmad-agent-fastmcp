# LLM 模式切换详细指南

## 🎯 概述

BMAD Agent FastMCP Service 支持两种 LLM 模式，可以根据需要动态切换：

1. **内置 LLM 模式**：使用 Cursor IDE 的内置 LLM
2. **外部 API 模式**：使用 DeepSeek API

## 🔄 模式对比

| 特性 | 内置 LLM 模式 | 外部 API 模式 |
|------|---------------|---------------|
| **响应速度** | ⚡ 极快 | 🐌 较慢（网络延迟） |
| **费用** | 🆓 免费 | 💰 按使用付费 |
| **网络要求** | ❌ 无需网络 | ✅ 需要网络连接 |
| **API Key** | ❌ 不需要 | ✅ 需要 DeepSeek API Key |
| **推理能力** | 🔧 依赖 Cursor LLM | 🚀 DeepSeek 专业能力 |
| **集成度** | 🎯 与 Cursor 深度集成 | 🔌 独立服务 |

## 🛠️ 切换方法

### 方法 1：使用 MCP 工具（推荐）

在 Cursor 中直接与 AI 对话：

```
用户: "切换到内置 LLM 模式"
AI: 调用 switch_llm_mode('builtin')
返回: 已切换到内置 LLM 模式

用户: "切换到外部 API 模式"
AI: 调用 switch_llm_mode('external')
返回: 已切换到外部 API 模式

用户: "查看当前 LLM 模式"
AI: 调用 get_llm_mode_info()
返回: 当前模式详细信息
```

### 方法 2：环境变量

```bash
# 切换到内置 LLM 模式
set USE_BUILTIN_LLM=true

# 切换到外部 API 模式
set USE_BUILTIN_LLM=false

# 重启服务使配置生效
python bmad_agent_mcp.py
```

### 方法 3：配置文件

编辑 `.env` 文件：

```bash
# 内置 LLM 模式
USE_BUILTIN_LLM=true

# 外部 API 模式
USE_BUILTIN_LLM=false
DEEPSEEK_API_KEY=your_api_key_here
```

### 方法 4：命令行脚本

```bash
# 使用切换脚本
python switch_llm_mode.py --builtin    # 切换到内置模式
python switch_llm_mode.py --external   # 切换到外部模式
python switch_llm_mode.py --info       # 查看当前模式
```

## 🔧 内置 LLM 模式详解

### 工作原理

1. **智能体激活**：返回专业角色提示给 Cursor
2. **角色扮演**：Cursor LLM 根据提示扮演专业角色
3. **任务执行**：以专业身份完成用户任务
4. **结果返回**：直接在 Cursor 中显示结果

### 优势

- ✅ **零延迟**：无网络请求，即时响应
- ✅ **零费用**：不产生 API 调用费用
- ✅ **深度集成**：与 Cursor 工作流完美融合
- ✅ **离线工作**：无需网络连接
- ✅ **隐私保护**：数据不离开本地环境

### 适用场景

- 🎯 **日常开发**：代码编写、重构、调试
- 🎯 **快速原型**：快速验证想法和概念
- 🎯 **学习探索**：技术学习和实验
- 🎯 **团队协作**：统一的开发环境

## 🌐 外部 API 模式详解

### 工作原理

1. **请求转发**：将用户请求发送到 DeepSeek API
2. **专业处理**：DeepSeek 模型进行专业分析
3. **结果获取**：获取 API 返回的专业结果
4. **格式化输出**：将结果格式化后返回给用户

### 优势

- 🚀 **专业能力**：DeepSeek 的强大推理能力
- 🚀 **独立服务**：不依赖 IDE 的 LLM 能力
- 🚀 **一致性**：跨平台一致的响应质量
- 🚀 **可扩展**：支持更复杂的任务

### 适用场景

- 🎯 **复杂分析**：深度业务分析和架构设计
- 🎯 **专业咨询**：需要专业领域知识的任务
- 🎯 **批量处理**：大量数据的分析和处理
- 🎯 **高质量输出**：对输出质量有严格要求

## ⚙️ 配置详解

### 环境变量配置

```bash
# === LLM 模式配置 ===
USE_BUILTIN_LLM=true                    # true=内置模式, false=外部模式

# === DeepSeek API 配置 ===
DEEPSEEK_API_KEY=your_api_key_here      # DeepSeek API 密钥
DEEPSEEK_BASE_URL=https://api.deepseek.com  # API 基础 URL
DEEPSEEK_MODEL=deepseek-chat            # 使用的模型名称

# === 请求配置 ===
API_TIMEOUT=30                          # API 超时时间（秒）
API_RETRIES=3                           # 重试次数
API_RETRY_DELAY=1                       # 重试延迟（秒）

# === 缓存配置 ===
ENABLE_CACHE=true                       # 启用响应缓存
CACHE_TTL=3600                          # 缓存过期时间（秒）
CACHE_SIZE=100                          # 缓存大小

# === 日志配置 ===
LOG_LEVEL=INFO                          # 日志级别
LOG_LLM_REQUESTS=false                  # 是否记录 LLM 请求
```

### 动态配置

```python
# 在运行时动态切换
from llm_client import LLMClient

client = LLMClient()

# 切换到内置模式
client.switch_mode('builtin')

# 切换到外部模式
client.switch_mode('external')

# 获取当前模式信息
info = client.get_mode_info()
print(f"当前模式: {info['mode']}")
print(f"状态: {info['status']}")
```

## 🧪 测试和验证

### 模式切换测试

```bash
# 测试内置模式
python test_builtin_mode.py

# 测试外部模式
python test_external_mode.py

# 测试模式切换
python test_mode_switching.py
```

### 性能对比测试

```bash
# 运行性能对比
python benchmark_llm_modes.py

# 查看测试结果
cat logs/performance_comparison.log
```

### 功能验证

```python
# 验证智能体功能
def test_agent_functionality():
    # 测试内置模式
    switch_llm_mode('builtin')
    result1 = call_agent_with_llm('analyst', '分析市场趋势')
    
    # 测试外部模式
    switch_llm_mode('external')
    result2 = call_agent_with_llm('analyst', '分析市场趋势')
    
    # 比较结果
    compare_results(result1, result2)
```

## 🚨 故障排除

### 内置模式问题

**问题：智能体没有响应**
```bash
# 检查 Cursor LLM 状态
# 确保 Cursor 的 AI 功能正常工作

# 验证智能体配置
python validate_agents.py

# 检查角色提示
python check_role_prompts.py
```

**问题：角色扮演不准确**
```bash
# 更新智能体配置
python update_agent_configs.py

# 重新加载智能体
python reload_agents.py
```

### 外部模式问题

**问题：API 连接失败**
```bash
# 检查网络连接
ping api.deepseek.com

# 验证 API Key
python test_api_key.py

# 检查 API 配置
python check_api_config.py
```

**问题：请求超时**
```bash
# 增加超时时间
set API_TIMEOUT=60

# 启用重试机制
set API_RETRIES=5

# 检查网络质量
python test_network_quality.py
```

### 切换问题

**问题：模式切换不生效**
```bash
# 重启服务
python bmad_agent_mcp.py --restart

# 清理缓存
python clear_cache.py

# 重新加载配置
python reload_config.py
```

## 📊 监控和日志

### 模式使用统计

```python
# 查看模式使用统计
from utils import get_usage_stats

stats = get_usage_stats()
print(f"内置模式使用次数: {stats['builtin_count']}")
print(f"外部模式使用次数: {stats['external_count']}")
print(f"平均响应时间: {stats['avg_response_time']}ms")
```

### 性能监控

```bash
# 启用性能监控
set ENABLE_PERFORMANCE_MONITORING=true

# 查看性能报告
python generate_performance_report.py

# 实时监控
python monitor_performance.py
```

### 日志分析

```bash
# 分析 LLM 请求日志
python analyze_llm_logs.py

# 生成使用报告
python generate_usage_report.py

# 导出统计数据
python export_stats.py --format csv
```

## 🎯 最佳实践

### 1. 模式选择策略

```python
# 智能模式选择
def choose_optimal_mode(task_type, complexity, network_available):
    if not network_available:
        return 'builtin'
    
    if task_type in ['coding', 'debugging', 'refactoring']:
        return 'builtin'  # 快速响应更重要
    
    if complexity == 'high' and task_type in ['analysis', 'architecture']:
        return 'external'  # 专业能力更重要
    
    return 'builtin'  # 默认使用内置模式
```

### 2. 性能优化

```python
# 缓存策略
def optimize_performance():
    # 启用智能缓存
    enable_smart_cache()
    
    # 预热常用智能体
    preload_common_agents()
    
    # 优化网络连接
    optimize_network_settings()
```

### 3. 错误处理

```python
# 优雅降级
def handle_llm_error(error, current_mode):
    if current_mode == 'external' and is_network_error(error):
        # 网络问题时自动切换到内置模式
        switch_llm_mode('builtin')
        return retry_with_builtin_mode()
    
    return handle_generic_error(error)
```

## 🔗 相关资源

- [Cursor IDE 官方文档](https://cursor.sh/docs)
- [DeepSeek API 文档](https://platform.deepseek.com/docs)
- [FastMCP 框架文档](https://github.com/jlowin/fastmcp)
- [BMAD 方法论](https://github.com/bmadcode/BMAD-METHOD)

---

**🎉 通过合理的模式选择和配置，充分发挥 BMAD Agent 的强大功能！**