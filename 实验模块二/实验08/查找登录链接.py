# -*- coding: utf-8 -*-
# 查找登录链接

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(3)

try:
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    print("查找所有链接...")
    links = driver.find_elements(By.TAG_NAME, "a")
    
    for link in links:
        text = link.text.strip()
        href = link.get_attribute('href')
        if text and ('登' in text or 'user' in str(href).lower() or 'login' in str(href).lower()):
            print(f"文本: {text}")
            print(f"链接: {href}")
            print()
    
    input("按回车关闭...")
    
except Exception as e:
    print(f"错误: {e}")
    
finally:
    driver.quit()
