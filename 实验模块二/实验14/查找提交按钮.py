# -*- coding: utf-8 -*-
# 查找评论提交按钮

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.maximize_window()

try:
    driver.get("http://localhost/upload/goods.php?id=24")
    sleep(2)
    
    # 滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    
    # 查找email输入框附近的提交按钮
    print("查找email输入框附近的元素...")
    email_input = driver.find_element(By.NAME, "email")
    
    # 获取email输入框的父元素
    parent = email_input.find_element(By.XPATH, "./..")
    print(f"email输入框的父元素: {parent.tag_name}")
    
    # 继续向上查找，找到表单或容器
    for i in range(5):
        try:
            parent = parent.find_element(By.XPATH, "./..")
            print(f"  第{i+1}层父元素: {parent.tag_name}")
            
            # 在这一层查找提交按钮
            buttons = parent.find_elements(By.XPATH, ".//input[@type='submit'] | .//input[@type='image'] | .//button")
            if buttons:
                print(f"    找到 {len(buttons)} 个按钮:")
                for btn in buttons:
                    tag = btn.tag_name
                    type_attr = btn.get_attribute('type')
                    name = btn.get_attribute('name')
                    value = btn.get_attribute('value')
                    src = btn.get_attribute('src')
                    print(f"      <{tag} type='{type_attr}' name='{name}' value='{value}' src='{src}'>")
        except:
            break
    
    # 查找所有图片类型的提交按钮
    print("\n查找所有图片类型的提交按钮:")
    image_buttons = driver.find_elements(By.XPATH, "//input[@type='image']")
    print(f"找到 {len(image_buttons)} 个")
    for idx, btn in enumerate(image_buttons, 1):
        name = btn.get_attribute('name')
        src = btn.get_attribute('src')
        alt = btn.get_attribute('alt')
        print(f"{idx}. name='{name}' src='{src}' alt='{alt}'")
    
    sleep(1)
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
