# -*- coding: utf-8 -*-
# 辅助脚本 - 查找商品详情页面的所有按钮和链接

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("查找商品详情页面的所有元素")
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
    print("查找所有按钮：")
    print("========================================\n")
    
    # 查找所有input按钮
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(all_inputs):
        try:
            input_type = inp.get_attribute("type")
            value = inp.get_attribute("value")
            name = inp.get_attribute("name")
            id_attr = inp.get_attribute("id")
            
            if input_type in ["button", "submit", "image"]:
                print(f"按钮 #{i+1}:")
                print(f"  type: {input_type}")
                print(f"  id: {id_attr}")
                print(f"  name: {name}")
                print(f"  value: {value}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("保存页面源代码和截图")
    print("========================================\n")
    
    # 保存页面源代码
    with open("商品详情页面源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("✅ 页面源代码已保存到: 商品详情页面源代码.html")
    
    # 截图
    driver.save_screenshot("商品详情页面截图.png")
    print("✅ 页面截图已保存到: 商品详情页面截图.png")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
