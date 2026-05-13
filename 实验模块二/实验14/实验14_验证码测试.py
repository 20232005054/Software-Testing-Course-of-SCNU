# -*- coding: utf-8 -*-
# 实验14 - 验证码测试（OCR识别版本）
# 使用ddddocr进行验证码识别

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os

print("========================================")
print("实验14 - 验证码测试（OCR版本）")
print("========================================\n")

# 检查ddddocr是否安装
try:
    import ddddocr
    print("✅ ddddocr已安装")
    ocr_available = True
except ImportError:
    print("❌ ddddocr未安装")
    print("安装命令: pip install ddddocr")
    print("将使用占位符验证码（会导致提交失败）\n")
    ocr_available = False

# 创建截图保存目录
screenshot_dir = "captcha_screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# 启动Chrome浏览器
print("✅ 启动Chrome浏览器")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 1. 打开P806商品详情页
    print("✅ 步骤1: 打开P806商品详情页")
    driver.get("http://localhost/upload/goods.php?id=24")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 滚动到评论区域
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    print("   已滚动到评论区域")
    
    # 2. 输入E-mail
    print("\n✅ 步骤2: 输入E-mail")
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("a@b.com")
    print(f"   已输入E-mail: {email_input.get_attribute('value')}")
    
    # 3. 输入评论内容
    print("\n✅ 步骤3: 输入评论内容")
    comment_input = driver.find_element(By.NAME, "content")
    driver.execute_script("arguments[0].value = \"It's excellent\";", comment_input)
    print(f"   已输入评论内容: {comment_input.get_attribute('value')}")
    
    # 4. 识别验证码
    print("\n✅ 步骤4: 识别验证码")
    captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")
    
    # 截取验证码图片
    captcha_screenshot = os.path.join(screenshot_dir, "captcha_image.png")
    captcha_img.screenshot(captcha_screenshot)
    print(f"   📸 验证码图片已保存: {captcha_screenshot}")
    
    # 使用OCR识别
    captcha_text = None
    if ocr_available:
        try:
            # show_ad=False 隐藏ddddocr的广告信息
            ocr = ddddocr.DdddOcr(show_ad=False)
            with open(captcha_screenshot, "rb") as f:
                image_bytes = f.read()
            captcha_text = ocr.classification(image_bytes)
            print(f"   ✅ OCR识别结果: {captcha_text}")
        except Exception as e:
            print(f"   ❌ OCR识别失败: {e}")
            captcha_text = "XXXX"
    else:
        captcha_text = "XXXX"
        print(f"   ⚠️ 使用占位符: {captcha_text}")
    
    # 5. 输入验证码
    print("\n✅ 步骤5: 输入验证码")
    captcha_input = driver.find_element(By.NAME, "captcha")
    captcha_input.clear()
    captcha_input.send_keys(captcha_text)
    print(f"   已输入验证码: {captcha_input.get_attribute('value')}")
    
    # 截取填写完成的表单
    screenshot_path = os.path.join(screenshot_dir, "comment_form_filled.png")
    driver.save_screenshot(screenshot_path)
    print(f"   📸 表单填写完成截图: {screenshot_path}")
    
    # 6. 点击提交评论按钮
    print("\n✅ 步骤6: 点击提交评论按钮")
    email_input = driver.find_element(By.NAME, "email")
    form = email_input.find_element(By.XPATH, "./ancestor::form")
    submit_button = form.find_element(By.XPATH, ".//input[@type='submit']")
    
    submit_button.click()
    print("   已点击提交评论按钮")
    sleep(2)
    
    # 检查结果
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"\n   💬 弹窗消息: {alert_text}")
        
        if "成功" in alert_text or "谢谢" in alert_text:
            print("   ✅ 评论提交成功！")
        elif "验证码" in alert_text:
            print("   ❌ 验证码错误")
            if not ocr_available:
                print("   提示：请安装ddddocr进行验证码识别")
        
        alert.accept()
    except:
        print("   没有弹窗，检查页面内容")
        page_text = driver.find_element(By.TAG_NAME, "body").text
        if "成功" in page_text:
            print("   ✅ 评论提交成功！")
    
    # 截取提交后的页面
    screenshot_path = os.path.join(screenshot_dir, "after_submit.png")
    driver.save_screenshot(screenshot_path)
    print(f"   📸 提交后截图: {screenshot_path}")
    
    print("\n========================================")
    print("✅ 实验14完成！")
    print("========================================")
    print("\n实验总结：")
    if ocr_available:
        print("- 使用ddddocr成功识别验证码")
        print("- OCR识别率取决于验证码复杂度")
    else:
        print("- 需要安装ddddocr: pip install ddddocr")
        print("- 或使用其他OCR工具（pytesseract等）")
    print("- 前台评论不支持万能验证码")
    print("- 生产环境建议使用打码平台或人工测试")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(3)
    driver.quit()
    print("\n✅ 浏览器已关闭")
