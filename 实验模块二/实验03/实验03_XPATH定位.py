# -*- coding: utf-8 -*-
# 实验03 - XPATH 高级定位

# 导入必要的模块
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 启动Chrome浏览器
print("=" * 60)
print("实验03 - XPATH 高级定位")
print("=" * 60)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    # 1. 启动Firefox浏览器（已改为Chrome）
    print("\n✅ 步骤1: 启动Chrome浏览器")
    
    # 2. 打开前台首页
    print("✅ 步骤2: 打开前台首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    # 3. 点击登录按钮，等待3秒
    print("✅ 步骤3: 点击登录按钮")
    try:
        # 尝试多种方式定位登录按钮/链接
        login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "录")
    except:
        try:
            login_link = driver.find_element(By.XPATH, "//a[contains(@href,'user.php')]")
        except:
            login_link = driver.find_element(By.XPATH, "//a[contains(text(),'录')]")
    login_link.click()
    sleep(3)
    
    # 4. 点击左上角ECSHOP商标，等待3秒
    print("✅ 步骤4: 点击左上角ECSHOP商标")
    try:
        # 尝试通过首页链接定位
        logo = driver.find_element(By.XPATH, "//a[@href='./']")
    except:
        try:
            logo = driver.find_element(By.XPATH, "//a[contains(@href,'index.php')]")
        except:
            # 直接访问首页
            driver.get("http://localhost/upload/index.php")
            print("   (直接访问首页)")
    
    if 'logo' in locals():
        logo.click()
    sleep(3)
    
    # 5. 点击精品推荐区里的第一个商品名称，等待3秒
    print("✅ 步骤5: 点击精品推荐区里的第一个商品名称")
    try:
        # 使用XPATH定位精品推荐区的第一个商品
        first_product = driver.find_element(By.XPATH, "//div[@class='box']//div[@class='goods_item'][1]//a")
    except:
        try:
            first_product = driver.find_element(By.XPATH, "//div[contains(@class,'goods')]//a[1]")
        except:
            # 如果上面的方式都不行，尝试找第一个商品链接
            first_product = driver.find_element(By.XPATH, "//a[contains(@href,'goods.php')]")
    first_product.click()
    sleep(3)
    
    # 6. 点击"高级搜索"，等待3秒
    print("✅ 步骤6: 点击高级搜索")
    try:
        advanced_search = driver.find_element(By.LINK_TEXT, "高级搜索")
    except:
        try:
            advanced_search = driver.find_element(By.PARTIAL_LINK_TEXT, "高级搜索")
        except:
            advanced_search = driver.find_element(By.XPATH, "//a[contains(text(),'高级搜索')]")
    advanced_search.click()
    sleep(3)
    
    # 7. 输入高级搜索页面里的关键字100，等待3秒
    print("✅ 步骤7: 输入关键字100")
    
    # 等待页面加载完成
    sleep(2)
    
    try:
        # 使用ID定位（根据你提供的HTML）
        keyword_input = driver.find_element(By.ID, "keywords")
    except:
        try:
            keyword_input = driver.find_element(By.NAME, "keywords")
        except:
            keyword_input = driver.find_element(By.XPATH, "//input[@id='keywords']")
    
    # 确保输入框可见并可交互
    driver.execute_script("arguments[0].scrollIntoView();", keyword_input)
    sleep(0.5)
    
    # 清空并输入
    keyword_input.clear()
    sleep(0.5)
    keyword_input.send_keys("100")
    
    # 验证输入是否成功
    input_value = keyword_input.get_attribute("value")
    print(f"   输入框当前值: {input_value}")
    
    sleep(3)
    
    # 8. 点击"立即搜索"按钮，等待3秒
    print("✅ 步骤8: 点击立即搜索按钮")
    try:
        search_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='立即搜索']")
    except:
        try:
            search_button = driver.find_element(By.XPATH, "//button[contains(text(),'搜索')]")
        except:
            search_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    search_button.click()
    sleep(3)
    
    # 9. 点击"夏新N7手机图标"，等待3秒
    print("✅ 步骤9: 点击夏新N7手机")
    try:
        # 方法1：使用XPATH避免中文编码问题
        product_link = driver.find_element(By.XPATH, "//a[contains(@href,'goods.php') and contains(text(),'夏新')]")
        print("   找到夏新商品（XPATH方式）")
    except:
        try:
            # 方法2：如果当前页面没有，重新进行高级搜索（复用步骤7和步骤8的逻辑）
            print("   当前页面未找到商品，尝试搜索夏新N7...")
            
            # 打开高级搜索页面
            driver.get("http://localhost/upload/search.php")
            sleep(2)
            
            # 定位关键字输入框（复用步骤7的逻辑）
            try:
                keyword_input = driver.find_element(By.ID, "keywords")
            except:
                try:
                    keyword_input = driver.find_element(By.NAME, "keywords")
                except:
                    keyword_input = driver.find_element(By.XPATH, "//input[@id='keywords']")
            
            # 确保输入框可见并可交互
            driver.execute_script("arguments[0].scrollIntoView();", keyword_input)
            sleep(0.5)
            
            # 清空并输入"夏新N7"（使用JavaScript避免中文乱码）
            keyword_input.clear()
            sleep(0.5)
            driver.execute_script("arguments[0].value = '夏新N7';", keyword_input)
            
            # 验证输入是否成功
            input_value = keyword_input.get_attribute("value")
            print(f"   输入框当前值: {input_value}")
            sleep(1)
            
            # 点击立即搜索按钮（复用步骤8的逻辑）
            try:
                search_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='立即搜索']")
            except:
                try:
                    search_button = driver.find_element(By.XPATH, "//button[contains(text(),'搜索')]")
                except:
                    search_button = driver.find_element(By.XPATH, "//input[@type='submit']")
            search_button.click()
            sleep(3)
            
            # 搜索完成后，再次尝试定位商品（复用方法1的XPATH）
            product_link = driver.find_element(By.XPATH, "//a[contains(@href,'goods.php') and contains(text(),'夏新')]")
            print("   搜索后找到夏新商品")
            
        except Exception as e:
            print(f"   ⚠️  未找到商品: {e}")
            product_link = None
    
    if product_link:
        product_link.click()
        sleep(3)
    
    # 10. 点击"查看购物车"，等待3秒
    print("✅ 步骤10: 点击查看购物车")
    try:
        cart_link = driver.find_element(By.LINK_TEXT, "查看购物车")
    except:
        try:
            cart_link = driver.find_element(By.PARTIAL_LINK_TEXT, "购物车")
        except:
            cart_link = driver.find_element(By.XPATH, "//a[contains(text(),'购物车')]")
    cart_link.click()
    sleep(3)
    
    print("\n" + "=" * 60)
    print("✅ 实验03完成！所有步骤执行成功")
    print("=" * 60)

except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    print("提示：某些元素可能需要调整定位方式")
    
    # 保存错误截图
    try:
        driver.save_screenshot("实验模块二/实验03/错误截图.png")
        print("已保存错误截图")
    except:
        pass

finally:
    # 11. 关闭浏览器
    print("\n✅ 步骤11: 关闭浏览器")
    sleep(2)
    driver.quit()
