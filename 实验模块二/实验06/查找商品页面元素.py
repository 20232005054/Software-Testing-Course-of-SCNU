# -*- coding: utf-8 -*-
# 辅助工具：查找商品详情页面元素

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    print("正在打开首页...")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    # 搜索100
    print("\n搜索关键字100...")
    keyword_input = driver.find_element(By.NAME, "keywords")
    keyword_input.clear()
    keyword_input.send_keys("100")
    
    search_button = driver.find_element(By.NAME, "imageField")
    search_button.click()
    sleep(3)
    
    print(f"当前URL: {driver.current_url}")
    
    # 查找金立A30
    print("\n查找金立A30商品...")
    try:
        product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "金立")
        print(f"✅ 找到商品: {product_link.text}")
        product_link.click()
        sleep(3)
    except:
        print("❌ 未找到金立商品")
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    # 查找购买数量输入框
    print("\n[1] 查找购买数量输入框...")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        if inp.get_attribute('type') == 'text':
            name = inp.get_attribute('name')
            value = inp.get_attribute('value')
            inp_id = inp.get_attribute('id')
            print(f"  NAME: {name}, ID: {inp_id}, VALUE: {value}")
    
    # 查找库存信息
    print("\n[2] 查找库存信息...")
    page_text = driver.page_source
    if "库存" in page_text:
        print("✅ 页面包含库存信息")
        # 尝试查找包含库存的元素
        elements = driver.find_elements(By.XPATH, "//*[contains(text(),'库存')]")
        for elem in elements:
            print(f"  文本: {elem.text}")
    
    # 查找复选框
    print("\n[3] 查找复选框...")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    print(f"找到 {len(checkboxes)} 个复选框")
    for i, cb in enumerate(checkboxes, 1):
        name = cb.get_attribute('name')
        value = cb.get_attribute('value')
        cb_id = cb.get_attribute('id')
        checked = cb.is_selected()
        print(f"  复选框{i}: NAME={name}, VALUE={value}, ID={cb_id}, CHECKED={checked}")
        # 查找关联文本
        try:
            parent = cb.find_element(By.XPATH, "..")
            label_text = parent.text.strip()
            if label_text and len(label_text) < 50:
                print(f"    关联文本: {label_text}")
        except:
            pass
    
    # 查找总价
    print("\n[4] 查找总价信息...")
    elements = driver.find_elements(By.XPATH, "//*[contains(text(),'总价') or contains(text(),'￥')]")
    for elem in elements:
        text = elem.text.strip()
        if text and len(text) < 100:
            print(f"  文本: {text}")
            print(f"  标签: {elem.tag_name}")
            print(f"  ID: {elem.get_attribute('id')}")
            print(f"  CLASS: {elem.get_attribute('class')}")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
