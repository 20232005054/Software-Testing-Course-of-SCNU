# -*- coding: utf-8 -*-
# 实验13 - 截屏操作
# 练习使用save_screenshot()和element.screenshot()进行全屏和元素截屏

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os

print("========================================")
print("实验13 - 截屏操作")
print("========================================\n")

# 创建截图保存目录
screenshot_dir = "screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
    print(f"✅ 创建截图目录: {screenshot_dir}\n")

# 启动Chrome浏览器
print("✅ 启动Chrome浏览器")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 1. 打开后台登录页
    print("✅ 步骤1: 打开后台登录页")
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 2. 输入管理员姓名admin，输入管理员密码：admin123，输入验证码：0，等待3秒，进行截屏
    print("\n✅ 步骤2: 输入登录信息并截屏")
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys("admin")
    print(f"   已输入用户名: {username_input.get_attribute('value')}")
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("admin123")
    print("   已输入密码")
    
    captcha_input = driver.find_element(By.NAME, "captcha")
    captcha_input.clear()
    captcha_input.send_keys("0")
    print(f"   已输入验证码: {captcha_input.get_attribute('value')}")
    
    sleep(3)
    screenshot_path = os.path.join(screenshot_dir, "01_登录页面.png")
    driver.save_screenshot(screenshot_path)
    print(f"   📸 已截屏保存: {screenshot_path}")
    
    # 3. 点击"进入管理中心"，等待5秒，进行截屏
    print("\n✅ 步骤3: 点击进入管理中心并截屏")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    print("   已点击登录按钮")
    sleep(5)
    
    screenshot_path = os.path.join(screenshot_dir, "02_管理中心首页.png")
    driver.save_screenshot(screenshot_path)
    print(f"   📸 已截屏保存: {screenshot_path}")
    print(f"   当前URL: {driver.current_url}")
    
    # 4. 对左侧菜单栏进行截屏
    print("\n✅ 步骤4: 对左侧菜单栏截屏")
    # 切换到左侧菜单frame
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame("menu-frame")
        print("   已切换到menu-frame")
    except:
        try:
            driver.switch_to.frame(0)
            print("   已切换到第一个frame")
        except:
            print("   未找到菜单frame，在当前页面截屏")
    
    # 截取左侧菜单
    try:
        # 尝试找到菜单容器元素
        menu_element = None
        try:
            menu_element = driver.find_element(By.ID, "menu")
        except:
            try:
                menu_element = driver.find_element(By.CLASS_NAME, "menu")
            except:
                try:
                    menu_element = driver.find_element(By.TAG_NAME, "body")
                except:
                    pass
        
        if menu_element:
            screenshot_path = os.path.join(screenshot_dir, "03_左侧菜单栏.png")
            menu_element.screenshot(screenshot_path)
            print(f"   📸 已截屏保存: {screenshot_path}")
        else:
            # 如果找不到元素，截全屏
            screenshot_path = os.path.join(screenshot_dir, "03_左侧菜单栏.png")
            driver.save_screenshot(screenshot_path)
            print(f"   📸 已截屏保存（全屏）: {screenshot_path}")
    except Exception as e:
        print(f"   元素截屏失败，使用全屏截屏: {e}")
        screenshot_path = os.path.join(screenshot_dir, "03_左侧菜单栏.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存（全屏）: {screenshot_path}")
    
    # 5. 点击"商品列表"，等待3秒，对右侧商品列表区域进行截屏
    print("\n✅ 步骤5: 点击商品列表并对右侧区域截屏")
    try:
        goods_list_link = driver.find_element(By.LINK_TEXT, "商品列表")
    except:
        try:
            goods_list_link = driver.find_element(By.PARTIAL_LINK_TEXT, "商品列表")
        except:
            goods_list_link = driver.find_element(By.XPATH, "//a[contains(text(),'商品列表')]")
    
    goods_list_link.click()
    print("   已点击商品列表")
    sleep(3)
    
    # 切换到主内容frame
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame("main-frame")
        print("   已切换到main-frame")
    except:
        try:
            driver.switch_to.frame(1)
            print("   已切换到第二个frame")
        except:
            print("   未找到主内容frame")
    
    # 截取商品列表区域
    try:
        # 尝试找到商品列表容器
        goods_list_element = None
        try:
            goods_list_element = driver.find_element(By.CLASS_NAME, "list-div")
        except:
            try:
                goods_list_element = driver.find_element(By.ID, "listDiv")
            except:
                try:
                    goods_list_element = driver.find_element(By.TAG_NAME, "form")
                except:
                    goods_list_element = driver.find_element(By.TAG_NAME, "body")
        
        screenshot_path = os.path.join(screenshot_dir, "04_商品列表区域.png")
        goods_list_element.screenshot(screenshot_path)
        print(f"   📸 已截屏保存: {screenshot_path}")
    except Exception as e:
        print(f"   元素截屏失败，使用全屏截屏: {e}")
        screenshot_path = os.path.join(screenshot_dir, "04_商品列表区域.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存（全屏）: {screenshot_path}")
    
    # 6. 点击商品列表中"夏新N7"一行中的查看按钮，等待3秒，切换到新窗口，对新窗口进行截屏
    print("\n✅ 步骤6: 点击夏新N7的查看按钮并截屏")
    try:
        # 查找夏新N7的查看按钮
        view_button = None
        try:
            view_button = driver.find_element(By.XPATH, "//tr[contains(.,'夏新N7')]//a[contains(text(),'查看') or contains(@title,'查看')]")
        except:
            try:
                view_button = driver.find_element(By.XPATH, "//tr[contains(.,'夏新') and contains(.,'N7')]//img[@alt='查看']/parent::a")
            except:
                # 查找所有查看按钮
                view_buttons = driver.find_elements(By.PARTIAL_LINK_TEXT, "查看")
                for button in view_buttons:
                    try:
                        row = button.find_element(By.XPATH, "./ancestor::tr")
                        if "夏新N7" in row.text or "夏新" in row.text and "N7" in row.text:
                            view_button = button
                            break
                    except:
                        pass
        
        if view_button:
            view_button.click()
            print("   已点击夏新N7的查看按钮")
            sleep(3)
            
            # 切换到新窗口
            all_windows = driver.window_handles
            driver.switch_to.window(all_windows[-1])
            print(f"   已切换到新窗口")
            print(f"   当前URL: {driver.current_url}")
            
            screenshot_path = os.path.join(screenshot_dir, "05_夏新N7详情窗口.png")
            driver.save_screenshot(screenshot_path)
            print(f"   📸 已截屏保存: {screenshot_path}")
        else:
            print("   ⚠️ 未找到夏新N7的查看按钮，跳过此步骤")
    except Exception as e:
        print(f"   操作失败: {e}")
    
    # 7. 点击登录按钮，等待3秒，进行截屏
    print("\n✅ 步骤7: 点击登录按钮并截屏")
    try:
        # 在商品详情页查找登录按钮
        # ECShop的登录按钮可能是图片或空文本链接
        login_link = None
        try:
            # 方法1：通过href查找（最可靠）
            login_link = driver.find_element(By.XPATH, "//a[@href='user.php' or contains(@href,'user.php') and not(contains(@href,'register')) and not(contains(@href,'affiliate'))]")
            print("   找到登录链接（通过href）")
        except:
            try:
                # 方法2：通过文本查找
                login_link = driver.find_element(By.LINK_TEXT, "登录")
                print("   找到登录链接（通过文本）")
            except:
                try:
                    # 方法3：通过部分文本查找
                    login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "登录")
                    print("   找到登录链接（通过部分文本）")
                except:
                    # 方法4：查找所有链接，找到user.php的
                    all_links = driver.find_elements(By.TAG_NAME, "a")
                    for link in all_links:
                        href = link.get_attribute("href")
                        if href and "user.php" in href and "register" not in href and "affiliate" not in href:
                            login_link = link
                            print("   找到登录链接（通过遍历）")
                            break
        
        if login_link:
            login_link.click()
            print("   已点击登录按钮")
            sleep(3)
            
            screenshot_path = os.path.join(screenshot_dir, "06_点击登录后.png")
            driver.save_screenshot(screenshot_path)
            print(f"   📸 已截屏保存: {screenshot_path}")
            print(f"   当前URL: {driver.current_url}")
        else:
            print("   ⚠️ 未找到登录按钮，直接访问登录页")
            driver.get("http://localhost/upload/user.php")
            sleep(2)
            screenshot_path = os.path.join(screenshot_dir, "06_点击登录后.png")
            driver.save_screenshot(screenshot_path)
            print(f"   📸 已截屏保存: {screenshot_path}")
    except Exception as e:
        print(f"   查找登录按钮失败: {e}")
        print("   直接访问前台登录页")
        driver.get("http://localhost/upload/user.php")
        sleep(2)
        screenshot_path = os.path.join(screenshot_dir, "06_点击登录后.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存: {screenshot_path}")
    
    # 8. 点击"立即登陆"按钮，等待2秒，进行截屏
    print("\n✅ 步骤8: 点击立即登陆按钮并截屏")
    try:
        # 查找立即登陆按钮
        login_submit = None
        try:
            login_submit = driver.find_element(By.NAME, "submit")
        except:
            try:
                login_submit = driver.find_element(By.XPATH, "//input[@type='submit' and contains(@value,'登')]")
            except:
                try:
                    login_submit = driver.find_element(By.XPATH, "//button[contains(text(),'登')]")
                except:
                    login_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        login_submit.click()
        print("   已点击立即登陆按钮")
        sleep(2)
    except Exception as e:
        print(f"   点击失败: {e}")
    
    # 9. 对消息框进行确认
    print("\n✅ 步骤9: 确认消息框")
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"   消息框文本: {alert_text}")
        alert.accept()
        print("   已确认消息框")
        sleep(1)
        
        # 确认消息框后截屏
        screenshot_path = os.path.join(screenshot_dir, "07_确认消息框后.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存: {screenshot_path}")
    except:
        print("   没有消息框")
        # 如果没有消息框，也截个屏
        screenshot_path = os.path.join(screenshot_dir, "07_点击立即登陆后.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存: {screenshot_path}")
    
    # 10. 输入用户名：vip，输入密码：vip
    print("\n✅ 步骤10: 输入用户名和密码")
    try:
        # 查找用户名输入框
        username_input = None
        try:
            username_input = driver.find_element(By.NAME, "username")
        except:
            try:
                username_input = driver.find_element(By.ID, "username")
            except:
                username_input = driver.find_element(By.XPATH, "//input[@type='text']")
        
        username_input.clear()
        username_input.send_keys("vip")
        print(f"   已输入用户名: {username_input.get_attribute('value')}")
        
        # 查找密码输入框
        password_input = None
        try:
            password_input = driver.find_element(By.NAME, "password")
        except:
            try:
                password_input = driver.find_element(By.ID, "password")
            except:
                password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        
        password_input.clear()
        password_input.send_keys("vip")
        print("   已输入密码")
    except Exception as e:
        print(f"   输入失败: {e}")
    
    # 11. 点击"立即登陆"按钮，等待3秒，进行截屏
    print("\n✅ 步骤11: 再次点击立即登陆并截屏")
    try:
        login_submit = None
        try:
            login_submit = driver.find_element(By.NAME, "submit")
        except:
            try:
                login_submit = driver.find_element(By.XPATH, "//input[@type='submit' and contains(@value,'登')]")
            except:
                login_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        login_submit.click()
        print("   已点击立即登陆按钮")
        sleep(3)
        
        screenshot_path = os.path.join(screenshot_dir, "08_登陆成功后.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存: {screenshot_path}")
        print(f"   当前URL: {driver.current_url}")
    except Exception as e:
        print(f"   操作失败: {e}")
    
    # 12. 自动刷新页面后，对包含ECSHOP图标在内的最上侧区域进行截屏
    print("\n✅ 步骤12: 对顶部区域（包含ECSHOP图标）截屏")
    sleep(2)  # 等待页面刷新
    
    try:
        # 查找顶部区域元素
        header_element = None
        try:
            header_element = driver.find_element(By.CLASS_NAME, "header")
        except:
            try:
                header_element = driver.find_element(By.ID, "header")
            except:
                try:
                    header_element = driver.find_element(By.TAG_NAME, "header")
                except:
                    try:
                        # 查找包含logo的div
                        header_element = driver.find_element(By.XPATH, "//div[contains(@class,'top') or contains(@class,'header')]")
                    except:
                        # 查找logo图片的父容器
                        try:
                            logo = driver.find_element(By.XPATH, "//img[contains(@src,'logo') or contains(@alt,'ECSHOP')]")
                            header_element = logo.find_element(By.XPATH, "./ancestor::div[1]")
                        except:
                            header_element = driver.find_element(By.TAG_NAME, "body")
        
        screenshot_path = os.path.join(screenshot_dir, "09_顶部ECSHOP区域.png")
        header_element.screenshot(screenshot_path)
        print(f"   📸 已截屏保存: {screenshot_path}")
    except Exception as e:
        print(f"   元素截屏失败，使用全屏截屏: {e}")
        screenshot_path = os.path.join(screenshot_dir, "09_顶部ECSHOP区域.png")
        driver.save_screenshot(screenshot_path)
        print(f"   📸 已截屏保存（全屏）: {screenshot_path}")
    
    # 13. 关闭浏览器
    print("\n✅ 步骤13: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验13完成！")
    print("========================================")
    print(f"\n所有截图已保存到: {os.path.abspath(screenshot_dir)}")
    print("\n实验总结：")
    print("- driver.save_screenshot(filename) - 全屏截图")
    print("- element.screenshot(filename) - 元素截图")
    print("- 截图文件格式通常为PNG")
    print("- 元素截图可以精确截取特定区域")
    print("- 全屏截图包含整个浏览器窗口内容")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
