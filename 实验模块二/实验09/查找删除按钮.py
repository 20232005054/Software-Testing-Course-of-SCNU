# -*- coding: utf-8 -*-
# 辅助脚本 - 查找购物车页面的删除按钮元素

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
    # 打开首页
    print("✅ 打开ECSHOP前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    # 搜索P806
    print("✅ 搜索P806商品")
    keyword_input = driver.find_element(By.NAME, "keywords")
    keyword_input.send_keys("P806")
    search_button = driver.find_element(By.NAME, "imageField")
    search_button.click()
    sleep(2)
    
    # 点击商品
    print("✅ 点击P806商品")
    product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "P806")
    product_link.click()
    sleep(2)
    
    # 加入购物车
    print("✅ 加入购物车")
    add_to_cart_button = driver.find_element(By.LINK_TEXT, "加入购物车")
    add_to_cart_button.click()
    sleep(5)
    
    print(f"\n当前URL: {driver.current_url}")
    print("\n========================================")
    print("查找所有可能的删除按钮：")
    print("========================================\n")
    
    # 查找所有链接
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"页面共有 {len(all_links)} 个链接\n")
    
    delete_links = []
    for i, link in enumerate(all_links):
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            onclick = link.get_attribute("onclick")
            
            # 查找包含"删除"或"delete"的链接
            if text and ("删除" in text or "delete" in text.lower()):
                print(f"找到删除链接 #{len(delete_links)+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print(f"  onclick: {onclick}")
                print()
                delete_links.append(link)
            elif href and "delete" in href.lower():
                print(f"找到删除链接 #{len(delete_links)+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print(f"  onclick: {onclick}")
                print()
                delete_links.append(link)
        except:
            pass
    
    # 查找所有图片按钮
    print("\n========================================")
    print("查找所有图片按钮：")
    print("========================================\n")
    
    all_images = driver.find_elements(By.TAG_NAME, "img")
    for img in all_images:
        try:
            src = img.get_attribute("src")
            alt = img.get_attribute("alt")
            title = img.get_attribute("title")
            
            if alt and ("删除" in alt or "delete" in alt.lower()):
                print(f"找到删除图片:")
                print(f"  src: {src}")
                print(f"  alt: {alt}")
                print(f"  title: {title}")
                print()
        except:
            pass
    
    # 查找所有input按钮
    print("\n========================================")
    print("查找所有input按钮：")
    print("========================================\n")
    
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in all_inputs:
        try:
            input_type = inp.get_attribute("type")
            value = inp.get_attribute("value")
            name = inp.get_attribute("name")
            onclick = inp.get_attribute("onclick")
            
            if value and ("删除" in value or "delete" in value.lower()):
                print(f"找到删除按钮:")
                print(f"  type: {input_type}")
                print(f"  name: {name}")
                print(f"  value: {value}")
                print(f"  onclick: {onclick}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("保存页面源代码到文件")
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
