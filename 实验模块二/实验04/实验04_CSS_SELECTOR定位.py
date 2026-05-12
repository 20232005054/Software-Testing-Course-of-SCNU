# -*- coding: utf-8 -*-
# 实验04 - CSS_SELECTOR高级定位
# 要求：所有元素必须使用CSS_SELECTOR选择器进行定位

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("实验04 - CSS_SELECTOR高级定位")
print("========================================\n")

# 1. 启动Chrome浏览器
print("✅ 步骤1: 启动Chrome浏览器")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    # 2. 打开前台首页
    print("✅ 步骤2: 打开前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 3. 点击"留言板"按钮，等待3秒
    print("✅ 步骤3: 点击留言板按钮")
    # 使用CSS选择器定位留言板链接
    message_board = driver.find_element(By.CSS_SELECTOR, "a[href*='message']")
    message_board.click()
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    
    # 4. 在电子邮件地址文本框里输入vip@163.com
    print("✅ 步骤4: 输入电子邮件地址")
    # 使用CSS选择器定位邮箱输入框
    email_input = driver.find_element(By.CSS_SELECTOR, "input[name='user_email']")
    # 滚动到元素可见
    driver.execute_script("arguments[0].scrollIntoView();", email_input)
    sleep(0.5)
    email_input.clear()
    sleep(0.5)
    email_input.send_keys("vip@163.com")
    # 验证输入
    email_value = email_input.get_attribute("value")
    print(f"   邮箱输入框当前值: {email_value}")
    
    # 5. 判断"询问"按钮是否选中，若否，选中"询问"按钮，等待2秒
    print("✅ 步骤5: 检查并选中询问按钮")
    # 使用CSS选择器定位"询问"单选按钮（value="2"）
    inquiry_radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][name='msg_type'][value='2']")
    
    # 判断是否已选中
    if inquiry_radio.is_selected():
        print("   询问按钮已选中")
    else:
        print("   询问按钮未选中，正在选中...")
        # 滚动到元素可见
        driver.execute_script("arguments[0].scrollIntoView();", inquiry_radio)
        sleep(0.5)
        inquiry_radio.click()
        sleep(0.5)
        # 验证是否选中
        if inquiry_radio.is_selected():
            print("   ✓ 询问按钮已成功选中")
        else:
            print("   ⚠️  询问按钮选中失败")
    
    sleep(2)
    
    # 6. 在主题文本框中输入"维修"
    print("✅ 步骤6: 输入主题")
    # 使用CSS选择器定位主题输入框
    subject_input = driver.find_element(By.CSS_SELECTOR, "input[name='msg_title']")
    # 滚动到元素可见
    driver.execute_script("arguments[0].scrollIntoView();", subject_input)
    sleep(0.5)
    subject_input.clear()
    sleep(0.5)
    # 使用JavaScript输入中文，避免乱码
    driver.execute_script("arguments[0].value = '维修';", subject_input)
    # 验证输入
    subject_value = subject_input.get_attribute("value")
    print(f"   主题输入框当前值: {subject_value}")
    
    # 7. 在留言内容文本域输入"手机坏了怎么处理？"
    print("✅ 步骤7: 输入留言内容")
    # 使用CSS选择器定位留言内容文本域
    content_textarea = driver.find_element(By.CSS_SELECTOR, "textarea[name='msg_content']")
    # 滚动到元素可见
    driver.execute_script("arguments[0].scrollIntoView();", content_textarea)
    sleep(0.5)
    content_textarea.clear()
    sleep(0.5)
    # 使用JavaScript输入中文，避免乱码
    driver.execute_script("arguments[0].value = '手机坏了怎么处理？';", content_textarea)
    # 验证输入
    content_value = content_textarea.get_attribute("value")
    print(f"   留言内容当前值: {content_value}")
    
    # 8. 点击我要留言按钮，等待1秒
    print("✅ 步骤8: 点击我要留言按钮")
    # 使用CSS选择器定位提交按钮
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='我要留言']")
    # 滚动到元素可见
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    sleep(0.5)
    submit_button.click()
    sleep(1)
    print(f"   提交后URL: {driver.current_url}")
    
    # 9. 关闭浏览器
    print("✅ 步骤9: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验04完成！")
    print("========================================")
    print("\n实验总结：")
    print("- 使用CSS_SELECTOR定位留言板链接: a[href*='message']")
    print("- 使用CSS_SELECTOR定位邮箱输入框: input[name='user_email']")
    print("- 使用CSS_SELECTOR定位单选按钮: input[type='radio'][name='msg_type'][value='2']")
    print("- 使用CSS_SELECTOR定位主题输入框: input[name='msg_title']")
    print("- 使用CSS_SELECTOR定位留言内容: textarea[name='msg_content']")
    print("- 使用CSS_SELECTOR定位提交按钮: input[type='submit'][value='我要留言']")
    print("- 使用JavaScript输入中文避免乱码")
    print("- 使用is_selected()判断单选按钮状态")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
