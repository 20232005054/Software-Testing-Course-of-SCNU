# -*- coding: utf-8 -*-
# 实验05 - 浏览器基本操作
# 练习浏览器窗口控制和导航操作

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("实验05 - 浏览器基本操作")
print("========================================\n")

# 启动Chrome浏览器
print("✅ 启动Chrome浏览器")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    # 1. 打开留言板页，等待3秒
    print("✅ 步骤1: 打开留言板页")
    driver.get("http://localhost/upload/message.php")
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    
    # 2. 把浏览器窗口大小设置为宽度800px和高度600px，等待3秒
    print("\n✅ 步骤2: 设置浏览器窗口大小为800x600")
    driver.set_window_size(800, 600)
    sleep(3)
    size = driver.get_window_size()
    print(f"   窗口大小: 宽度={size['width']}px, 高度={size['height']}px")
    
    # 3. 打印窗口左上角位置坐标
    print("\n✅ 步骤3: 打印窗口左上角位置坐标")
    position = driver.get_window_position()
    print(f"   窗口位置: x={position['x']}px, y={position['y']}px")
    
    # 4. 把浏览器窗口最小化，等待3秒，打印窗口大小尺寸
    print("\n✅ 步骤4: 最小化浏览器窗口")
    driver.minimize_window()
    sleep(3)
    size = driver.get_window_size()
    print(f"   最小化后窗口大小: 宽度={size['width']}px, 高度={size['height']}px")
    
    # 5. 自定义浏览器窗口位置，把窗口左上角坐标设置为（60px,60px），等待3秒，打印自定义后窗口左上角位置坐标
    print("\n✅ 步骤5: 设置窗口位置为(60, 60)")
    driver.set_window_position(60, 60)
    sleep(3)
    position = driver.get_window_position()
    print(f"   设置后窗口位置: x={position['x']}px, y={position['y']}px")
    
    # 6. 把浏览器窗口最大化，等待3秒，打印窗口大小尺寸
    print("\n✅ 步骤6: 最大化浏览器窗口")
    driver.maximize_window()
    sleep(3)
    size = driver.get_window_size()
    print(f"   最大化后窗口大小: 宽度={size['width']}px, 高度={size['height']}px")
    
    # 7. 点击"高级搜索"，等待3秒
    print("\n✅ 步骤7: 点击高级搜索")
    try:
        # 使用链接文本定位
        advanced_search = driver.find_element(By.LINK_TEXT, "高级搜索")
        advanced_search.click()
        sleep(3)
        print(f"   跳转后URL: {driver.current_url}")
    except Exception as e:
        print(f"   ⚠️  未找到高级搜索链接: {e}")
        # 尝试其他方式
        try:
            advanced_search = driver.find_element(By.PARTIAL_LINK_TEXT, "高级")
            advanced_search.click()
            sleep(3)
            print(f"   跳转后URL: {driver.current_url}")
        except:
            print("   ⚠️  无法找到高级搜索链接，跳过此步骤")
    
    # 8. 后退，等待3秒
    print("\n✅ 步骤8: 后退")
    driver.back()
    sleep(3)
    print(f"   后退后URL: {driver.current_url}")
    
    # 9. 获取当前网页的标题和URL，并打印
    print("\n✅ 步骤9: 获取当前网页标题和URL")
    current_title = driver.title
    current_url = driver.current_url
    print(f"   页面标题: {current_title}")
    print(f"   页面URL: {current_url}")
    
    # 10. 前进，等待3秒
    print("\n✅ 步骤10: 前进")
    driver.forward()
    sleep(3)
    print(f"   前进后URL: {driver.current_url}")
    
    # 11. 在地址栏输入获取的URL网址进行访问，等待3秒
    print("\n✅ 步骤11: 访问之前获取的URL")
    print(f"   访问URL: {current_url}")
    driver.get(current_url)
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    
    # 12. 后退，等待3秒
    print("\n✅ 步骤12: 后退")
    driver.back()
    sleep(3)
    print(f"   后退后URL: {driver.current_url}")
    
    # 13. 关闭浏览器
    print("\n✅ 步骤13: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验05完成！")
    print("========================================")
    print("\n实验总结：")
    print("- 窗口大小控制: set_window_size(), get_window_size()")
    print("- 窗口位置控制: set_window_position(), get_window_position()")
    print("- 窗口状态控制: minimize_window(), maximize_window()")
    print("- 浏览器导航: back(), forward(), get()")
    print("- 页面信息获取: title, current_url")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
