# -*- coding: utf-8 -*-
# 查找库存元素的详细信息

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(3)

try:
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    keyword_input = driver.find_element(By.NAME, "keywords")
    keyword_input.send_keys("100")
    driver.find_element(By.NAME, "imageField").click()
    sleep(3)
    
    driver.find_element(By.PARTIAL_LINK_TEXT, "金立").click()
    sleep(3)
    
    print("查找库存相关元素...")
    print("\n方法1: 查找所有包含'库存'的元素")
    elements = driver.find_elements(By.XPATH, "//*[contains(text(),'库存')]")
    for elem in elements:
        print(f"  标签: {elem.tag_name}")
        print(f"  文本: {elem.text}")
        print(f"  HTML: {elem.get_attribute('outerHTML')[:200]}")
        print()
    
    print("\n方法2: 查找库存后面的元素")
    try:
        stock_elem = driver.find_element(By.XPATH, "//*[contains(text(),'商品库存')]")
        parent = stock_elem.find_element(By.XPATH, "..")
        print(f"父元素HTML: {parent.get_attribute('outerHTML')[:500]}")
    except:
        pass
    
    print("\n方法3: 查找所有数字")
    page_source = driver.page_source
    import re
    if "商品库存" in page_source:
        # 查找"商品库存"后面的内容
        match = re.search(r'商品库存[：:]\s*(\d+)', page_source)
        if match:
            print(f"找到库存数字: {match.group(1)}")
        else:
            print("未找到库存数字")
            # 打印商品库存附近的HTML
            idx = page_source.find("商品库存")
            print(f"商品库存附近的HTML: {page_source[idx:idx+200]}")
    
    input("\n按回车关闭...")
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
