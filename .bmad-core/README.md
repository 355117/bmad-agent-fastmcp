# BMAD Core Configuration

这个目录包含 BMAD (Business Model and Architecture Development) 系统的核心配置文件。

## 📁 目录结构

- **`agents/`** - 智能体定义文件 (10个专业智能体)
- **`workflows/`** - 工作流程配置 (6种完整工作流程)
- **`tasks/`** - 任务定义文件 (19个任务配置)
- **`templates/`** - 文档模板 (11个专业模板)
- **`checklists/`** - 检查清单
- **`utils/`** - 工具和实用程序
- **`data/`** - 知识库和技术偏好
- **`agent-teams/`** - 智能体团队配置

## 🤖 智能体列表

1. **pm** 📋 - 产品经理
2. **analyst** 📊 - 业务分析师
3. **architect** 🏗️ - 系统架构师
4. **dev** 💻 - 开发工程师
5. **qa** 🧪 - 质量保证工程师
6. **ux-expert** 🎨 - 用户体验专家
7. **po** 📝 - 产品负责人
8. **sm** 🏃 - Scrum Master
9. **bmad-master** 🎯 - BMAD 主管
10. **bmad-orchestrator** 🎼 - BMAD 编排器

## 🔄 工作流程类型

1. **greenfield-fullstack** - 全栈新项目
2. **greenfield-service** - 服务端新项目
3. **greenfield-ui** - 前端新项目
4. **brownfield-fullstack** - 全栈现有项目
5. **brownfield-service** - 服务端现有项目
6. **brownfield-ui** - 前端现有项目

## 📋 核心任务

- 需求分析和文档创建
- 架构设计和技术选型
- 项目规划和工作流程管理
- 代码生成和质量保证
- 用户体验设计和优化

## 📄 文档模板

- PRD (产品需求文档)
- 架构设计文档
- 技术规范文档
- 项目简介模板
- 竞品分析模板
- 市场研究模板
- 用户故事模板

## 🚀 使用方式

通过 BMAD Agent FastMCP Service 调用这些配置：

```python
# 列出所有智能体
result = list_agents()

# 激活产品经理
result = activate_agent("pm")

# 调用智能体执行任务
result = call_agent("pm", "创建产品需求文档")

# 启动工作流程
result = start_workflow("greenfield-fullstack", "web-app")
```

## 📚 更多信息

详细的使用指南请参考项目根目录的文档：
- `README.md` - 项目概述
- `docs/CURSOR_USAGE_GUIDE.md` - Cursor IDE 使用指南
- `docs/LLM_SWITCH_GUIDE.md` - LLM 模式切换指南
- `FULL_VERSION_INFO.md` - 完整版本说明