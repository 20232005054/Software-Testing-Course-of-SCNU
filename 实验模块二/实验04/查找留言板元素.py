# -*- coding: utf-8 -*-
# 辅助工具：查找留言板页面元素的CSS选择器

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    # 打开首页
    print("正在打开首页...")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    # 点击留言板
    print("\n正在查找留言板链接...")
    try:
        message_board = driver.find_element(By.LINK_TEXT, "留言板")
        print(f"✅ 找到留言板链接")
        message_board.click()
        sleep(3)
    except Exception as e:
        print(f"❌ 未找到留言板链接: {e}")
        # 尝试其他方式
        try:
            message_board = driver.find_element(By.PARTIAL_LINK_TEXT, "留言")
            print(f"✅ 通过部分文本找到留言板链接")
            message_board.click()
            sleep(3)
        except:
            print("❌ 无法找到留言板链接")
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    # 查找表单元素
    print("\n========================================")
    print("查找留言板表单元素")
    print("========================================")
    
    # 查找邮箱输入框
    print("\n[1] 查找邮箱输入框...")
    try:
        email_input = driver.find_element(By.NAME, "email")
        print(f"✅ NAME: email")
        print(f"   ID: {email_input.get_attribute('id')}")
        print(f"   CLASS: {email_input.get_attribute('class')}")
        print(f"   TYPE: {email_input.get_attribute('type')}")
        print(f"   CSS选择器建议: input[name='email']")
        if email_input.get_attribute('id'):
            print(f"   CSS选择器建议: #{email_input.get_attribute('id')}")
    except Exception as e:
        print(f"❌ 未找到邮箱输入框: {e}")
    
    # 查找留言类型单选按钮
    print("\n[2] 查找留言类型单选按钮...")
    try:
        radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
        print(f"✅ 找到 {len(radio_buttons)} 个单选按钮")
        for i, radio in enumerate(radio_buttons):
            print(f"\n   单选按钮 {i+1}:")
            print(f"   NAME: {radio.get_attribute('name')}")
            print(f"   VALUE: {radio.get_attribute('value')}")
            print(f"   ID: {radio.get_attribute('id')}")
            print(f"   CHECKED: {radio.is_selected()}")
            # 查找关联的label
            try:
                parent = radio.find_element(By.XPATH, "..")
                print(f"   父元素文本: {parent.text}")
            except:
                pass
            print(f"   CSS选择器建议: input[type='radio'][value='{radio.get_attribute('value')}']")
    except Exception as e:
        print(f"❌ 未找到单选按钮: {e}")
    
    # 查找主题输入框
    print("\n[3] 查找主题输入框...")
    try:
        subject_input = driver.find_element(By.NAME, "msg_title")
        print(f"✅ NAME: msg_title")
        print(f"   ID: {subject_input.get_attribute('id')}")
        print(f"   CLASS: {subject_input.get_attribute('class')}")
        print(f"   CSS选择器建议: input[name='msg_title']")
        if subject_input.get_attribute('id'):
            print(f"   CSS选择器建议: #{subject_input.get_attribute('id')}")
    except Exception as e:
        print(f"❌ 未找到主题输入框: {e}")
    
    # 查找留言内容文本域
    print("\n[4] 查找留言内容文本域...")
    try:
        content_textarea = driver.find_element(By.NAME, "msg_content")
        print(f"✅ NAME: msg_content")
        print(f"   ID: {content_textarea.get_attribute('id')}")
        print(f"   CLASS: {content_textarea.get_attribute('class')}")
        print(f"   CSS选择器建议: textarea[name='msg_content']")
        if content_textarea.get_attribute('id'):
            print(f"   CSS选择器建议: #{content_textarea.get_attribute('id')}")
    except Exception as e:
        print(f"❌ 未找到留言内容文本域: {e}")
    
    # 查找提交按钮
    print("\n[5] 查找提交按钮...")
    try:
        submit_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='submit'], button[type='submit']")
        print(f"✅ 找到 {len(submit_buttons)} 个提交按钮")
        for i, btn in enumerate(submit_buttons):
            print(f"\n   按钮 {i+1}:")
            print(f"   NAME: {btn.get_attribute('name')}")
            print(f"   VALUE: {btn.get_attribute('value')}")
            print(f"   ID: {btn.get_attribute('id')}")
            print(f"   CLASS: {btn.get_attribute('class')}")
            print(f"   TEXT: {btn.text}")
            if btn.get_attribute('name'):
                print(f"   CSS选择器建议: input[name='{btn.get_attribute('name')}']")
    except Exception as e:
        print(f"❌ 未找到提交按钮: {e}")
    
    print("\n========================================")
    print("按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
