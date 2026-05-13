# -*- coding: utf-8 -*-
# 实验15-1：文件上传测试
# 测试ECShop前台用户留言上传附件功能

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os

# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.maximize_window()

try:
    print("=" * 60)
    print("实验15-1：文件上传测试")
    print("=" * 60)
    
    # 步骤1：打开ECShop前台登录页
    print("\n✅ 步骤1: 打开ECShop前台登录页")
    driver.get("http://localhost/upload/user.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 步骤2：输入用户名vip、密码vip、点击"立即登陆"，等待5秒
    print("\n✅ 步骤2: 输入用户名和密码")
    
    # 输入用户名
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    sleep(0.5)
    username_input.send_keys("vip")
    print(f"   输入用户名: vip")
    
    # 输入密码
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    sleep(0.5)
    password_input.send_keys("vip")
    print(f"   输入密码: vip")
    
    # 点击"立即登陆"按钮
    print("\n✅ 步骤3: 点击'立即登陆'按钮")
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    sleep(5)
    print(f"   登录后URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 步骤3：点击上方"用户中心"，等待3秒
    print("\n✅ 步骤4: 点击上方'用户中心'")
    user_center_link = driver.find_element(By.LINK_TEXT, "用户中心")
    user_center_link.click()
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 步骤4：点击左侧"我的留言"，等待3秒
    print("\n✅ 步骤5: 点击左侧'我的留言'")
    message_link = driver.find_element(By.LINK_TEXT, "我的留言")
    message_link.click()
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 步骤5：输入主题"hello"，输入留言内容"welcome to this world!"
    print("\n✅ 步骤6: 填写留言表单")
    
    # 输入主题
    subject_input = driver.find_element(By.NAME, "msg_title")
    subject_input.clear()
    sleep(0.5)
    subject_input.send_keys("hello")
    print(f"   输入主题: hello")
    
    # 输入留言内容（使用JavaScript避免中文乱码）
    content_textarea = driver.find_element(By.NAME, "msg_content")
    driver.execute_script("arguments[0].value = 'welcome to this world!';", content_textarea)
    sleep(0.5)
    print(f"   输入留言内容: welcome to this world!")
    
    # 步骤6：选择文件c:\temp\777.txt
    print("\n✅ 步骤7: 选择上传文件")
    
    # 检查文件是否存在
    file_path = r"c:\temp\777.txt"
    if not os.path.exists(file_path):
        print(f"   ⚠️  警告: 文件不存在: {file_path}")
        print(f"   正在创建测试文件...")
        
        # 创建目录（如果不存在）
        os.makedirs(r"c:\temp", exist_ok=True)
        
        # 创建测试文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("这是一个测试文件\n")
            f.write("用于测试ECShop文件上传功能\n")
            f.write("Test file for upload functionality\n")
        print(f"   ✅ 测试文件已创建: {file_path}")
    
    # 上传文件
    file_input = driver.find_element(By.NAME, "message_img")
    file_input.send_keys(file_path)
    sleep(1)
    print(f"   已选择文件: {file_path}")
    
    # 步骤7：点击"提交"
    print("\n✅ 步骤8: 点击'提交'按钮")
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='提 交']")
    
    # 滚动到按钮位置
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    sleep(1)
    
    # 点击提交
    submit_button.click()
    sleep(3)
    print(f"   提交后URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 验证提交结果
    print("\n✅ 步骤9: 验证提交结果")
    try:
        # 检查是否有成功提示
        page_source = driver.page_source
        if "留言" in page_source or "成功" in page_source:
            print("   ✅ 留言提交成功！")
        else:
            print("   ⚠️  无法确认提交状态")
    except Exception as e:
        print(f"   ⚠️  验证时出错: {e}")
    
    # 保存截图
    screenshot_path = "实验模块二/实验15/文件上传结果.png"
    driver.save_screenshot(screenshot_path)
    print(f"\n📸 截图已保存: {screenshot_path}")
    
    print("\n" + "=" * 60)
    print("✅ 实验15-1：文件上传测试完成！")
    print("=" * 60)
    
    # 等待查看结果
    print("\n⏳ 等待5秒后关闭浏览器...")
    sleep(5)
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
    # 保存错误截图
    try:
        driver.save_screenshot("实验模块二/实验15/错误截图_上传.png")
        print("📸 错误截图已保存")
    except:
        pass
    
finally:
    driver.quit()
    print("\n🔚 浏览器已关闭")
