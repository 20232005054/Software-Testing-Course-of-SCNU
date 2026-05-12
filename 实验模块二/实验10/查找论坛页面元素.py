# -*- coding: utf-8 -*-
# 辅助脚本 - 查找EC论坛页面的所有链接

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("查找EC论坛页面的所有链接")
print("========================================\n")

# 启动Chrome浏览器
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 打开首页
    print("✅ 打开ECSHOP前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    # 点击注册
    print("✅ 点击注册按钮")
    register_link = driver.find_element(By.PARTIAL_LINK_TEXT, "注册")
    register_link.click()
    sleep(3)
    
    # 点击用户协议
    print("✅ 点击用户协议")
    agreement_link = driver.find_element(By.PARTIAL_LINK_TEXT, "用户协议")
    agreement_link.click()
    sleep(5)
    
    # 切换到新窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    print(f"✅ 已切换到用户协议窗口")
    print(f"   URL: {driver.current_url}")
    
    # 点击配送与支付
    print("\n✅ 点击配送与支付")
    delivery_link = driver.find_element(By.PARTIAL_LINK_TEXT, "配送")
    delivery_link.click()
    sleep(3)
    
    # 点击EC论坛
    print("\n✅ 点击EC论坛")
    forum_link = driver.find_element(By.PARTIAL_LINK_TEXT, "论坛")
    forum_link.click()
    sleep(5)
    
    # 切换到EC论坛窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    print(f"\n✅ 已切换到EC论坛窗口")
    print(f"   URL: {driver.current_url}")
    print(f"   标题: {driver.title}")
    
    print("\n========================================")
    print("查找所有链接：")
    print("========================================\n")
    
    # 查找所有链接
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"页面共有 {len(all_links)} 个链接\n")
    
    for i, link in enumerate(all_links[:100]):  # 只显示前100个
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            
            if text:  # 只显示有文本的链接
                print(f"链接 #{i+1}:")
                print(f"  文本: {text}")
                print(f"  href: {href}")
                print()
        except:
            pass
    
    print("\n========================================")
    print("保存页面源代码和截图")
    print("========================================\n")
    
    # 保存页面源代码
    with open("EC论坛页面源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("✅ 页面源代码已保存到: EC论坛页面源代码.html")
    
    # 截图
    driver.save_screenshot("EC论坛页面截图.png")
    print("✅ 页面截图已保存到: EC论坛页面截图.png")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
