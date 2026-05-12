# -*- coding: utf-8 -*-
# 辅助脚本 - 保存后台页面源代码和截图

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("保存后台页面源代码和截图")
print("========================================\n")

# 启动Chrome浏览器
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 登录后台
    print("✅ 登录后台")
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("admin")
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123")
    
    captcha_input = driver.find_element(By.NAME, "captcha")
    captcha_input.send_keys("0")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    sleep(8)
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    # 保存页面源代码
    with open("后台首页源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("\n✅ 页面源代码已保存到: 后台首页源代码.html")
    
    # 截图
    driver.save_screenshot("后台首页截图.png")
    print("✅ 页面截图已保存到: 后台首页截图.png")
    
    # 查找所有链接
    print("\n========================================")
    print("查找所有链接：")
    print("========================================\n")
    
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"页面共有 {len(all_links)} 个链接\n")
    
    for i, link in enumerate(all_links[:50]):  # 只显示前50个
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            
            if text:
                print(f"链接 #{i+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print()
        except:
            pass
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
