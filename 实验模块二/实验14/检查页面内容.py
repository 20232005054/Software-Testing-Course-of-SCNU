# -*- coding: utf-8 -*-
# 检查页面是否有评论功能

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
    
    # 获取页面文本
    page_text = driver.find_element(By.TAG_NAME, "body").text
    
    # 检查是否包含评论相关文字
    if "评论" in page_text:
        print("✅ 页面包含'评论'文字")
        
        # 查找包含"评论"的元素
        comment_elements = driver.find_elements(By.XPATH, "//*[contains(text(),'评论')]")
        print(f"找到 {len(comment_elements)} 个包含'评论'的元素\n")
        
        for idx, elem in enumerate(comment_elements[:5], 1):
            print(f"{idx}. {elem.tag_name}: {elem.text[:50]}")
    else:
        print("❌ 页面不包含'评论'文字")
    
    # 检查是否需要登录
    if "登录" in page_text or "请先登录" in page_text:
        print("\n⚠️ 可能需要登录才能评论")
    
    # 查找email输入框
    print("\n查找email输入框:")
    try:
        email_inputs = driver.find_elements(By.XPATH, "//input[contains(@name,'email') or contains(@name,'mail')]")
        print(f"找到 {len(email_inputs)} 个email输入框")
        for inp in email_inputs:
            print(f"  name={inp.get_attribute('name')} type={inp.get_attribute('type')}")
    except:
        print("未找到email输入框")
    
    # 查找textarea
    print("\n查找textarea:")
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    print(f"找到 {len(textareas)} 个textarea")
    for ta in textareas:
        print(f"  name={ta.get_attribute('name')} placeholder={ta.get_attribute('placeholder')}")
    
    # 查找验证码
    print("\n查找验证码:")
    captcha_imgs = driver.find_elements(By.XPATH, "//img[contains(@src,'captcha')]")
    print(f"找到 {len(captcha_imgs)} 个验证码图片")
    
    captcha_inputs = driver.find_elements(By.XPATH, "//input[contains(@name,'captcha') or contains(@name,'verify')]")
    print(f"找到 {len(captcha_inputs)} 个验证码输入框")
    
    sleep(1)
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
