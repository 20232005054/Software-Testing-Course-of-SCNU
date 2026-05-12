# -*- coding: utf-8 -*-
# 实验08 - 模拟鼠标和键盘操作
# 练习使用ActionChains类模拟鼠标操作和键盘操作

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

print("========================================")
print("实验08 - 模拟鼠标和键盘操作")
print("========================================\n")

# 启动Chrome浏览器
print("✅ 启动Chrome浏览器")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 1. 打开ECSHOP前台首页
    print("✅ 步骤1: 打开ECSHOP前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 2. 定位到登录按钮，然后单击
    print("\n✅ 步骤2: 定位并单击登录按钮")
    try:
        login_link = driver.find_element(By.LINK_TEXT, "登录")
    except:
        try:
            # 尝试使用部分文本
            login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "登")
        except:
            # 尝试使用href
            login_link = driver.find_element(By.CSS_SELECTOR, "a[href*='user.php']")
    
    # 使用ActionChains模拟鼠标单击
    actions = ActionChains(driver)
    actions.click(login_link).perform()
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 3. 鼠标移动到用户名文本框元素，然后单击
    print("\n✅ 步骤3: 鼠标移动到用户名文本框并单击")
    username_input = driver.find_element(By.NAME, "username")
    # 使用ActionChains模拟鼠标移动和单击
    actions = ActionChains(driver)
    actions.move_to_element(username_input).click().perform()
    sleep(1)
    print("   已移动到用户名文本框并单击")
    
    # 4. 在文本框里输入"vip"
    print("\n✅ 步骤4: 输入用户名")
    username_input.send_keys("vip")
    sleep(1)
    print(f"   已输入: {username_input.get_attribute('value')}")
    
    # 5. 按下键盘的Tab键
    print("\n✅ 步骤5: 按下Tab键")
    username_input.send_keys(Keys.TAB)
    sleep(1)
    print("   已按下Tab键，焦点移到密码框")
    
    # 6. 等待2秒
    print("\n✅ 步骤6: 等待2秒")
    sleep(2)
    print("   等待完成")
    
    # 7. 在密码文本框里输入"vip"
    print("\n✅ 步骤7: 输入密码")
    # 获取当前焦点元素（应该是密码框）
    password_input = driver.switch_to.active_element
    password_input.send_keys("vip")
    sleep(1)
    print("   已输入密码")
    
    # 8. 按下键盘的Tab键
    print("\n✅ 步骤8: 按下Tab键")
    password_input.send_keys(Keys.TAB)
    sleep(1)
    print("   已按下Tab键，焦点移到登录按钮")
    
    # 9. 等待2秒
    print("\n✅ 步骤9: 等待2秒")
    sleep(2)
    print("   等待完成")
    
    # 10. 此时当前焦点位于"立即登陆"这个元素，在这个焦点位置按下回车
    print("\n✅ 步骤10: 在当前焦点位置按下回车")
    # 获取当前焦点元素
    current_element = driver.switch_to.active_element
    current_element.send_keys(Keys.ENTER)
    sleep(2)
    print("   已按下回车键")
    print(f"   登录后URL: {driver.current_url}")
    
    # 11. 等待5秒
    print("\n✅ 步骤11: 等待5秒")
    sleep(5)
    print("   等待完成")
    
    # 12. 关闭浏览器
    print("\n✅ 步骤12: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验08完成！")
    print("========================================")
    print("\n实验总结：")
    print("- ActionChains类模拟鼠标操作")
    print("- actions.move_to_element() - 移动到元素")
    print("- actions.click() - 单击")
    print("- actions.perform() - 执行动作")
    print("- Keys.TAB - Tab键切换焦点")
    print("- driver.switch_to.active_element - 获取当前焦点元素")
    print("- 焦点元素可以直接接收键盘输入")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
