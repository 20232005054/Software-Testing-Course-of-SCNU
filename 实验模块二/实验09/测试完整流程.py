# -*- coding: utf-8 -*-
# 测试完整流程 - 添加商品到购物车并查找删除按钮

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("测试完整流程")
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
    sleep(3)
    
    # 加入购物车
    print("✅ 点击加入购物车")
    add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(@href,'addToCart')]")
    add_to_cart_button.click()
    sleep(6)
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    print("\n========================================")
    print("查找所有链接和图片：")
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
    
    # 查找所有图片
    print("\n========================================")
    print("查找所有图片：")
    print("========================================\n")
    
    all_images = driver.find_elements(By.TAG_NAME, "img")
    for i, img in enumerate(all_images):
        try:
            src = img.get_attribute("src")
            alt = img.get_attribute("alt")
            onclick = img.get_attribute("onclick")
            parent = img.find_element(By.XPATH, "..")
            parent_tag = parent.tag_name
            parent_onclick = parent.get_attribute("onclick")
            
            if alt or onclick or parent_onclick:
                print(f"图片 #{i+1}:")
                print(f"  src: {src}")
                print(f"  alt: {alt}")
                if onclick:
                    print(f"  onclick: {onclick}")
                if parent_onclick:
                    print(f"  父元素: {parent_tag}")
                    print(f"  父元素onclick: {parent_onclick}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("保存页面源代码和截图")
    print("========================================\n")
    
    # 保存页面源代码
    with open("购物车有商品页面源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("✅ 页面源代码已保存到: 购物车有商品页面源代码.html")
    
    # 截图
    driver.save_screenshot("购物车有商品页面截图.png")
    print("✅ 页面截图已保存到: 购物车有商品页面截图.png")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
