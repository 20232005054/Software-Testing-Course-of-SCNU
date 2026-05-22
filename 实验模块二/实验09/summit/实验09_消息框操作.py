# -*- coding: utf-8 -*-
# 实验09 - 消息框操作
# 练习使用switch_to.alert处理JavaScript消息框（alert、confirm）

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("========================================")
print("实验09 - 消息框操作")
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
    
    # 2. 点击"搜索"，等待3秒
    print("\n✅ 步骤2: 点击搜索按钮（不输入关键字）")
    try:
        # 尝试通过name定位搜索按钮
        search_button = driver.find_element(By.NAME, "imageField")
    except:
        try:
            # 尝试通过type定位
            search_button = driver.find_element(By.CSS_SELECTOR, "input[type='image'][src*='search']")
        except:
            # 尝试通过alt属性
            search_button = driver.find_element(By.CSS_SELECTOR, "input[alt='搜索']")
    
    search_button.click()
    print("   已点击搜索按钮")
    sleep(3)
    
    # 3. 切换到消息框
    print("\n✅ 步骤3: 切换到消息框")
    alert = driver.switch_to.alert
    print("   已切换到alert消息框")
    
    # 4. 获得其文本，打印出来
    print("\n✅ 步骤4: 获取消息框文本")
    alert_text = alert.text
    print(f"   消息框文本: {alert_text}")
    
    # 5. 点击"确定"按钮
    print("\n✅ 步骤5: 点击确定按钮")
    alert.accept()
    sleep(1)
    print("   已点击确定按钮，消息框已关闭")
    
    # 6. 在关键字文本框输入P806
    print("\n✅ 步骤6: 在关键字文本框输入P806")
    try:
        # 尝试通过name定位关键字输入框
        keyword_input = driver.find_element(By.NAME, "keywords")
    except:
        # 尝试通过id定位
        keyword_input = driver.find_element(By.ID, "keyword")
    
    keyword_input.clear()
    sleep(0.5)
    keyword_input.send_keys("P806")
    sleep(1)
    print(f"   已输入关键字: {keyword_input.get_attribute('value')}")
    
    # 7. 点击"搜索"，等待3秒
    print("\n✅ 步骤7: 点击搜索按钮")
    try:
        search_button = driver.find_element(By.NAME, "imageField")
    except:
        try:
            search_button = driver.find_element(By.CSS_SELECTOR, "input[type='image'][src*='search']")
        except:
            search_button = driver.find_element(By.CSS_SELECTOR, "input[alt='搜索']")
    
    search_button.click()
    print("   已点击搜索按钮")
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    
    # 8. 点击P806商品名称，等待3秒
    print("\n✅ 步骤8: 点击P806商品名称")
    try:
        # 尝试通过链接文本定位
        product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "P806")
    except:
        try:
            # 尝试通过XPATH定位包含P806的链接
            product_link = driver.find_element(By.XPATH, "//a[contains(text(),'P806')]")
        except:
            # 尝试通过商品链接定位
            product_link = driver.find_element(By.XPATH, "//a[contains(@href,'goods.php') and contains(text(),'P806')]")
    
    product_link.click()
    print("   已点击P806商品链接")
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    
    # 9. 点击"加入购物车"，等待6秒
    print("\n✅ 步骤9: 点击加入购物车按钮")
    try:
        # 尝试通过href中的addToCart定位
        add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(@href,'addToCart')]")
    except:
        try:
            # 尝试通过图片src定位
            add_to_cart_button = driver.find_element(By.XPATH, "//a[.//img[contains(@src,'bnt_cat')]]")
        except:
            # 尝试通过form的action定位并提交
            driver.execute_script("addToCart(24)")
    
    add_to_cart_button.click()
    print("   已点击加入购物车按钮")
    sleep(6)
    print(f"   当前URL: {driver.current_url}")
    
    # 10. 点击"删除"，等待3秒
    print("\n✅ 步骤10: 点击删除按钮")
    # 删除按钮是一个包含confirm的JavaScript链接
    delete_button = driver.find_element(By.LINK_TEXT, "删除")
    delete_button.click()
    print("   已点击删除按钮")
    sleep(3)
    
    # 11. 切换到消息框
    print("\n✅ 步骤11: 切换到消息框")
    alert = driver.switch_to.alert
    print("   已切换到confirm消息框")
    
    # 12. 获得其文本，打印出来
    print("\n✅ 步骤12: 获取消息框文本")
    alert_text = alert.text
    print(f"   消息框文本: {alert_text}")
    
    # 13. 点击"取消"按钮
    print("\n✅ 步骤13: 点击取消按钮")
    alert.dismiss()
    sleep(2)
    print("   已点击取消按钮，消息框已关闭")
    
    # 14. 关闭浏览器
    print("\n✅ 步骤14: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验09完成！")
    print("========================================")
    print("\n实验总结：")
    print("- driver.switch_to.alert - 切换到alert/confirm消息框")
    print("- alert.text - 获取消息框文本内容")
    print("- alert.accept() - 点击确定按钮")
    print("- alert.dismiss() - 点击取消按钮")
    print("- alert消息框：只有确定按钮")
    print("- confirm消息框：有确定和取消按钮")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
