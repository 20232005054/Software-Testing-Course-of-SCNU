# -*- coding: utf-8 -*-
# 直接访问商品详情页查看结构

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 直接访问一个商品详情页（诺基亚N85的ID是1）
    driver.get("http://localhost/upload/goods.php?id=1")
    sleep(3)
    
    print(f"当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    print("\n" + "="*60)
    
    # 查找所有链接
    print("\n所有链接（前30个）：")
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"共找到 {len(links)} 个链接\n")
    
    for idx, link in enumerate(links[:30], 1):
        text = link.text.strip()
        href = link.get_attribute("href")
        if text or "user.php" in (href or ""):
            print(f"{idx}. '{text}' -> {href}")
    
    # 查找包含"登录"或"注册"的链接
    print("\n" + "="*60)
    print("\n包含'登录'或'注册'的链接：")
    
    login_links = driver.find_elements(By.XPATH, "//a[contains(text(),'登录') or contains(text(),'注册') or contains(@href,'user.php')]")
    print(f"找到 {len(login_links)} 个\n")
    
    for idx, link in enumerate(login_links, 1):
        print(f"{idx}. 文本: '{link.text}'")
        print(f"   href: {link.get_attribute('href')}")
        print(f"   class: {link.get_attribute('class')}")
        
        # 获取父元素信息
        try:
            parent = link.find_element(By.XPATH, "./..")
            print(f"   父元素: <{parent.tag_name} class='{parent.get_attribute('class')}'>")
        except:
            pass
        print()
    
    print("\n按Enter继续...")
    input()
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
