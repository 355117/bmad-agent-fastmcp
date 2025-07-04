#!/usr/bin/env python3
"""
简单的 MCP 工具测试

测试 BMAD Agent FastMCP Service 的 MCP 工具功能
"""

import sys
import json
from pathlib import Path

def test_mcp_tools():
    """测试 MCP 工具"""
    print("🧪 测试 MCP 工具")
    print("-" * 30)
    
    try:
        # 导入主服务
        from bmad_agent_mcp import app
        
        print("✅ MCP 服务导入成功")
        
        # 获取所有工具
        tools = app.list_tools()
        print(f"   发现 {len(tools)} 个 MCP 工具")
        
        # 按类别分组显示工具
        tool_categories = {
            '智能体管理': [],
            '工作流程': [],
            'LLM 功能': [],
            '任务和模板': [],
            '其他': []
        }
        
        for tool in tools:
            tool_name = tool.name
            if any(keyword in tool_name for keyword in ['agent', 'activate']):
                tool_categories['智能体管理'].append(tool_name)
            elif any(keyword in tool_name for keyword in ['workflow', 'step']):
                tool_categories['工作流程'].append(tool_name)
            elif any(keyword in tool_name for keyword in ['llm', 'mode', 'switch']):
                tool_categories['LLM 功能'].append(tool_name)
            elif any(keyword in tool_name for keyword in ['task', 'template']):
                tool_categories['任务和模板'].append(tool_name)
            else:
                tool_categories['其他'].append(tool_name)
        
        for category, tool_list in tool_categories.items():
            if tool_list:
                print(f"\n   📂 {category}:")
                for tool_name in tool_list[:3]:  # 只显示前3个
                    print(f"      - {tool_name}")
                if len(tool_list) > 3:
                    print(f"      ... 还有 {len(tool_list) - 3} 个工具")
        
        return True
        
    except Exception as e:
        print(f"❌ MCP 工具测试失败: {e}")
        return False

def test_agent_tools():
    """测试智能体相关工具"""
    print("\n🧪 测试智能体工具")
    print("-" * 30)
    
    try:
        from bmad_agent_mcp import (
            list_agents,
            get_agent_details,
            activate_agent
        )
        
        # 测试列出智能体
        agents_result = list_agents()
        print(f"✅ 列出智能体: 发现 {len(agents_result.get('agents', []))} 个智能体")
        
        # 显示前几个智能体
        agents = agents_result.get('agents', [])
        if agents:
            print("   前几个智能体:")
            for agent in agents[:3]:
                print(f"      - {agent['id']}: {agent['title']}")
        
        # 测试获取智能体详情
        if agents:
            first_agent_id = agents[0]['id']
            details_result = get_agent_details(first_agent_id)
            print(f"✅ 获取智能体详情: {first_agent_id}")
            print(f"   角色: {details_result.get('role', 'N/A')}")
            print(f"   专长: {details_result.get('expertise', 'N/A')}")
        
        # 测试激活智能体
        if agents:
            first_agent_id = agents[0]['id']
            activate_result = activate_agent(first_agent_id)
            print(f"✅ 激活智能体: {activate_result.get('message', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ 智能体工具测试失败: {e}")
        return False

def test_workflow_tools():
    """测试工作流程工具"""
    print("\n🧪 测试工作流程工具")
    print("-" * 30)
    
    try:
        from bmad_agent_mcp import (
            list_workflows,
            get_workflow_status
        )
        
        # 测试列出工作流程
        workflows_result = list_workflows()
        workflows = workflows_result.get('workflows', [])
        print(f"✅ 列出工作流程: 发现 {len(workflows)} 个工作流程")
        
        # 显示工作流程
        if workflows:
            print("   可用工作流程:")
            for workflow in workflows:
                print(f"      - {workflow['id']}: {workflow['name']}")
        
        # 测试获取工作流程状态
        status_result = get_workflow_status()
        print(f"✅ 工作流程状态: {status_result.get('status', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ 工作流程工具测试失败: {e}")
        return False

def test_llm_tools():
    """测试 LLM 工具"""
    print("\n🧪 测试 LLM 工具")
    print("-" * 30)
    
    try:
        from bmad_agent_mcp import (
            get_llm_mode_info,
            switch_llm_mode,
            get_system_status
        )
        
        # 测试获取 LLM 模式信息
        mode_info = get_llm_mode_info()
        print(f"✅ LLM 模式信息:")
        print(f"   当前模式: {mode_info.get('current_mode', 'N/A')}")
        print(f"   状态: {mode_info.get('status', 'N/A')}")
        
        # 测试模式切换
        switch_result = switch_llm_mode('builtin')
        print(f"✅ 切换到内置模式: {switch_result.get('success', False)}")
        
        # 测试系统状态
        system_status = get_system_status()
        print(f"✅ 系统状态:")
        print(f"   服务状态: {system_status.get('service_status', 'N/A')}")
        print(f"   LLM 状态: {system_status.get('llm_status', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ LLM 工具测试失败: {e}")
        return False

def test_template_tools():
    """测试模板工具"""
    print("\n🧪 测试模板工具")
    print("-" * 30)
    
    try:
        from bmad_agent_mcp import (
            list_templates,
            get_template
        )
        
        # 测试列出模板
        templates_result = list_templates()
        templates = templates_result.get('templates', [])
        print(f"✅ 列出模板: 发现 {len(templates)} 个模板")
        
        # 显示模板
        if templates:
            print("   可用模板:")
            for template in templates[:5]:  # 只显示前5个
                print(f"      - {template['name']}: {template['description']}")
            if len(templates) > 5:
                print(f"      ... 还有 {len(templates) - 5} 个模板")
        
        # 测试获取模板内容
        if templates:
            first_template = templates[0]['name']
            template_content = get_template(first_template)
            print(f"✅ 获取模板内容: {first_template}")
            content_preview = template_content.get('content', '')[:100]
            print(f"   内容预览: {content_preview}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 模板工具测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 BMAD Agent MCP 工具测试")
    print("=" * 50)
    
    tests = [
        ("MCP 工具", test_mcp_tools),
        ("智能体工具", test_agent_tools),
        ("工作流程工具", test_workflow_tools),
        ("LLM 工具", test_llm_tools),
        ("模板工具", test_template_tools)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ 测试 '{test_name}' 出现异常: {e}")
            results.append((test_name, False))
    
    # 总结
    print("\n" + "=" * 50)
    print("📊 MCP 工具测试结果")
    print("-" * 30)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"   {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 总体结果: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有 MCP 工具测试都通过了！")
        return 0
    else:
        print("⚠️  部分 MCP 工具测试失败，请检查服务配置。")
        return 1

if __name__ == "__main__":
    sys.exit(main())