# 🤝 Contributing to BMAD Agent FastMCP Service

感谢您对 BMAD Agent FastMCP Service 项目的关注！我们欢迎所有形式的贡献。

## 🎯 贡献方式

### 🐛 报告 Bug
- 使用 [GitHub Issues](https://github.com/your-username/bmad-agent-fastmcp/issues) 报告问题
- 提供详细的错误描述和复现步骤
- 包含系统环境信息（Python 版本、操作系统等）

### 💡 功能建议
- 在 Issues 中提出新功能建议
- 详细描述功能需求和使用场景
- 讨论实现方案的可行性

### 🔧 代码贡献
1. Fork 项目到您的 GitHub 账户
2. 创建功能分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'Add amazing feature'`
4. 推送到分支：`git push origin feature/amazing-feature`
5. 创建 Pull Request

## 📋 开发指南

### 环境设置
```bash
# 克隆项目
git clone https://github.com/your-username/bmad-agent-fastmcp.git
cd bmad-agent-fastmcp

# 安装依赖
pip install -r requirements.txt

# 运行测试
python tests/simple_test.py
```

### 代码规范
- 遵循 PEP 8 Python 代码规范
- 使用有意义的变量和函数名
- 添加适当的注释和文档字符串
- 保持代码简洁和可读性

### 测试要求
- 新功能必须包含相应的测试
- 确保所有现有测试通过
- 测试覆盖率应保持在合理水平

## 🏗️ 项目结构

```
📂 bmad-agent-fastmcp/
├── 📄 bmad_agent_mcp.py     # 主服务文件
├── 📄 llm_client.py         # LLM 客户端
├── 📄 utils.py              # 工具函数
├── 📁 .bmad-core/           # 核心数据
├── 📁 docs/                 # 文档
├── 📁 tests/                # 测试
└── 📁 archive/              # 归档
```

## 🎨 添加新智能体

1. 在 `.bmad-core/agents/` 目录创建新的智能体配置文件
2. 按照现有格式定义智能体属性
3. 在 `bmad_agent_mcp.py` 中注册新智能体
4. 添加相应的测试

## 🔄 添加新工作流程

1. 在 `.bmad-core/workflows/` 目录创建工作流程定义
2. 定义步骤和依赖关系
3. 实现工作流程逻辑
4. 添加文档和测试

## 📝 文档贡献

- 改进现有文档的清晰度和准确性
- 添加使用示例和最佳实践
- 翻译文档到其他语言
- 创建教程和指南

## 🔍 代码审查

所有 Pull Request 都会经过代码审查：
- 检查代码质量和规范
- 验证功能正确性
- 确保向后兼容性
- 评估性能影响

## 📞 联系方式

- GitHub Issues: 技术问题和功能建议
- Discussions: 一般讨论和问答
- Email: 私人或敏感问题

## 📜 行为准则

请遵循我们的行为准则：
- 尊重所有贡献者
- 保持建设性的讨论
- 欢迎新手和学习者
- 创造包容的环境

## 🎉 致谢

感谢所有为项目做出贡献的开发者！您的贡献让这个项目变得更好。

---

**Happy Coding! 🚀**