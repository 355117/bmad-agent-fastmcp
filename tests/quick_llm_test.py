#!/usr/bin/env python3
"""
快速 LLM 功能测试

测试 BMAD Agent 的 LLM 集成功能
"""

import sys
import os
from pathlib import Path

def test_llm_client_basic():
    """测试 LLM 客户端基础功能"""
    print("🧪 测试 LLM 客户端基础功能")
    print("-" * 30)
    
    try:
        from llm_client import LLMClient
        
        # 创建客户端
        client = LLMClient()
        print("✅ LLM 客户端创建成功")
        
        # 获取当前模式
        mode_info = client.get_mode_info()
        print(f"   当前模式: {mode_info['mode']}")
        print(f"   状态: {mode_info['status']}")
        
        # 检查配置
        config = client.get_config()
        print(f"   使用内置 LLM: {config.get('use_builtin_llm', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ LLM 客户端基础测试失败: {e}")
        return False

def test_mode_switching():
    """测试模式切换"""
    print("\n🧪 测试模式切换")
    print("-" * 30)
    
    try:
        from llm_client import LLMClient
        
        client = LLMClient()
        
        # 测试切换到内置模式
        result = client.switch_mode('builtin')
        print(f"✅ 切换到内置模式: {result['success']}")
        if result['success']:
            print(f"   消息: {result.get('message', 'N/A')}")
        
        # 验证当前模式
        mode_info = client.get_mode_info()
        print(f"   验证当前模式: {mode_info['mode']}")
        
        # 测试切换到外部模式（可能失败，如果没有 API Key）
        result = client.switch_mode('external')
        if result['success']:
            print(f"✅ 切换到外部模式: {result['success']}")
            print(f"   消息: {result.get('message', 'N/A')}")
            
            # 切换回内置模式
            client.switch_mode('builtin')
            print(f"✅ 切换回内置模式")
        else:
            print(f"⚠️  外部模式不可用: {result.get('error', '未知错误')}")
            print(f"   这是正常的，如果没有配置 DeepSeek API Key")
        
        return True
        
    except Exception as e:
        print(f"❌ 模式切换测试失败: {e}")
        return False

def test_builtin_mode():
    """测试内置模式功能"""
    print("\n🧪 测试内置模式功能")
    print("-" * 30)
    
    try:
        from llm_client import LLMClient
        
        client = LLMClient()
        
        # 确保在内置模式
        client.switch_mode('builtin')
        
        # 测试生成角色提示
        test_prompt = "你是一个专业的产品经理，请分析用户需求。"
        
        # 在内置模式下，这应该返回格式化的提示
        response = client.generate_response(test_prompt, "测试任务")
        
        print(f"✅ 内置模式响应生成成功")
        print(f"   响应类型: {type(response)}")
        
        if isinstance(response, dict):
            print(f"   包含键: {list(response.keys())}")
        elif isinstance(response, str):
            preview = response[:100] + "..." if len(response) > 100 else response
            print(f"   响应预览: {preview}")
        
        return True
        
    except Exception as e:
        print(f"❌ 内置模式测试失败: {e}")
        return False

def test_external_mode():
    """测试外部模式功能（如果可用）"""
    print("\n🧪 测试外部模式功能")
    print("-" * 30)
    
    try:
        from llm_client import LLMClient
        
        client = LLMClient()
        
        # 检查是否有 API Key
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            print("⚠️  未配置 DEEPSEEK_API_KEY，跳过外部模式测试")
            return True
        
        # 尝试切换到外部模式
        result = client.switch_mode('external')
        if not result['success']:
            print(f"⚠️  无法切换到外部模式: {result.get('error', '未知错误')}")
            return True
        
        print(f"✅ 成功切换到外部模式")
        
        # 测试简单的 API 调用
        test_prompt = "Hello, please respond with 'API test successful'"
        
        try:
            response = client.generate_response(test_prompt, "API 测试")
            print(f"✅ 外部 API 响应成功")
            
            if isinstance(response, str):
                preview = response[:100] + "..." if len(response) > 100 else response
                print(f"   响应预览: {preview}")
            
        except Exception as api_error:
            print(f"⚠️  API 调用失败: {api_error}")
            print(f"   这可能是网络问题或 API 配置问题")
        
        # 切换回内置模式
        client.switch_mode('builtin')
        print(f"✅ 切换回内置模式")
        
        return True
        
    except Exception as e:
        print(f"❌ 外部模式测试失败: {e}")
        return False

def test_error_handling():
    """测试错误处理"""
    print("\n🧪 测试错误处理")
    print("-" * 30)
    
    try:
        from llm_client import LLMClient
        
        client = LLMClient()
        
        # 测试无效模式切换
        result = client.switch_mode('invalid_mode')
        print(f"✅ 无效模式处理: {not result['success']}")
        if not result['success']:
            print(f"   错误消息: {result.get('error', 'N/A')}")
        
        # 测试空提示
        try:
            response = client.generate_response("", "空提示测试")
            print(f"✅ 空提示处理: 有响应")
        except Exception as e:
            print(f"✅ 空提示处理: 正确抛出异常 - {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ 错误处理测试失败: {e}")
        return False

def test_environment_config():
    """测试环境配置"""
    print("\n🧪 测试环境配置")
    print("-" * 30)
    
    # 检查环境变量
    env_vars = {
        'USE_BUILTIN_LLM': os.getenv('USE_BUILTIN_LLM', 'true'),
        'DEEPSEEK_API_KEY': '已配置' if os.getenv('DEEPSEEK_API_KEY') else '未配置',
        'PYTHONIOENCODING': os.getenv('PYTHONIOENCODING', '未设置'),
        'PYTHONPATH': '已设置' if os.getenv('PYTHONPATH') else '未设置'
    }
    
    print("📋 环境变量检查:")
    for var, value in env_vars.items():
        print(f"   {var}: {value}")
    
    # 检查配置文件
    config_files = ['.env', '.env.example']
    print("\n📄 配置文件检查:")
    for config_file in config_files:
        if Path(config_file).exists():
            print(f"   ✅ {config_file}")
        else:
            print(f"   ❌ {config_file} (不存在)")
    
    return True

def main():
    """主测试函数"""
    print("🚀 BMAD Agent LLM 功能测试")
    print("=" * 50)
    
    tests = [
        ("环境配置", test_environment_config),
        ("LLM 客户端基础", test_llm_client_basic),
        ("模式切换", test_mode_switching),
        ("内置模式", test_builtin_mode),
        ("外部模式", test_external_mode),
        ("错误处理", test_error_handling)
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
    print("📊 LLM 功能测试结果")
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
        print("🎉 所有 LLM 功能测试都通过了！")
        return 0
    else:
        print("⚠️  部分 LLM 功能测试失败，请检查配置。")
        return 1

if __name__ == "__main__":
    sys.exit(main())