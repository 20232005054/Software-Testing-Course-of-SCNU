# -*- coding: utf-8 -*-
# 辅助脚本 - 直接访问购物车页面查找删除按钮

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("查找购物车页面的删除按钮")
print("========================================\n")

# 启动Chrome浏览器
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 直接访问购物车页面（假设已有商品）
    print("✅ 打开购物车页面")
    driver.get("http://localhost/upload/flow.php")
    sleep(3)
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    print("\n========================================")
    print("查找所有链接：")
    print("========================================\n")
    
    # 查找所有链接
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"页面共有 {len(all_links)} 个链接\n")
    
    for i, link in enumerate(all_links):
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            onclick = link.get_attribute("onclick")
            
            if text:  # 只显示有文本的链接
                print(f"链接 #{i+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                if onclick:
                    print(f"  onclick: {onclick}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("查找所有图片：")
    print("========================================\n")
    
    # 查找所有图片
    all_images = driver.find_elements(By.TAG_NAME, "img")
    for i, img in enumerate(all_images):
        try:
            src = img.get_attribute("src")
            alt = img.get_attribute("alt")
            onclick = img.get_attribute("onclick")
            
            if alt or onclick:
                print(f"图片 #{i+1}:")
                print(f"  src: {src}")
                print(f"  alt: {alt}")
                if onclick:
                    print(f"  onclick: {onclick}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("保存页面源代码和截图")
    print("========================================\n")
    
    # 保存页面源代码
    with open("购物车页面源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("✅ 页面源代码已保存到: 购物车页面源代码.html")
    
    # 截图
    driver.save_screenshot("购物车页面截图.png")
    print("✅ 页面截图已保存到: 购物车页面截图.png")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
