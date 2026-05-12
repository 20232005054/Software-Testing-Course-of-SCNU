# -*- coding: utf-8 -*-
# 辅助脚本 - 查找后台页面的frame结构和商品列表

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("查找后台页面的frame结构")
print("========================================\n")

# 启动Chrome浏览器
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 登录后台
    print("✅ 登录后台")
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("admin")
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123")
    
    captcha_input = driver.find_element(By.NAME, "captcha")
    captcha_input.send_keys("0")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    sleep(8)
    
    print(f"\n当前URL: {driver.current_url}")
    print(f"页面标题: {driver.title}")
    
    # 查找所有iframe
    print("\n========================================")
    print("查找所有iframe：")
    print("========================================\n")
    
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"页面共有 {len(iframes)} 个iframe\n")
    
    for i, iframe in enumerate(iframes):
        name = iframe.get_attribute("name")
        id_attr = iframe.get_attribute("id")
        src = iframe.get_attribute("src")
        print(f"iframe #{i+1}:")
        print(f"  name: {name}")
        print(f"  id: {id_attr}")
        print(f"  src: {src}")
        print()
    
    # 点击商品列表
    print("\n========================================")
    print("点击商品列表：")
    print("========================================\n")
    
    # 尝试切换到不同的frame查找商品列表链接
    for i, iframe in enumerate(iframes):
        try:
            driver.switch_to.default_content()
            driver.switch_to.frame(i)
            print(f"切换到iframe #{i+1}")
            
            # 查找商品列表链接
            try:
                goods_list_link = driver.find_element(By.PARTIAL_LINK_TEXT, "商品列表")
                print(f"  找到商品列表链接！")
                goods_list_link.click()
                print(f"  已点击商品列表链接")
                sleep(5)
                break
            except:
                print(f"  未找到商品列表链接")
        except:
            pass
    
    # 切换回主文档
    driver.switch_to.default_content()
    
    # 查找主内容frame
    print("\n========================================")
    print("查找主内容frame：")
    print("========================================\n")
    
    for i, iframe in enumerate(iframes):
        try:
            driver.switch_to.default_content()
            driver.switch_to.frame(i)
            print(f"切换到iframe #{i+1}")
            
            # 查找商品列表表格
            try:
                table = driver.find_element(By.TAG_NAME, "table")
                print(f"  找到表格！")
                
                # 查找所有行
                rows = driver.find_elements(By.TAG_NAME, "tr")
                print(f"  表格共有 {len(rows)} 行")
                
                # 查找诺基亚N85
                for j, row in enumerate(rows[:20]):  # 只显示前20行
                    try:
                        row_text = row.text
                        if row_text:
                            print(f"\n  行 #{j+1}:")
                            print(f"    {row_text[:100]}")  # 只显示前100个字符
                            
                            if "诺基亚N85" in row_text or "N85" in row_text:
                                print(f"    ✅ 找到诺基亚N85！")
                                # 查找查看按钮
                                links = row.find_elements(By.TAG_NAME, "a")
                                for link in links:
                                    link_text = link.text
                                    href = link.get_attribute("href")
                                    print(f"      链接: {link_text} - {href}")
                    except:
                        pass
                
                break
            except:
                print(f"  未找到表格")
        except:
            pass
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
