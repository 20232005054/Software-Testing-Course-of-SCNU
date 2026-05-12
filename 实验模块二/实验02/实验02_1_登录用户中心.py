# 实验02-1 - 登录并访问用户中心

# 1. 从selenium中导入webdriver模块
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 2. 从selenium.webdriver.common.by导入By
from selenium.webdriver.common.by import By

# 3. 从time导入sleep
from time import sleep

# (1) 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 隐式等待3秒
driver.implicitly_wait(3)

try:
    # (2) 打开前台登录页
    driver.get("http://localhost/upload/user.php")
    
    # (3) 输入用户名：vip
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("vip")
    
    # (4) 输入密码：vip
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("vip")
    
    # (5) 点击"立即登陆"
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    
    # (6) 等待1秒
    sleep(1)
    
    # (7) 点击界面上方"用户中心"
    # 尝试多种定位方式
    try:
        user_center = driver.find_element(By.LINK_TEXT, "用户中心")
    except:
        try:
            user_center = driver.find_element(By.PARTIAL_LINK_TEXT, "用户中心")
        except:
            user_center = driver.find_element(By.XPATH, "//a[contains(text(),'用户中心')]")
    user_center.click()
    
    # (8) 等待2秒
    sleep(2)
    
    # (9) 点击左侧"用户信息"
    try:
        user_info = driver.find_element(By.LINK_TEXT, "用户信息")
    except:
        try:
            user_info = driver.find_element(By.PARTIAL_LINK_TEXT, "用户信息")
        except:
            user_info = driver.find_element(By.XPATH, "//a[contains(text(),'用户信息')]")
    user_info.click()
    
    # (10) 等待5秒
    sleep(5)
    
    print("✅ 实验02-1完成！成功登录并访问用户信息页面")

except Exception as e:
    print(f"❌ 发生错误: {e}")

finally:
    # (11) 关闭浏览器
    driver.quit()
