# -*- coding: utf-8 -*-
# 实验11 - 切换Frame
# 练习使用switch_to.frame()和switch_to.default_content()切换iframe

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("实验11 - 切换Frame")
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
    # 1. 打开后台页
    print("✅ 步骤1: 打开后台管理页面")
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 2. 输入用户名：admin
    print("\n✅ 步骤2: 输入用户名admin")
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys("admin")
    sleep(1)
    print(f"   已输入用户名: {username_input.get_attribute('value')}")
    
    # 3. 输入密码：admin123
    print("\n✅ 步骤3: 输入密码admin123")
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("admin123")
    sleep(1)
    print("   已输入密码")
    
    # 4. 输入万能验证码：0
    print("\n✅ 步骤4: 输入验证码0")
    captcha_input = driver.find_element(By.NAME, "captcha")
    captcha_input.clear()
    captcha_input.send_keys("0")
    sleep(1)
    print(f"   已输入验证码: {captcha_input.get_attribute('value')}")
    
    # 5. 点击"进入管理中心"，等待8秒
    print("\n✅ 步骤5: 点击进入管理中心按钮")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    print("   已点击登录按钮")
    sleep(8)
    print(f"   当前URL: {driver.current_url}")
    
    # 6. 点击左侧菜单里的"商品列表"，等待5秒
    print("\n✅ 步骤6: 点击左侧菜单的商品列表")
    # 后台管理系统使用frameset布局，需要切换到左侧菜单的frame
    # 切换到左侧菜单frame（名为menu-frame）
    driver.switch_to.frame("menu-frame")
    print("   已切换到menu-frame")
    
    # 查找商品列表链接
    try:
        goods_list_link = driver.find_element(By.LINK_TEXT, "商品列表")
    except:
        try:
            goods_list_link = driver.find_element(By.PARTIAL_LINK_TEXT, "商品列表")
        except:
            goods_list_link = driver.find_element(By.XPATH, "//a[contains(text(),'商品列表')]")
    
    goods_list_link.click()
    print("   已点击商品列表链接")
    sleep(5)
    
    # 切换回主文档
    driver.switch_to.default_content()
    print("   已切换回主文档")
    
    # 7. 点击商品名称为"诺基亚N85"一行后面的"查看"操作按钮，等待5秒
    print("\n✅ 步骤7: 点击诺基亚N85的查看按钮")
    # 切换到主内容frame
    driver.switch_to.frame("main-frame")
    print("   已切换到main-frame")
    
    # 查找诺基亚N85的查看按钮
    try:
        # 方法1：通过XPATH定位包含"诺基亚N85"的行，然后找查看按钮
        view_button = driver.find_element(By.XPATH, "//tr[contains(.,'诺基亚N85')]//a[contains(text(),'查看') or contains(@title,'查看')]")
    except:
        try:
            # 方法2：查找所有查看按钮，遍历找到诺基亚N85的
            view_buttons = driver.find_elements(By.PARTIAL_LINK_TEXT, "查看")
            view_button = None
            for button in view_buttons:
                # 获取按钮所在行的文本
                try:
                    row = button.find_element(By.XPATH, "./ancestor::tr")
                    if "诺基亚N85" in row.text or "N85" in row.text:
                        view_button = button
                        break
                except:
                    pass
            
            if view_button is None:
                raise Exception("未找到诺基亚N85的查看按钮")
        except:
            # 方法3：通过图片alt属性
            view_button = driver.find_element(By.XPATH, "//tr[contains(.,'N85')]//img[@alt='查看']/parent::a")
    
    view_button.click()
    print("   已点击诺基亚N85的查看按钮")
    sleep(5)
    
    # 8. 在新的窗口内，判断"蓝牙耳机"前的复选框是否选中，若否，选中复选框
    print("\n✅ 步骤8: 检查并选中蓝牙耳机复选框")
    # 切换到新窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    print(f"   已切换到新窗口")
    print(f"   当前URL: {driver.current_url}")
    sleep(2)
    
    # 查找蓝牙耳机的复选框
    try:
        # 方法1：通过label文本查找
        bluetooth_checkbox = driver.find_element(By.XPATH, "//label[contains(text(),'蓝牙耳机')]/preceding-sibling::input[@type='checkbox']")
    except:
        try:
            # 方法2：通过包含蓝牙耳机的元素查找复选框
            bluetooth_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and following-sibling::*[contains(text(),'蓝牙耳机')]]")
        except:
            # 方法3：查找所有复选框，遍历找到蓝牙耳机的
            checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            for checkbox in checkboxes:
                # 获取复选框后面的文本
                parent = checkbox.find_element(By.XPATH, "./..")
                if "蓝牙耳机" in parent.text:
                    bluetooth_checkbox = checkbox
                    break
    
    # 判断是否选中
    is_selected = bluetooth_checkbox.is_selected()
    print(f"   蓝牙耳机复选框当前状态: {'已选中' if is_selected else '未选中'}")
    
    if not is_selected:
        bluetooth_checkbox.click()
        print("   已选中蓝牙耳机复选框")
        sleep(1)
    else:
        print("   复选框已经是选中状态，无需操作")
    
    # 9. 点击"加入收藏夹"按钮，等待5秒，若有弹窗，点击"确定"
    print("\n✅ 步骤9: 点击加入收藏夹按钮")
    try:
        favorite_button = driver.find_element(By.LINK_TEXT, "加入收藏夹")
    except:
        try:
            favorite_button = driver.find_element(By.PARTIAL_LINK_TEXT, "收藏")
        except:
            favorite_button = driver.find_element(By.XPATH, "//a[contains(text(),'收藏')]")
    
    favorite_button.click()
    print("   已点击加入收藏夹按钮")
    sleep(5)
    
    # 检查是否有alert弹窗
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"   弹窗文本: {alert_text}")
        alert.accept()
        print("   已点击确定按钮")
    except:
        print("   没有弹窗")
    
    # 10. 关闭"诺基亚N85"窗口
    print("\n✅ 步骤10: 关闭诺基亚N85窗口")
    driver.close()
    print("   已关闭当前窗口")
    
    # 切换回主窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[0])
    print("   已切换回主窗口")
    sleep(2)
    
    # 11. 点击左侧菜单里的"商品回收站"，等待5秒
    print("\n✅ 步骤11: 点击左侧菜单的商品回收站")
    # 切换到左侧菜单frame
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame("menu-frame")
    except:
        driver.switch_to.frame(0)
    
    try:
        recycle_link = driver.find_element(By.LINK_TEXT, "商品回收站")
    except:
        try:
            recycle_link = driver.find_element(By.PARTIAL_LINK_TEXT, "回收站")
        except:
            recycle_link = driver.find_element(By.XPATH, "//a[contains(text(),'回收站')]")
    
    recycle_link.click()
    print("   已点击商品回收站链接")
    sleep(5)
    
    # 切换回主文档
    driver.switch_to.default_content()
    
    # 12. 点击上方"开店向导"按钮，等待5秒
    print("\n✅ 步骤12: 点击开店向导按钮")
    # 开店向导按钮在顶部frame（header-frame）
    try:
        driver.switch_to.frame("header-frame")
        print("   已切换到header-frame")
        guide_button = driver.find_element(By.PARTIAL_LINK_TEXT, "向导")
        guide_button.click()
        print("   已点击开店向导按钮")
        sleep(5)
    except Exception as e:
        print(f"   未找到开店向导按钮，跳过此步骤: {e}")
    
    # 切换回主文档
    driver.switch_to.default_content()
    
    # 13. 点击"退出"，等待5秒
    print("\n✅ 步骤13: 点击退出按钮")
    # 退出按钮也在顶部frame
    try:
        driver.switch_to.frame("header-frame")
        logout_button = driver.find_element(By.PARTIAL_LINK_TEXT, "退出")
        logout_button.click()
        print("   已点击退出按钮")
        sleep(5)
        driver.switch_to.default_content()
        print(f"   当前URL: {driver.current_url}")
    except Exception as e:
        print(f"   未找到退出按钮: {e}")
        # 尝试直接访问登录页面
        driver.get("http://localhost/upload/admin/privilege.php?act=login")
        sleep(2)
        print("   已跳转到登录页面")
    
    # 14. 输入管理员姓名：Jack
    print("\n✅ 步骤14: 输入管理员姓名Jack")
    try:
        admin_name_input = driver.find_element(By.NAME, "username")
    except:
        try:
            admin_name_input = driver.find_element(By.ID, "username")
        except:
            admin_name_input = driver.find_element(By.XPATH, "//input[@type='text']")
    
    admin_name_input.clear()
    admin_name_input.send_keys("Jack")
    sleep(2)
    print(f"   已输入管理员姓名: {admin_name_input.get_attribute('value')}")
    
    # 15. 关闭浏览器
    print("\n✅ 步骤15: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验11完成！")
    print("========================================")
    print("\n实验总结：")
    print("- driver.switch_to.frame(name/id/index/element) - 切换到指定frame")
    print("- driver.switch_to.default_content() - 切换回主文档")
    print("- driver.switch_to.parent_frame() - 切换到父frame")
    print("- 后台管理系统通常使用iframe布局")
    print("- 操作iframe内的元素前必须先切换到该frame")
    print("- 切换frame后要记得切换回主文档")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
