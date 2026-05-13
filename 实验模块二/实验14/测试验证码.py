# -*- coding: utf-8 -*-
# 测试不同的验证码值

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
    
    # 填写表单
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("test@test.com")
    
    content_input = driver.find_element(By.NAME, "content")
    driver.execute_script("arguments[0].value = 'Test comment';", content_input)
    
    # 测试不同的验证码值
    test_captchas = ["0", "1234", ""]
    
    for captcha_value in test_captchas:
        print(f"\n测试验证码: '{captcha_value}'")
        
        # 输入验证码
        captcha_input = driver.find_element(By.NAME, "captcha")
        captcha_input.clear()
        if captcha_value:
            captcha_input.send_keys(captcha_value)
        
        # 查找提交按钮
        email_input = driver.find_element(By.NAME, "email")
        form = email_input.find_element(By.XPATH, "./ancestor::form")
        submit_button = form.find_element(By.XPATH, ".//input[@type='submit']")
        
        # 点击提交
        submit_button.click()
        sleep(2)
        
        # 检查alert
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"  结果: {alert_text}")
            alert.accept()
            sleep(1)
        except:
            print("  结果: 没有alert，可能提交成功")
            # 检查页面内容
            page_text = driver.find_element(By.TAG_NAME, "body").text
            if "成功" in page_text:
                print("  页面显示成功")
            break
    
    print("\n\n说明：")
    print("- 如果所有验证码都提示错误，说明前台不支持万能验证码")
    print("- 需要使用OCR识别或人工输入真实验证码")
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
