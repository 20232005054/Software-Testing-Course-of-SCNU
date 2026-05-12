# 实验02-2 - 注册新会员

# 1. 从selenium中导入webdriver模块
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 2. 从selenium.webdriver.common.by导入By
from selenium.webdriver.common.by import By

# 3. 从time导入sleep
from time import sleep
import random

# (1) 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 隐式等待3秒
driver.implicitly_wait(3)

try:
    # (2) 打开注册页
    driver.get("http://localhost/upload/user.php?act=register")
    
    # (3) 注册成为一个新会员
    # 生成随机用户名，避免重复
    random_num = random.randint(10000, 99999)
    new_username = f"user{random_num}"
    
    print(f"正在注册新用户: {new_username}")
    
    # 填写用户名 *
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(new_username)
    
    # 填写邮箱 *
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(f"{new_username}@test.com")
    
    # 填写密码 *
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("123456")
    
    # 确认密码 *
    confirm_password_input = driver.find_element(By.NAME, "confirm_password")
    confirm_password_input.send_keys("123456")
    
    # 填写扩展字段（MSN、QQ、办公电话、家庭电话、手机）
    try:
        extend_field1 = driver.find_element(By.NAME, "extend_field1")
        extend_field1.send_keys(f"{new_username}@msn.com")  # MSN
    except:
        pass
    
    try:
        extend_field2 = driver.find_element(By.NAME, "extend_field2")
        extend_field2.send_keys(f"{random_num}")  # QQ
    except:
        pass
    
    try:
        extend_field3 = driver.find_element(By.NAME, "extend_field3")
        extend_field3.send_keys("010-12345678")  # 办公电话
    except:
        pass
    
    try:
        extend_field4 = driver.find_element(By.NAME, "extend_field4")
        extend_field4.send_keys("010-87654321")  # 家庭电话
    except:
        pass
    
    try:
        extend_field5 = driver.find_element(By.NAME, "extend_field5")
        extend_field5.send_keys("13800138000")  # 手机
    except:
        pass
    
    # 选择密码提示问题 *
    try:
        from selenium.webdriver.support.ui import Select
        sel_question = Select(driver.find_element(By.NAME, "sel_question"))
        sel_question.select_by_index(1)  # 选择第一个问题
        print("已选择密码提示问题")
    except Exception as e:
        print(f"选择密码提示问题失败: {e}")
    
    # 填写密码问题答案 *
    try:
        passwd_answer = driver.find_element(By.NAME, "passwd_answer")
        passwd_answer.send_keys("测试答案123")
        print("已填写密码问题答案")
    except:
        print("未找到密码问题答案字段")
    
    # 勾选同意协议
    try:
        agreement = driver.find_element(By.NAME, "agreement")
        if not agreement.is_selected():
            agreement.click()
        print("已勾选用户协议")
    except:
        print("未找到协议复选框")
    
    # 等待2秒，让用户看到填写的内容
    sleep(2)
    
    # 点击注册按钮
    print("\n准备点击注册按钮...")
    try:
        # 先尝试找到注册按钮
        register_button = driver.find_element(By.NAME, "Submit")
        print(f"找到注册按钮: {register_button.get_attribute('value')}")
        
        # 滚动到按钮位置
        driver.execute_script("arguments[0].scrollIntoView();", register_button)
        sleep(1)
        
        # 点击按钮
        register_button.click()
        print("已点击注册按钮")
        
    except Exception as e:
        print(f"点击注册按钮失败: {e}")
        # 尝试其他方式
        try:
            register_button = driver.find_element(By.XPATH, "//input[@type='submit']")
            register_button.click()
            print("使用 XPATH 点击注册按钮成功")
        except:
            print("所有方式都失败了")
    
    # 等待5秒，查看注册结果
    sleep(5)
    
    # 检查当前页面URL和标题
    current_url = driver.current_url
    page_title = driver.title
    print(f"\n当前页面URL: {current_url}")
    print(f"当前页面标题: {page_title}")
    
    # 检查是否有错误提示
    try:
        # 查找可能的错误信息
        error_msgs = driver.find_elements(By.CLASS_NAME, "error")
        if error_msgs:
            print("\n发现错误信息:")
            for msg in error_msgs:
                if msg.text:
                    print(f"  - {msg.text}")
    except:
        pass
    
    # 截图保存
    try:
        screenshot_path = "实验模块二/实验02/注册结果截图.png"
        driver.save_screenshot(screenshot_path)
        print(f"\n已保存截图到: {screenshot_path}")
    except Exception as e:
        print(f"保存截图失败: {e}")
    
    print(f"✅ 实验02-2执行完成！")
    print(f"   用户名: {new_username}")
    print(f"   密码: 123456")
    print(f"   邮箱: {new_username}@test.com")
    print(f"\n请检查截图和页面信息，确认注册是否成功")
    
    # 等待3秒
    sleep(3)
    
    # ========== 验证注册是否成功 ==========
    print("\n" + "=" * 60)
    print("开始验证注册是否成功...")
    print("=" * 60)
    
    # 先退出登录（如果已登录）
    try:
        driver.get("http://localhost/upload/user.php?act=logout")
        sleep(1)
    except:
        pass
    
    # 重新打开登录页
    driver.get("http://localhost/upload/user.php")
    sleep(2)
    
    # 使用新注册的账号登录
    print(f"\n尝试使用新账号登录: {new_username}")
    
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(new_username)
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("123456")
    
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    
    sleep(3)
    
    # 检查登录结果
    current_url = driver.current_url
    page_source = driver.page_source
    
    if "user.php" in current_url and ("欢迎" in page_source or new_username in page_source):
        print(f"\n🎉 验证成功！")
        print(f"   ✅ 账号 {new_username} 注册成功")
        print(f"   ✅ 可以正常登录")
        
        # 保存登录成功的截图
        driver.save_screenshot("实验模块二/实验02/注册验证成功.png")
        print(f"   ✅ 已保存验证截图")
    else:
        print(f"\n❌ 验证失败")
        print(f"   注册可能未成功，请检查")
    
    # 再等待2秒让用户看到结果
    sleep(2)

except Exception as e:
    print(f"❌ 发生错误: {e}")
    print("提示：请检查注册页面的表单字段名称是否正确")

finally:
    # 关闭浏览器
    driver.quit()
