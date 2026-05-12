# -*- coding: utf-8 -*-
# 辅助脚本 - 查找首页的注册按钮

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("查找首页的注册按钮")
print("========================================\n")

# 启动Chrome浏览器
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 打开首页
    print("✅ 打开ECSHOP前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(3)
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    print("\n========================================")
    print("查找所有链接：")
    print("========================================\n")
    
    # 查找所有链接
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"页面共有 {len(all_links)} 个链接\n")
    
    for i, link in enumerate(all_links[:50]):  # 只显示前50个
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            
            if text:  # 只显示有文本的链接
                print(f"链接 #{i+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("查找所有图片按钮：")
    print("========================================\n")
    
    # 查找所有图片
    all_images = driver.find_elements(By.TAG_NAME, "img")
    for i, img in enumerate(all_images[:30]):
        try:
            src = img.get_attribute("src")
            alt = img.get_attribute("alt")
            parent = img.find_element(By.XPATH, "..")
            parent_href = parent.get_attribute("href")
            
            if parent_href:
                print(f"图片链接 #{i+1}:")
                print(f"  图片src: {src}")
                print(f"  图片alt: {alt}")
                print(f"  链接href: {parent_href}")
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
