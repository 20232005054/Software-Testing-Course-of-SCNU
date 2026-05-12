# -*- coding: utf-8 -*-
# 辅助工具 - 查找商品详情页的登录按钮

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 登录后台
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.NAME, "captcha").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    sleep(8)
    
    # 进入商品列表
    driver.switch_to.default_content()
    driver.switch_to.frame("menu-frame")
    driver.find_element(By.PARTIAL_LINK_TEXT, "商品列表").click()
    sleep(3)
    
    # 点击夏新N7查看
    driver.switch_to.default_content()
    driver.switch_to.frame("main-frame")
    
    view_button = driver.find_element(By.XPATH, "//tr[contains(.,'夏新N7')]//a[contains(text(),'查看')]")
    view_button.click()
    sleep(3)
    
    # 切换到新窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    
    print(f"当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    print("\n" + "="*60)
    
    # 查找所有链接
    print("\n所有链接（<a>标签）：")
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"共找到 {len(links)} 个链接\n")
    
    for idx, link in enumerate(links[:30], 1):  # 只显示前30个
        text = link.text.strip()
        href = link.get_attribute("href")
        if text or href:
            print(f"{idx}. 文本: '{text}' | href: {href}")
    
    # 查找包含"登录"的元素
    print("\n" + "="*60)
    print("\n查找包含'登录'的元素：")
    
    try:
        login_elements = driver.find_elements(By.XPATH, "//*[contains(text(),'登录') or contains(@href,'user.php')]")
        print(f"找到 {len(login_elements)} 个相关元素\n")
        for idx, elem in enumerate(login_elements, 1):
            print(f"{idx}. 标签: {elem.tag_name}")
            print(f"   文本: {elem.text}")
            print(f"   href: {elem.get_attribute('href')}")
            print(f"   class: {elem.get_attribute('class')}")
            print()
    except Exception as e:
        print(f"查找失败: {e}")
    
    # 查找顶部导航区域
    print("="*60)
    print("\n查找顶部导航区域：")
    
    try:
        # 尝试多种方式查找顶部区域
        top_elements = []
        
        try:
            top_elements = driver.find_elements(By.CLASS_NAME, "topNav")
        except:
            pass
        
        if not top_elements:
            try:
                top_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'top')]")
            except:
                pass
        
        if not top_elements:
            try:
                top_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'nav')]")
            except:
                pass
        
        print(f"找到 {len(top_elements)} 个顶部区域元素")
        
        for idx, elem in enumerate(top_elements, 1):
            print(f"\n顶部区域 #{idx}:")
            print(f"  class: {elem.get_attribute('class')}")
            print(f"  文本内容: {elem.text[:200]}")  # 只显示前200字符
            
            # 在这个区域内查找链接
            links_in_top = elem.find_elements(By.TAG_NAME, "a")
            print(f"  包含 {len(links_in_top)} 个链接")
            for link in links_in_top[:10]:
                print(f"    - {link.text} | {link.get_attribute('href')}")
    except Exception as e:
        print(f"查找失败: {e}")
    
    print("\n按Enter继续...")
    input()
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
