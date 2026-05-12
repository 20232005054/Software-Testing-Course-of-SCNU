# -*- coding: utf-8 -*-
# 辅助脚本 - 详细查看EC论坛页面的所有链接

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("详细查看EC论坛页面的所有链接")
print("========================================\n")

# 启动Chrome浏览器
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 直接访问EC论坛页面
    print("✅ 直接访问EC论坛页面")
    driver.get("https://www.ecshop.com/")
    sleep(5)  # 等待页面完全加载
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    print("\n========================================")
    print("查找所有链接：")
    print("========================================\n")
    
    # 查找所有链接
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"页面共有 {len(all_links)} 个链接\n")
    
    # 统计包含特定关键词的链接
    keywords = ["授权", "商业", "license", "商务", "合作", "购买", "价格", "版本"]
    matched_links = []
    
    for i, link in enumerate(all_links):
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            
            # 检查是否包含关键词
            is_matched = False
            for keyword in keywords:
                if keyword in text.lower() or (href and keyword in href.lower()):
                    is_matched = True
                    break
            
            if is_matched:
                matched_links.append((text, href))
                print(f"🎯 匹配链接 #{len(matched_links)}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print()
            elif text:  # 显示所有有文本的链接
                print(f"链接 #{i+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print()
        except:
            pass
    
    print("\n========================================")
    print(f"找到 {len(matched_links)} 个匹配的链接")
    print("========================================\n")
    
    for i, (text, href) in enumerate(matched_links):
        print(f"{i+1}. {text}")
        print(f"   {href}")
        print()
    
    print("\n========================================")
    print("保存页面源代码和截图")
    print("========================================\n")
    
    # 保存页面源代码
    with open("EC论坛详细页面源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("✅ 页面源代码已保存到: EC论坛详细页面源代码.html")
    
    # 截图
    driver.save_screenshot("EC论坛详细页面截图.png")
    print("✅ 页面截图已保存到: EC论坛详细页面截图.png")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
