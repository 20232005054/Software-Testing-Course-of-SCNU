# -*- coding: utf-8 -*-
# 实验12 - 下拉列表操作
# 练习使用Select类操作下拉列表（select元素）

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

print("========================================")
print("实验12 - 下拉列表操作")
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
    # 1. 打开ECShop后台页
    print("✅ 步骤1: 打开ECShop后台管理页面")
    driver.get("http://localhost/upload/admin/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 2. 输入用户名：admin、输入密码：admin123、输入万能验证码：0
    print("\n✅ 步骤2: 输入登录信息")
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys("admin")
    print(f"   已输入用户名: {username_input.get_attribute('value')}")
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("admin123")
    print("   已输入密码")
    
    captcha_input = driver.find_element(By.NAME, "captcha")
    captcha_input.clear()
    captcha_input.send_keys("0")
    print(f"   已输入验证码: {captcha_input.get_attribute('value')}")
    
    # 3. 点击"进入管理中心"，等待8秒
    print("\n✅ 步骤3: 点击进入管理中心")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    print("   已点击登录按钮")
    sleep(8)
    print(f"   当前URL: {driver.current_url}")
    
    # 4. 点击界面上方"个人设置"，等待5秒
    print("\n✅ 步骤4: 点击个人设置")
    # 切换到顶部frame
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame("header-frame")
        print("   已切换到header-frame")
    except:
        try:
            driver.switch_to.frame("top-frame")
            print("   已切换到top-frame")
        except:
            print("   未找到header frame，尝试在主文档中查找")
    
    try:
        personal_settings = driver.find_element(By.LINK_TEXT, "个人设置")
    except:
        try:
            personal_settings = driver.find_element(By.PARTIAL_LINK_TEXT, "个人设置")
        except:
            personal_settings = driver.find_element(By.XPATH, "//a[contains(text(),'个人设置')]")
    
    personal_settings.click()
    print("   已点击个人设置")
    sleep(5)
    
    # 切换到主内容frame
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame("main-frame")
        print("   已切换到main-frame")
    except:
        print("   未找到main-frame，在当前页面操作")
    
    print(f"   当前URL: {driver.current_url}")
    
    # 5. 选中"设置个人导航"右侧下拉列表的从第1个到第6个选项，等待5秒
    print("\n✅ 步骤5: 选中右侧下拉列表的第1-6个选项")
    # 右侧下拉列表是all_menu_list（所有菜单列表）
    right_select_element = driver.find_element(By.ID, "all_menu_list")
    right_select = Select(right_select_element)
    print(f"   找到右侧下拉列表(all_menu_list)，共有 {len(right_select.options)} 个选项")
    
    # 先取消所有选项
    right_select.deselect_all()
    print("   已取消所有选项")
    
    # 选中第1-6个选项（索引0-5）
    for i in range(6):
        try:
            right_select.select_by_index(i)
            option_text = right_select.options[i].text
            print(f"   已选中第{i+1}个选项: {option_text}")
        except Exception as e:
            print(f"   选择第{i+1}个选项失败: {e}")
    
    sleep(5)
    
    # 6. 取消文本是"商品管理"的选项，取消第2个选项，取消value是"comment_manage.php?act=list"的选项，等待5秒
    print("\n✅ 步骤6: 取消特定选项")
    
    # 取消文本是"商品管理"的选项
    try:
        right_select.deselect_by_visible_text("商品管理")
        print("   已取消文本为'商品管理'的选项")
    except Exception as e:
        print(f"   取消'商品管理'选项失败: {e}")
    
    # 取消第2个选项（索引1）
    try:
        option_text = right_select.options[1].text
        right_select.deselect_by_index(1)
        print(f"   已取消第2个选项: {option_text}")
    except Exception as e:
        print(f"   取消第2个选项失败: {e}")
    
    # 取消value是"comment_manage.php?act=list"的选项
    try:
        right_select.deselect_by_value("comment_manage.php?act=list")
        print("   已取消value为'comment_manage.php?act=list'的选项")
    except Exception as e:
        print(f"   取消该value选项失败: {e}")
    
    sleep(5)
    
    # 7. 取消右侧下拉列表所有选项
    print("\n✅ 步骤7: 取消右侧下拉列表所有选项")
    right_select.deselect_all()
    print("   已取消所有选项")
    sleep(1)
    
    # 8. 选择右侧文本是"商品类型"的选项，等待3秒
    print("\n✅ 步骤8: 选择文本为'商品类型'的选项")
    # 注意：ECShop的选项文本前有空格，需要模糊匹配
    selected = False
    for option in right_select.options:
        if "商品类型" in option.text:
            right_select.select_by_visible_text(option.text)
            print(f"   已选中'商品类型'选项（完整文本: '{option.text}'）")
            selected = True
            break
    
    if not selected:
        print("   ⚠️ 未找到'商品类型'选项")
    
    sleep(3)
    
    # 9. 如果"增加"按钮变为可用，点击它，等待5秒
    print("\n✅ 步骤9: 检查并点击增加按钮")
    try:
        # 查找增加按钮
        add_button = None
        try:
            add_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='增加']")
        except:
            try:
                add_button = driver.find_element(By.XPATH, "//button[contains(text(),'增加')]")
            except:
                add_button = driver.find_element(By.XPATH, "//*[contains(text(),'增加') and (@type='button' or @type='submit')]")
        
        if add_button:
            is_enabled = add_button.is_enabled()
            print(f"   增加按钮状态: {'可用' if is_enabled else '不可用'}")
            
            if is_enabled:
                add_button.click()
                print("   已点击增加按钮")
                sleep(5)
            else:
                print("   增加按钮不可用，跳过点击")
    except Exception as e:
        print(f"   未找到增加按钮或操作失败: {e}")
    
    # 10. 选中"设置个人导航"左侧下拉列表的最后一个选项和倒数第二个选项，等待3秒
    print("\n✅ 步骤10: 选中左侧下拉列表的最后两个选项")
    try:
        # 左侧下拉列表是menus_navlist（个人导航列表）
        left_select_element = driver.find_element(By.ID, "menus_navlist")
        left_select = Select(left_select_element)
        print(f"   找到左侧下拉列表(menus_navlist)，共有 {len(left_select.options)} 个选项")
        
        # 获取选项总数
        total_options = len(left_select.options)
        
        if total_options >= 2:
            # 选中最后一个选项
            last_option_text = left_select.options[-1].text
            left_select.select_by_index(total_options - 1)
            print(f"   已选中最后一个选项: {last_option_text}")
            
            # 选中倒数第二个选项
            second_last_option_text = left_select.options[-2].text
            left_select.select_by_index(total_options - 2)
            print(f"   已选中倒数第二个选项: {second_last_option_text}")
        else:
            print(f"   选项数量不足2个，无法选择")
        
        sleep(3)
        
        # 11. 打印左侧下拉列表中所有已被选中的选项的文本
        print("\n✅ 步骤11: 打印左侧下拉列表所有已选中选项")
        selected_options = left_select.all_selected_options
        print(f"   左侧下拉列表共有 {len(selected_options)} 个选中的选项:")
        for idx, option in enumerate(selected_options, 1):
            print(f"   {idx}. {option.text}")
        
        # 12. 打印左侧下拉列表中已被选中的选项中第一个的文本
        print("\n✅ 步骤12: 打印第一个已选中选项的文本")
        if selected_options:
            first_selected = left_select.first_selected_option
            print(f"   第一个已选中的选项: {first_selected.text}")
        else:
            print("   没有选中的选项")
            
    except Exception as e:
        print(f"   操作左侧下拉列表失败: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n========================================")
    print("✅ 实验12完成！")
    print("========================================")
    print("\n实验总结：")
    print("- Select类用于操作下拉列表（<select>元素）")
    print("- select_by_index(index) - 通过索引选择")
    print("- select_by_value(value) - 通过value属性选择")
    print("- select_by_visible_text(text) - 通过可见文本选择")
    print("- deselect_by_index/value/visible_text - 取消选择")
    print("- deselect_all() - 取消所有选择（仅多选列表）")
    print("- all_selected_options - 获取所有已选中的选项")
    print("- first_selected_option - 获取第一个已选中的选项")
    print("- options - 获取所有选项")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    sleep(3)
    driver.quit()
    print("\n✅ 浏览器已关闭")
