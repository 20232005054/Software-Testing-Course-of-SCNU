# -*- coding: utf-8 -*-
# 实验07 - 模拟键盘操作
# 练习使用Keys类模拟键盘按键操作

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

print("========================================")
print("实验07 - 模拟键盘操作")
print("========================================\n")

# 1. 启动Chrome浏览器
print("✅ 步骤1: 启动Chrome浏览器")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 2. 登录前台首页
    print("✅ 步骤2: 打开前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 3. 点击"留言板"
    print("\n✅ 步骤3: 点击留言板")
    message_board = driver.find_element(By.LINK_TEXT, "留言板")
    message_board.click()
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 4. 定位电子邮件地址文本框
    print("\n✅ 步骤4: 定位电子邮件地址文本框")
    email_input = driver.find_element(By.NAME, "user_email")
    # 滚动到元素可见
    driver.execute_script("arguments[0].scrollIntoView();", email_input)
    sleep(0.5)
    print("   已定位到邮箱输入框")
    
    # 5. 输入电子邮件地址：vip@ecshop.com
    print("\n✅ 步骤5: 输入电子邮件地址")
    email_input.clear()
    email_input.send_keys("vip@ecshop.com")
    sleep(1)
    print(f"   已输入: {email_input.get_attribute('value')}")
    
    # 6. 按下Home键光标回到行首
    print("\n✅ 步骤6: 按下Home键回到行首")
    email_input.send_keys(Keys.HOME)
    sleep(1)
    print("   已按下Home键")
    
    # 7. Shift+右箭头（→）连续点击三次，选中三个字符vip
    print("\n✅ 步骤7: Shift+右箭头选中'vip'")
    email_input.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
    email_input.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
    email_input.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
    sleep(1)
    print("   已选中前3个字符")
    
    # 8. Ctrl+c复制，到主题文本框里Ctrl+v粘贴
    print("\n✅ 步骤8: 复制并粘贴到主题文本框")
    # 复制
    email_input.send_keys(Keys.CONTROL + 'c')
    sleep(0.5)
    print("   已复制选中内容")
    
    # 定位主题文本框
    subject_input = driver.find_element(By.NAME, "msg_title")
    driver.execute_script("arguments[0].scrollIntoView();", subject_input)
    sleep(0.5)
    subject_input.clear()
    # 粘贴
    subject_input.send_keys(Keys.CONTROL + 'v')
    sleep(1)
    subject_value = subject_input.get_attribute('value')
    print(f"   主题文本框内容: {subject_value}")
    
    # 9. 到留言内容里输入"我是"、Ctrl+v粘贴，Enter回车换行
    print("\n✅ 步骤9: 在留言内容中输入并粘贴")
    content_textarea = driver.find_element(By.NAME, "msg_content")
    driver.execute_script("arguments[0].scrollIntoView();", content_textarea)
    sleep(0.5)
    content_textarea.clear()
    # 使用JavaScript输入中文
    driver.execute_script("arguments[0].value = '我是';", content_textarea)
    sleep(0.5)
    # 粘贴
    content_textarea.send_keys(Keys.CONTROL + 'v')
    sleep(0.5)
    # 回车换行
    content_textarea.send_keys(Keys.ENTER)
    sleep(1)
    content_value = content_textarea.get_attribute('value')
    print(f"   留言内容: {content_value}")
    
    # 10. 再输入"请问有优惠码？"
    print("\n✅ 步骤10: 继续输入内容")
    # 使用JavaScript追加中文内容
    current_value = content_textarea.get_attribute('value')
    new_value = current_value + "请问有优惠码？"
    driver.execute_script("arguments[0].value = arguments[1];", content_textarea, new_value)
    sleep(1)
    final_value = content_textarea.get_attribute('value')
    print(f"   最终留言内容: {final_value}")
    
    # 11. 在主题文本框里按下回车
    print("\n✅ 步骤11: 在主题文本框按下回车")
    subject_input.send_keys(Keys.ENTER)
    sleep(2)
    print("   已按下回车键")
    print(f"   当前URL: {driver.current_url}")
    
    print("\n========================================")
    print("✅ 实验07完成！")
    print("========================================")
    print("\n实验总结：")
    print("- 使用Keys类模拟键盘按键")
    print("- Keys.HOME - 回到行首")
    print("- Keys.SHIFT + Keys.ARROW_RIGHT - 选中文本")
    print("- Keys.CONTROL + 'c' - 复制")
    print("- Keys.CONTROL + 'v' - 粘贴")
    print("- Keys.ENTER - 回车")
    print("- 中文输入使用JavaScript避免乱码")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    print("\n等待3秒后自动关闭浏览器...")
    sleep(3)
    driver.quit()
    print("✅ 浏览器已关闭")
