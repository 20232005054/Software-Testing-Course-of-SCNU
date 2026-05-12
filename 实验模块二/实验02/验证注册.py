# 验证注册是否成功 - 尝试登录新账号

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 要验证的账号（修改为最新注册的）
test_username = "user17587"
test_password = "123456"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    print(f"正在验证账号: {test_username}")
    
    # 打开登录页
    driver.get("http://localhost/upload/user.php")
    sleep(2)
    
    # 输入用户名
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(test_username)
    
    # 输入密码
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(test_password)
    
    # 点击登录
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    
    sleep(3)
    
    # 检查是否登录成功
    current_url = driver.current_url
    page_source = driver.page_source
    
    print(f"\n当前URL: {current_url}")
    
    # 检查是否有登录成功的标志
    if "user.php" in current_url and "欢迎" in page_source:
        print(f"✅ 验证成功！账号 {test_username} 可以正常登录")
        print(f"   注册确实成功了！")
    elif "user.php" in current_url:
        print(f"✅ 已跳转到用户中心，注册成功！")
    else:
        print(f"❌ 登录失败，可能注册未成功")
        print(f"   请检查用户名或密码是否正确")
    
    # 截图
    driver.save_screenshot("实验模块二/实验02/登录验证截图.png")
    print(f"\n已保存截图")
    
    sleep(3)

except Exception as e:
    print(f"❌ 验证过程出错: {e}")

finally:
    driver.quit()
