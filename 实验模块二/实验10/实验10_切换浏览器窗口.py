# -*- coding: utf-8 -*-
# 实验10 - 切换浏览器窗口
# 练习使用window_handles和switch_to.window()切换浏览器窗口

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("实验10 - 切换浏览器窗口")
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
    print(f"   当前窗口数量: {len(driver.window_handles)}")
    
    # 2. 点击注册按钮，等待5秒
    print("\n✅ 步骤2: 点击注册按钮")
    # 注册按钮是一个图片链接
    register_link = driver.find_element(By.XPATH, "//a[contains(@href,'user.php?act=register')]")
    register_link.click()
    print("   已点击注册按钮")
    sleep(5)
    print(f"   当前URL: {driver.current_url}")
    
    # 3. 点击"用户协议"，等待8秒
    print("\n✅ 步骤3: 点击用户协议链接")
    try:
        # 尝试通过链接文本定位
        agreement_link = driver.find_element(By.LINK_TEXT, "用户协议")
    except:
        try:
            # 尝试通过部分链接文本
            agreement_link = driver.find_element(By.PARTIAL_LINK_TEXT, "用户协议")
        except:
            # 尝试通过XPATH
            agreement_link = driver.find_element(By.XPATH, "//a[contains(text(),'用户协议') or contains(text(),'协议')]")
    
    agreement_link.click()
    print("   已点击用户协议链接")
    sleep(8)
    print(f"   当前窗口数量: {len(driver.window_handles)}")
    
    # 4. 获得当前窗口句柄，保存在变量里
    print("\n✅ 步骤4: 获取当前窗口句柄")
    original_window = driver.current_window_handle
    print(f"   原始窗口句柄: {original_window}")
    print(f"   所有窗口句柄: {driver.window_handles}")
    
    # 5. 切换到最新窗口
    print("\n✅ 步骤5: 切换到最新窗口")
    # 获取所有窗口句柄
    all_windows = driver.window_handles
    # 切换到最新的窗口（最后一个）
    driver.switch_to.window(all_windows[-1])
    print(f"   已切换到窗口: {driver.current_window_handle}")
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 6. 在新窗口里点击配送与支付按钮，等待5秒
    print("\n✅ 步骤6: 在新窗口里点击配送与支付链接")
    try:
        # 尝试通过链接文本定位
        delivery_link = driver.find_element(By.LINK_TEXT, "配送与支付")
    except:
        try:
            # 尝试通过部分链接文本
            delivery_link = driver.find_element(By.PARTIAL_LINK_TEXT, "配送")
        except:
            # 尝试通过XPATH
            delivery_link = driver.find_element(By.XPATH, "//a[contains(text(),'配送')]")
    
    delivery_link.click()
    print("   已点击配送与支付链接")
    sleep(5)
    print(f"   当前URL: {driver.current_url}")
    print(f"   当前窗口数量: {len(driver.window_handles)}")
    
    # 7. 点击"EC论坛"，等待5秒，切换到新窗口
    print("\n✅ 步骤7: 点击EC论坛链接")
    try:
        # 尝试通过链接文本定位
        forum_link = driver.find_element(By.LINK_TEXT, "EC论坛")
    except:
        try:
            # 尝试通过部分链接文本
            forum_link = driver.find_element(By.PARTIAL_LINK_TEXT, "论坛")
        except:
            # 尝试通过href
            forum_link = driver.find_element(By.XPATH, "//a[contains(@href,'bbs.ecshop.com')]")
    
    forum_link.click()
    print("   已点击EC论坛链接")
    sleep(5)
    
    # 切换到新窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    print(f"   已切换到新窗口")
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    print(f"   当前窗口数量: {len(driver.window_handles)}")
    
    # 8. 点击"商派官网"（替代"商业授权"），等待5秒，切换到新窗口
    # 注意：EC论坛是外部网站，没有"商业授权"链接，使用"商派官网"替代
    print("\n✅ 步骤8: 点击商派官网链接（替代商业授权）")
    try:
        # 尝试通过链接文本定位商派官网
        shopex_link = driver.find_element(By.LINK_TEXT, "商派官网")
    except:
        try:
            # 尝试通过部分链接文本
            shopex_link = driver.find_element(By.PARTIAL_LINK_TEXT, "商派")
        except:
            # 尝试通过href
            shopex_link = driver.find_element(By.XPATH, "//a[contains(@href,'shopex.cn')]")
    
    shopex_link.click()
    print("   已点击商派官网链接")
    sleep(5)
    
    # 切换到新窗口
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    print(f"   已切换到新窗口")
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    print(f"   当前窗口数量: {len(driver.window_handles)}")
    print("   注意：使用'商派官网'替代'商业授权'链接")
    
    # 9. 关闭"EC论坛"窗口
    print("\n✅ 步骤9: 关闭EC论坛窗口")
    # 获取所有窗口句柄
    all_windows = driver.window_handles
    print(f"   关闭前窗口数量: {len(all_windows)}")
    
    # 遍历所有窗口，找到EC论坛窗口并关闭
    # EC论坛的URL是 www.ecshop.com，商派官网是 www.shopex.cn
    for window in all_windows:
        driver.switch_to.window(window)
        current_url = driver.current_url
        current_title = driver.title
        # 只关闭 ecshop.com 的窗口，不关闭 shopex.cn
        if "ecshop.com" in current_url and window != original_window:
            print(f"   找到EC论坛窗口: {current_title}")
            print(f"   URL: {current_url}")
            driver.close()
            print("   已关闭EC论坛窗口")
            break
    
    sleep(2)
    print(f"   关闭后窗口数量: {len(driver.window_handles)}")
    
    # 10. 用前面变量里保存的句柄切换回原窗口
    print("\n✅ 步骤10: 切换回原始窗口")
    driver.switch_to.window(original_window)
    print(f"   已切换回原始窗口: {original_window}")
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 11. 输入用户名"Jack"，等待3秒
    print("\n✅ 步骤11: 输入用户名Jack")
    try:
        # 尝试通过name定位用户名输入框
        username_input = driver.find_element(By.NAME, "username")
    except:
        try:
            # 尝试通过id定位
            username_input = driver.find_element(By.ID, "username")
        except:
            # 尝试通过XPATH
            username_input = driver.find_element(By.XPATH, "//input[@type='text' and contains(@name,'user')]")
    
    username_input.clear()
    sleep(0.5)
    username_input.send_keys("Jack")
    sleep(3)
    print(f"   已输入用户名: {username_input.get_attribute('value')}")
    
    # 12. 关闭浏览器
    print("\n✅ 步骤12: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验10完成！")
    print("========================================")
    print("\n实验总结：")
    print("- driver.current_window_handle - 获取当前窗口句柄")
    print("- driver.window_handles - 获取所有窗口句柄列表")
    print("- driver.switch_to.window(handle) - 切换到指定窗口")
    print("- driver.close() - 关闭当前窗口")
    print("- 保存原始窗口句柄可以方便地切换回去")
    print("- 新窗口通常是window_handles列表的最后一个")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
