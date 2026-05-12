# -*- coding: utf-8 -*-
# 辅助工具 - 查找下拉列表元素
# 用于查找页面中的所有下拉列表及其选项信息

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

print("========================================")
print("查找下拉列表元素")
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
    # 登录后台
    print("✅ 登录ECShop后台")
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
    print("   登录成功\n")
    
    # 进入个人设置
    print("✅ 进入个人设置页面")
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame("header-frame")
    except:
        driver.switch_to.frame("top-frame")
    
    personal_settings = driver.find_element(By.PARTIAL_LINK_TEXT, "个人设置")
    personal_settings.click()
    sleep(5)
    
    # 切换到主内容frame
    driver.switch_to.default_content()
    driver.switch_to.frame("main-frame")
    print("   已进入个人设置页面\n")
    
    # 查找所有下拉列表
    print("=" * 60)
    print("查找页面中的所有下拉列表")
    print("=" * 60)
    
    select_elements = driver.find_elements(By.TAG_NAME, "select")
    print(f"\n找到 {len(select_elements)} 个下拉列表\n")
    
    for idx, select_element in enumerate(select_elements, 1):
        print(f"\n{'=' * 60}")
        print(f"下拉列表 #{idx}")
        print(f"{'=' * 60}")
        
        # 获取基本属性
        name = select_element.get_attribute("name") or "无"
        id_attr = select_element.get_attribute("id") or "无"
        multiple = select_element.get_attribute("multiple")
        size = select_element.get_attribute("size") or "1"
        
        print(f"Name属性: {name}")
        print(f"ID属性: {id_attr}")
        print(f"类型: {'多选列表' if multiple else '单选列表'}")
        print(f"Size: {size}")
        
        # 创建Select对象
        select = Select(select_element)
        
        # 获取所有选项
        options = select.options
        print(f"选项数量: {len(options)}")
        
        # 打印所有选项
        print(f"\n所有选项：")
        for opt_idx, option in enumerate(options):
            text = option.text.strip()
            value = option.get_attribute("value")
            selected = "✓" if option.is_selected() else " "
            print(f"  [{selected}] {opt_idx}. {text}")
            print(f"      value: {value}")
        
        # 如果有已选中的选项
        selected_options = select.all_selected_options
        if selected_options:
            print(f"\n已选中的选项：")
            for option in selected_options:
                print(f"  - {option.text.strip()}")
        
        # 打印定位方式
        print(f"\n推荐定位方式：")
        if name != "无":
            print(f"  By.NAME: '{name}'")
        if id_attr != "无":
            print(f"  By.ID: '{id_attr}'")
        print(f"  By.XPATH: '//select[@name=\"{name}\"]'")
        
        # 打印示例代码
        print(f"\n示例代码：")
        print(f"  select_element = driver.find_element(By.NAME, '{name}')")
        print(f"  select = Select(select_element)")
        print(f"  select.select_by_index(0)  # 选择第1个选项")
        print(f"  select.select_by_visible_text('{options[0].text.strip()}')  # 选择第1个选项")
        if multiple:
            print(f"  select.deselect_all()  # 取消所有选择")
    
    print(f"\n{'=' * 60}")
    print("查找完成！")
    print(f"{'=' * 60}\n")
    
    # 查找增加按钮
    print("\n查找增加按钮：")
    try:
        add_buttons = driver.find_elements(By.XPATH, "//*[contains(text(),'增加') or @value='增加']")
        print(f"找到 {len(add_buttons)} 个包含'增加'的元素")
        for idx, button in enumerate(add_buttons, 1):
            tag = button.tag_name
            text = button.text or button.get_attribute("value")
            enabled = "可用" if button.is_enabled() else "不可用"
            print(f"  {idx}. <{tag}> {text} - {enabled}")
    except Exception as e:
        print(f"  未找到增加按钮: {e}")
    
    print("\n按Enter键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
