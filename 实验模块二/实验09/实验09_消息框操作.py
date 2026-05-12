# -*- coding: utf-8 -*-
# 实验09 - 消息框操作
# 练习处理JavaScript的alert和confirm对话框

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
    # 立即处理可能出现的初始alert（不等待页面完全加载）
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        initial_alert = driver.switch_to.alert
        alert_text = initial_alert.text
        print(f"   检测到初始提示: {alert_text}")
        initial_alert.accept()
        print("   已关闭初始提示")
        sleep(2)
    except:
        print("   未检测到初始提示")
    
    print(f"   当前URL: {driver.current_url}")
    
    # 2. 点击"搜索"，等待3秒
    print("\n✅ 步骤2: 点击搜索按钮")
    search_button = driver.find_element(By.NAME, "imageField")
    search_button.click()
    sleep(3)
    print("   已点击搜索按钮")
    
    # 3. 切换到消息框
    print("\n✅ 步骤3: 切换到消息框")
    try:
        # 等待alert出现
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("   已切换到消息框")
        
        # 4. 获得其文本，打印出来
        print("\n✅ 步骤4: 获取消息框文本")
        alert_text = alert.text
        print(f"   消息框文本: {alert_text}")
        
        # 5. 点击"确定"按钮
        print("\n✅ 步骤5: 点击确定按钮")
        alert.accept()
        sleep(1)
        print("   已点击确定")
    except Exception as e:
        print(f"   ⚠️  未出现消息框或处理失败: {e}")
    
    # 6. 在关键字文本框输入8806
    print("\n✅ 步骤6: 输入关键字")
    # 首页的搜索框ID是keyword
    keyword_input = driver.find_element(By.ID, "keyword")
    keyword_input.clear()
    keyword_input.send_keys("806")
    sleep(1)
    print(f"   已输入: {keyword_input.get_attribute('value')}")
    
    # 7. 点击"搜索"，等待3秒
    print("\n✅ 步骤7: 点击搜索按钮")
    search_button = driver.find_element(By.NAME, "imageField")
    search_button.click()
    sleep(3)
    print(f"   搜索后URL: {driver.current_url}")
    
    # 8. 点击P806商品名称，等待3秒
    print("\n✅ 步骤8: 点击商品")
    try:
        # 查找任何商品链接
        products = driver.find_elements(By.CSS_SELECTOR, "a[href*='goods.php?id=']")
        if products:
            product_link = products[0]
            product_name = product_link.text
            print(f"   找到商品: {product_name}")
            product_link.click()
            sleep(3)
            print(f"   商品页URL: {driver.current_url}")
        else:
            print("   ❌ 未找到商品")
            raise Exception("未找到商品")
    except Exception as e:
        print(f"   ⚠️  点击商品失败: {e}")
    
    # 9. 点击"加入购物车"，等待6秒
    print("\n✅ 步骤9: 点击加入购物车")
    try:
        # 查找加入购物车链接（通过href包含addToCart）
        add_to_cart = driver.find_element(By.CSS_SELECTOR, "a[href*='addToCart']")
        driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
        sleep(1)
        add_to_cart.click()
        sleep(6)
        print("   已点击加入购物车")
        print(f"   当前URL: {driver.current_url}")
    except Exception as e:
        print(f"   ⚠️  加入购物车失败: {e}")
        # 尝试通过图片定位
        try:
            add_to_cart_img = driver.find_element(By.CSS_SELECTOR, "img[src*='bnt_cat']")
            parent_link = add_to_cart_img.find_element(By.XPATH, "..")
            parent_link.click()
            sleep(6)
            print("   已通过图片点击加入购物车")
        except:
            print("   ❌ 无法找到加入购物车按钮")
    
    # 10. 点击"删除"，等待3秒
    print("\n✅ 步骤10: 点击删除按钮")
    try:
        # 查找删除链接
        delete_link = driver.find_element(By.PARTIAL_LINK_TEXT, "删除")
        delete_link.click()
        sleep(3)
        print("   已点击删除")
    except Exception as e:
        print(f"   ⚠️  未找到删除按钮: {e}")
    
    # 11. 切换到消息框
    print("\n✅ 步骤11: 切换到消息框")
    try:
        # 等待confirm对话框出现
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        confirm_box = driver.switch_to.alert
        print("   已切换到消息框")
        
        # 12. 获得其文本，打印出来
        print("\n✅ 步骤12: 获取消息框文本")
        confirm_text = confirm_box.text
        print(f"   消息框文本: {confirm_text}")
        
        # 13. 点击"取消"按钮
        print("\n✅ 步骤13: 点击取消按钮")
        confirm_box.dismiss()
        sleep(2)
        print("   已点击取消")
    except Exception as e:
        print(f"   ⚠️  未出现消息框或处理失败: {e}")
    
    # 14. 关闭浏览器
    print("\n✅ 步骤14: 关闭浏览器")
    
    print("\n========================================")
    print("✅ 实验09完成！")
    print("========================================")
    print("\n实验总结：")
    print("- driver.switch_to.alert - 切换到alert/confirm对话框")
    print("- alert.text - 获取对话框文本")
    print("- alert.accept() - 点击确定")
    print("- alert.dismiss() - 点击取消")
    print("- WebDriverWait等待alert出现")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(2)
    driver.quit()
    print("\n✅ 浏览器已关闭")
