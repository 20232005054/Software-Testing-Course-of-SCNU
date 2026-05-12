# -*- coding: utf-8 -*-
# 快速查找个人设置页面的元素

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 登录
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.NAME, "captcha").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    sleep(8)
    
    # 点击个人设置
    driver.switch_to.default_content()
    driver.switch_to.frame("header-frame")
    driver.find_element(By.PARTIAL_LINK_TEXT, "个人设置").click()
    sleep(5)
    
    # 切换到主内容
    driver.switch_to.default_content()
    driver.switch_to.frame("main-frame")
    
    # 打印页面源码（查找select元素）
    page_source = driver.page_source
    
    # 查找所有select元素
    selects = driver.find_elements(By.TAG_NAME, "select")
    print(f"找到 {len(selects)} 个select元素\n")
    
    for idx, sel in enumerate(selects, 1):
        print(f"Select #{idx}:")
        print(f"  name: {sel.get_attribute('name')}")
        print(f"  id: {sel.get_attribute('id')}")
        print(f"  multiple: {sel.get_attribute('multiple')}")
        print(f"  size: {sel.get_attribute('size')}")
        
        # 获取选项
        options = sel.find_elements(By.TAG_NAME, "option")
        print(f"  选项数: {len(options)}")
        for opt_idx, opt in enumerate(options[:5]):  # 只显示前5个
            print(f"    {opt_idx}. {opt.text} (value={opt.get_attribute('value')})")
        print()
    
    # 查找所有input按钮
    buttons = driver.find_elements(By.TAG_NAME, "input")
    print(f"\n找到 {len(buttons)} 个input元素")
    for btn in buttons:
        if btn.get_attribute("type") in ["button", "submit"]:
            print(f"  {btn.get_attribute('type')}: {btn.get_attribute('value')}")
    
    print("\n按Enter继续...")
    input()
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
