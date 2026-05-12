# 查找登录和注册页面元素的辅助脚本

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

print("=" * 60)
print("查找登录页面元素")
print("=" * 60)

# 打开登录页
driver.get("http://localhost/upload/user.php")
sleep(2)

# 查找用户名输入框
username_fields = [
    ("NAME", "username"),
    ("NAME", "user"),
    ("ID", "username"),
    ("ID", "user"),
]

print("\n[用户名输入框]")
for method, value in username_fields:
    try:
        if method == "NAME":
            driver.find_element(By.NAME, value)
        elif method == "ID":
            driver.find_element(By.ID, value)
        print(f"✅ By.{method}, '{value}'")
        break
    except:
        print(f"❌ By.{method}, '{value}'")

# 查找密码输入框
print("\n[密码输入框]")
password_fields = [
    ("NAME", "password"),
    ("NAME", "pwd"),
    ("ID", "password"),
]

for method, value in password_fields:
    try:
        if method == "NAME":
            driver.find_element(By.NAME, value)
        elif method == "ID":
            driver.find_element(By.ID, value)
        print(f"✅ By.{method}, '{value}'")
        break
    except:
        print(f"❌ By.{method}, '{value}'")

# 查找登录按钮
print("\n[登录按钮]")
login_buttons = [
    ("NAME", "submit"),
    ("XPATH", "//input[@type='submit']"),
    ("XPATH", "//button[contains(text(),'登')]"),
]

for method, value in login_buttons:
    try:
        if method == "NAME":
            driver.find_element(By.NAME, value)
        elif method == "XPATH":
            driver.find_element(By.XPATH, value)
        print(f"✅ By.{method}, '{value}'")
        break
    except:
        print(f"❌ By.{method}, '{value}'")

print("\n" + "=" * 60)
print("查找注册页面元素")
print("=" * 60)

# 打开注册页
driver.get("http://localhost/upload/user.php?act=register")
sleep(2)

# 查找注册表单字段
print("\n[注册表单字段]")
register_fields = ["username", "email", "password", "confirm_password"]

for field in register_fields:
    try:
        driver.find_element(By.NAME, field)
        print(f"✅ By.NAME, '{field}'")
    except:
        print(f"❌ By.NAME, '{field}'")

print("\n按任意键关闭浏览器...")
input()

driver.quit()
