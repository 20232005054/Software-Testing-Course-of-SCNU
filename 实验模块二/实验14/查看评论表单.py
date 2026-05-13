# -*- coding: utf-8 -*-
# 辅助工具 - 查看商品详情页的评论表单结构

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 访问P806商品详情页
    driver.get("http://localhost/upload/goods.php?id=24")
    sleep(2)
    
    print(f"当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    print("\n" + "="*60)
    
    # 滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    
    # 查找所有表单
    print("\n所有表单（<form>标签）：")
    forms = driver.find_elements(By.TAG_NAME, "form")
    print(f"共找到 {len(forms)} 个表单\n")
    
    for idx, form in enumerate(forms, 1):
        action = form.get_attribute("action")
        method = form.get_attribute("method")
        name = form.get_attribute("name")
        print(f"表单 #{idx}:")
        print(f"  action: {action}")
        print(f"  method: {method}")
        print(f"  name: {name}")
        
        # 查找表单内的输入框
        inputs = form.find_elements(By.TAG_NAME, "input")
        print(f"  包含 {len(inputs)} 个input元素")
        for inp in inputs[:10]:  # 只显示前10个
            print(f"    - type={inp.get_attribute('type')} name={inp.get_attribute('name')} value={inp.get_attribute('value')}")
        
        # 查找表单内的textarea
        textareas = form.find_elements(By.TAG_NAME, "textarea")
        print(f"  包含 {len(textareas)} 个textarea元素")
        for ta in textareas:
            print(f"    - name={ta.get_attribute('name')}")
        print()
    
    # 查找所有提交按钮
    print("="*60)
    print("\n所有提交按钮：")
    
    submit_buttons = driver.find_elements(By.XPATH, "//input[@type='submit'] | //button[@type='submit']")
    print(f"找到 {len(submit_buttons)} 个提交按钮\n")
    
    for idx, btn in enumerate(submit_buttons, 1):
        print(f"按钮 #{idx}:")
        print(f"  type: {btn.get_attribute('type')}")
        print(f"  name: {btn.get_attribute('name')}")
        print(f"  value: {btn.get_attribute('value')}")
        print(f"  text: {btn.text}")
        
        # 获取按钮所在的表单
        try:
            form = btn.find_element(By.XPATH, "./ancestor::form")
            form_action = form.get_attribute("action")
            print(f"  所在表单action: {form_action}")
        except:
            print(f"  不在表单内")
        print()
    
    # 查找评论相关的元素
    print("="*60)
    print("\n查找评论相关元素：")
    
    try:
        comment_elements = driver.find_elements(By.XPATH, "//*[contains(@name,'comment') or contains(@id,'comment') or contains(text(),'评论')]")
        print(f"找到 {len(comment_elements)} 个相关元素\n")
        
        for idx, elem in enumerate(comment_elements[:10], 1):
            print(f"{idx}. 标签: {elem.tag_name}")
            print(f"   name: {elem.get_attribute('name')}")
            print(f"   id: {elem.get_attribute('id')}")
            print(f"   type: {elem.get_attribute('type')}")
            print(f"   文本: {elem.text[:50] if elem.text else ''}")
            print()
    except Exception as e:
        print(f"查找失败: {e}")
    
    print("\n按Enter继续...")
    input()
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
