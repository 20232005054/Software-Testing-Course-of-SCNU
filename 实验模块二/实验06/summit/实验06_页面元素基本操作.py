# -*- coding: utf-8 -*-
# 实验06 - 页面元素基本操作
# 练习元素状态判断、属性获取、值修改等操作

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import re

print("========================================")
print("实验06 - 页面元素基本操作")
print("========================================\n")

# 启动Chrome浏览器
print("✅ 启动Chrome浏览器")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
    # 如果网络问题，使用本地ChromeDriver
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

try:
    # 1. 打开首页
    print("✅ 步骤1: 打开首页")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    print(f"   当前URL: {driver.current_url}")
    
    # 2. 输入关键字100，判断"搜索"按钮如果可用，点击搜索按钮，等待3秒
    print("\n✅ 步骤2: 输入关键字100并搜索")
    keyword_input = driver.find_element(By.NAME, "keywords")
    keyword_input.clear()
    keyword_input.send_keys("100")
    print("   已输入关键字: 100")
    
    # 判断搜索按钮是否可用
    search_button = driver.find_element(By.NAME, "imageField")
    if search_button.is_enabled():
        print("   搜索按钮可用，点击搜索")
        search_button.click()
        sleep(3)
    else:
        print("   ⚠️  搜索按钮不可用")
    
    print(f"   搜索后URL: {driver.current_url}")
    
    # 3. 点击搜索结果区域里的"金立 A30"的商品名称，等待3秒
    print("\n✅ 步骤3: 点击金立A30商品")
    try:
        product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "金立")
        print(f"   找到商品: {product_link.text}")
        product_link.click()
        sleep(3)
        print(f"   商品页URL: {driver.current_url}")
    except Exception as e:
        print(f"   ❌ 未找到金立商品: {e}")
        raise
    
    # 4. 打印默认"购买数量"文本框的当前默认值
    print("\n✅ 步骤4: 获取购买数量默认值")
    number_input = driver.find_element(By.NAME, "number")
    default_number = number_input.get_attribute("value")
    print(f"   购买数量默认值: {default_number}")
    
    # 5. 获得"商品库存"的台数
    print("\n✅ 步骤5: 获取商品库存")
    try:
        # 从页面源代码中查找库存信息
        page_source = driver.page_source
        # 查找"商品库存"后面的数字
        stock_match = re.search(r'商品库存[：:]\s*(\d+)', page_source)
        if stock_match:
            stock_number = int(stock_match.group(1))
            print(f"   库存台数: {stock_number}台")
        else:
            # 尝试其他方式
            stock_element = driver.find_element(By.XPATH, "//*[contains(text(),'商品库存')]")
            # 获取父元素的文本
            parent = stock_element.find_element(By.XPATH, "..")
            parent_text = parent.text
            print(f"   库存区域文本: {parent_text}")
            # 从文本中提取数字
            numbers = re.findall(r'\d+', parent_text)
            if numbers:
                stock_number = int(numbers[0])
                print(f"   库存台数: {stock_number}台")
            else:
                print("   ⚠️  无法提取库存数字，默认设为10")
                stock_number = 10
    except Exception as e:
        print(f"   ❌ 获取库存失败: {e}，默认设为10")
        stock_number = 10
    
    # 6. 如果台数大于3台，清空"购买数量"文本框，输入3
    print("\n✅ 步骤6: 判断库存并修改购买数量")
    if stock_number > 3:
        print(f"   库存({stock_number}台) > 3台，修改购买数量为3")
        number_input.clear()
        sleep(0.5)
        number_input.send_keys("3")
        # 验证输入
        new_value = number_input.get_attribute("value")
        print(f"   购买数量已修改为: {new_value}")
    else:
        print(f"   库存({stock_number}台) <= 3台，不修改购买数量")
    
    # 7. 判断"数据线"复选框，如果没有被选中，就点击选中它
    print("\n✅ 步骤7: 判断并选中数据线复选框")
    try:
        # 通过ID定位数据线复选框
        data_cable_checkbox = driver.find_element(By.ID, "spec_value_190")
        if data_cable_checkbox.is_selected():
            print("   数据线复选框已选中")
        else:
            print("   数据线复选框未选中，正在选中...")
            # 滚动到元素可见
            driver.execute_script("arguments[0].scrollIntoView();", data_cable_checkbox)
            sleep(0.5)
            data_cable_checkbox.click()
            sleep(1)
            # 验证是否选中
            if data_cable_checkbox.is_selected():
                print("   ✓ 数据线复选框已成功选中")
            else:
                print("   ⚠️  数据线复选框选中失败")
    except Exception as e:
        print(f"   ❌ 操作数据线复选框失败: {e}")
    
    # 8. 判断"线控耳机"复选框，如果没有被选中，就点击选中它
    print("\n✅ 步骤8: 判断并选中线控耳机复选框")
    try:
        # 通过ID定位线控耳机复选框
        earphone_checkbox = driver.find_element(By.ID, "spec_value_189")
        if earphone_checkbox.is_selected():
            print("   线控耳机复选框已选中")
        else:
            print("   线控耳机复选框未选中，正在选中...")
            # 滚动到元素可见
            driver.execute_script("arguments[0].scrollIntoView();", earphone_checkbox)
            sleep(0.5)
            earphone_checkbox.click()
            sleep(1)
            # 验证是否选中
            if earphone_checkbox.is_selected():
                print("   ✓ 线控耳机复选框已成功选中")
            else:
                print("   ⚠️  线控耳机复选框选中失败")
    except Exception as e:
        print(f"   ❌ 操作线控耳机复选框失败: {e}")
    
    # 9. 获得此时的"商品总价"，如果是"￥6210元"，打印"总价计算正确"，否则打印"总价计算错误"
    print("\n✅ 步骤9: 验证商品总价")
    try:
        # 等待价格更新
        sleep(2)
        # 通过ID定位商品总价
        total_price_element = driver.find_element(By.ID, "ECS_GOODS_AMOUNT")
        total_price_text = total_price_element.text
        print(f"   商品总价: {total_price_text}")
        
        # 判断总价是否正确
        # 金立A30: 2000元 * 3 = 6000元
        # 数据线: 20元
        # 线控耳机: 50元
        # 总计: 6000 + 20 + 50 = 6070元
        if "6210" in total_price_text:
            print("   ✓ 总价计算正确")
        else:
            print(f"   ⚠️  总价计算错误（预期: ￥6210元，实际: {total_price_text}）")
            # 打印详细信息
            print(f"   说明: 金立A30(2000元×3) + 数据线(20元) + 线控耳机(50元) = 6070元")
    except Exception as e:
        print(f"   ❌ 获取总价失败: {e}")
    
    print("\n========================================")
    print("✅ 实验06完成！")
    print("========================================")
    print("\n实验总结：")
    print("- 元素状态判断: is_enabled(), is_selected()")
    print("- 属性获取: get_attribute('value')")
    print("- 文本提取: element.text")
    print("- 复选框操作: click(), is_selected()")
    print("- 正则表达式提取数字: re.search()")
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    print("\n按回车键关闭浏览器...")
    input()
    driver.quit()
    print("✅ 浏览器已关闭")
