# -*- coding: utf-8 -*-
# 快速查看评论表单

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
    
    print("查找评论表单...")
    
    # 查找包含comment的表单
    forms = driver.find_elements(By.TAG_NAME, "form")
    for idx, form in enumerate(forms, 1):
        action = form.get_attribute("action")
        if "comment" in (action or "").lower():
            print(f"\n找到评论表单 #{idx}:")
            print(f"  action: {action}")
            print(f"  method: {form.get_attribute('method')}")
            
            # 查找提交按钮
            buttons = form.find_elements(By.XPATH, ".//input[@type='submit'] | .//button")
            print(f"  提交按钮数量: {len(buttons)}")
            for btn in buttons:
                print(f"    - name={btn.get_attribute('name')} value={btn.get_attribute('value')}")
    
    # 直接查找评论提交按钮
    print("\n\n直接查找所有提交按钮:")
    all_submits = driver.find_elements(By.XPATH, "//input[@type='submit']")
    for idx, btn in enumerate(all_submits, 1):
        name = btn.get_attribute('name')
        value = btn.get_attribute('value')
        print(f"{idx}. name='{name}' value='{value}'")
        
        # 检查是否在评论表单中
        try:
            form = btn.find_element(By.XPATH, "./ancestor::form")
            action = form.get_attribute("action")
            if "comment" in (action or "").lower():
                print(f"   ✅ 这是评论表单的提交按钮！")
        except:
            pass
    
    sleep(1)
    
except Exception as e:
    print(f"错误: {e}")
    
finally:
    driver.quit()
