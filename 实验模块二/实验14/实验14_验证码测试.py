# -*- coding: utf-8 -*-
# 实验14 - 验证码测试
# 练习处理验证码：使用万能验证码、截图保存、OCR识别等方法

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os

print("========================================")
print("实验14 - 验证码测试")
print("========================================\n")

# 创建截图保存目录
screenshot_dir = "captcha_screenshots"
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
    # 1. 打开ECShop前台P806商品详情页
    print("✅ 步骤1: 打开P806商品详情页")
    driver.get("http://localhost/upload/goods.php?id=24")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 滚动到评论区域
    try:
        # 查找评论表单
        comment_form = driver.find_element(By.XPATH, "//form[contains(@action,'comment')]")
        driver.execute_script("arguments[0].scrollIntoView();", comment_form)
        sleep(1)
        print("   已滚动到评论区域")
    except:
        # 如果找不到表单，尝试滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        print("   已滚动到页面底部")
    
    # 2. 输入E-mail：a@b.com
    print("\n✅ 步骤2: 输入E-mail")
    try:
        email_input = None
        try:
            email_input = driver.find_element(By.NAME, "email")
        except:
            try:
                email_input = driver.find_element(By.ID, "email")
            except:
                email_input = driver.find_element(By.XPATH, "//input[@type='text' and contains(@name,'email')]")
        
        email_input.clear()
        email_input.send_keys("a@b.com")
        print(f"   已输入E-mail: {email_input.get_attribute('value')}")
    except Exception as e:
        print(f"   输入E-mail失败: {e}")
    
    # 3. 输入评论内容：It's excellent
    print("\n✅ 步骤3: 输入评论内容")
    try:
        comment_input = None
        try:
            comment_input = driver.find_element(By.NAME, "content")
        except:
            try:
                comment_input = driver.find_element(By.ID, "content")
            except:
                try:
                    comment_input = driver.find_element(By.TAG_NAME, "textarea")
                except:
                    comment_input = driver.find_element(By.XPATH, "//textarea[contains(@name,'content') or contains(@name,'comment')]")
        
        comment_input.clear()
        # 使用JavaScript输入，避免中文乱码
        driver.execute_script("arguments[0].value = \"It's excellent\";", comment_input)
        print(f"   已输入评论内容: {comment_input.get_attribute('value')}")
    except Exception as e:
        print(f"   输入评论内容失败: {e}")
    
    # 4. 识别验证码图片上的内容
    print("\n✅ 步骤4: 识别验证码")
    
    # 查找验证码图片
    try:
        captcha_img = None
        try:
            captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha') or contains(@onclick,'captcha')]")
        except:
            try:
                captcha_img = driver.find_element(By.ID, "captcha_img")
            except:
                captcha_img = driver.find_element(By.XPATH, "//img[contains(@alt,'验证码') or contains(@title,'验证码')]")
        
        if captcha_img:
            # 截取验证码图片
            captcha_screenshot = os.path.join(screenshot_dir, "captcha_image.png")
            captcha_img.screenshot(captcha_screenshot)
            print(f"   📸 验证码图片已保存: {captcha_screenshot}")
            
            # 获取验证码图片的src
            captcha_src = captcha_img.get_attribute("src")
            print(f"   验证码图片URL: {captcha_src}")
            
            # ECShop有万能验证码"0"
            print("\n   💡 ECShop验证码说明：")
            print("   - ECShop系统支持万能验证码：0")
            print("   - 在实际测试中，可以直接使用'0'作为验证码")
            print("   - 生产环境中需要使用OCR识别或人工输入")
    except Exception as e:
        print(f"   查找验证码图片失败: {e}")
    
    # 5. 输入正确的验证码
    print("\n✅ 步骤5: 输入验证码")
    try:
        captcha_input = None
        try:
            captcha_input = driver.find_element(By.NAME, "captcha")
        except:
            try:
                captcha_input = driver.find_element(By.ID, "captcha")
            except:
                captcha_input = driver.find_element(By.XPATH, "//input[@type='text' and (contains(@name,'captcha') or contains(@name,'verify'))]")
        
        # 使用万能验证码
        captcha_value = "0"
        captcha_input.clear()
        captcha_input.send_keys(captcha_value)
        print(f"   已输入验证码: {captcha_input.get_attribute('value')}")
        print(f"   使用万能验证码: {captcha_value}")
    except Exception as e:
        print(f"   输入验证码失败: {e}")
    
    # 截取填写完成的表单
    screenshot_path = os.path.join(screenshot_dir, "comment_form_filled.png")
    driver.save_screenshot(screenshot_path)
    print(f"   📸 表单填写完成截图: {screenshot_path}")
    
    # 6. 点击"提交评论"按钮
    print("\n✅ 步骤6: 点击提交评论按钮")
    try:
        submit_button = None
        
        # ECShop的评论提交按钮特点：name和value都为空
        # 需要通过位置关系查找
        try:
            # 方法1：在email输入框的父表单中查找提交按钮
            email_input = driver.find_element(By.NAME, "email")
            form = email_input.find_element(By.XPATH, "./ancestor::form")
            submit_button = form.find_element(By.XPATH, ".//input[@type='submit']")
            print("   找到提交按钮（通过表单查找）")
        except:
            try:
                # 方法2：在验证码输入框附近查找
                captcha_input = driver.find_element(By.NAME, "captcha")
                parent_table = captcha_input.find_element(By.XPATH, "./ancestor::table")
                submit_button = parent_table.find_element(By.XPATH, ".//input[@type='submit']")
                print("   找到提交按钮（通过验证码附近查找）")
            except:
                try:
                    # 方法3：查找所有提交按钮，选择最后一个（通常是评论按钮）
                    submit_buttons = driver.find_elements(By.XPATH, "//input[@type='submit']")
                    if submit_buttons:
                        submit_button = submit_buttons[-1]  # 选择最后一个
                        print(f"   找到提交按钮（共{len(submit_buttons)}个，选择最后一个）")
                except:
                    pass
        
        if submit_button:
            # 滚动到按钮位置
            driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            sleep(0.5)
            
            submit_button.click()
            print("   已点击提交评论按钮")
            sleep(2)
            
            # 检查是否有alert弹窗
            try:
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"\n   💬 弹窗消息: {alert_text}")
                
                # 判断是否是评论相关的弹窗
                if "评论" in alert_text or "成功" in alert_text or "谢谢" in alert_text:
                    print("   ✅ 评论提交成功！")
                elif "搜索" in alert_text or "关键词" in alert_text:
                    print("   ⚠️ 出现了搜索表单的弹窗（可能点击了错误的按钮）")
                else:
                    print("   ⚠️ 出现了其他弹窗")
                
                alert.accept()
                print("   已确认弹窗")
                sleep(1)
            except:
                print("   没有弹窗")
            
            # 截取提交后的页面
            screenshot_path = os.path.join(screenshot_dir, "after_submit.png")
            driver.save_screenshot(screenshot_path)
            print(f"   📸 提交后截图: {screenshot_path}")
            
            # 检查页面是否有成功或错误消息
            try:
                page_text = driver.find_element(By.TAG_NAME, "body").text
                if "成功" in page_text or "谢谢" in page_text:
                    print("   ✅ 页面显示成功消息")
                elif "失败" in page_text or "错误" in page_text:
                    print("   ❌ 页面显示错误消息")
                
                print(f"   当前URL: {driver.current_url}")
            except:
                pass
        else:
            print("   ❌ 未找到提交按钮")
        
    except Exception as e:
        print(f"   提交过程出现异常: {e}")
        # 截图保存错误现场
        try:
            screenshot_path = os.path.join(screenshot_dir, "error_screenshot.png")
            driver.save_screenshot(screenshot_path)
            print(f"   📸 错误截图: {screenshot_path}")
        except:
            pass
    
    print("\n========================================")
    print("✅ 实验14完成！")
    print("========================================")
    print("\n实验总结：")
    print("- 验证码是防止自动化攻击的重要手段")
    print("- ECShop支持万能验证码'0'用于测试")
    print("- 可以使用element.screenshot()截取验证码图片")
    print("- 生产环境需要使用OCR识别或人工输入")
    print("- 常用OCR库：pytesseract, ddddocr等")
    print(f"\n所有截图已保存到: {os.path.abspath(screenshot_dir)}")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(3)
    driver.quit()
    print("\n✅ 浏览器已关闭")
