# -*- coding: utf-8 -*-
# 辅助工具：查找留言板页面的邮箱字段

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    # 打开首页
    print("正在打开首页...")
    driver.get("http://localhost/upload/index.php")
    sleep(2)
    
    # 点击留言板
    print("正在点击留言板...")
    message_board = driver.find_element(By.LINK_TEXT, "留言板")
    message_board.click()
    sleep(3)
    
    print(f"\n当前URL: {driver.current_url}")
    
    # 查找所有input元素
    print("\n========================================")
    print("查找所有input元素")
    print("========================================")
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"\n找到 {len(inputs)} 个input元素：\n")
    
    for i, inp in enumerate(inputs, 1):
        inp_type = inp.get_attribute('type')
        inp_name = inp.get_attribute('name')
        inp_id = inp.get_attribute('id')
        inp_class = inp.get_attribute('class')
        inp_value = inp.get_attribute('value')
        inp_placeholder = inp.get_attribute('placeholder')
        
        print(f"Input {i}:")
        print(f"  TYPE: {inp_type}")
        print(f"  NAME: {inp_name}")
        print(f"  ID: {inp_id}")
        print(f"  CLASS: {inp_class}")
        print(f"  VALUE: {inp_value}")
        print(f"  PLACEHOLDER: {inp_placeholder}")
        
        # 查找关联的label
        try:
            # 尝试通过父元素找label
            parent = inp.find_element(By.XPATH, "..")
            label_text = parent.text.strip()
            if label_text and len(label_text) < 50:
                print(f"  关联文本: {label_text}")
        except:
            pass
        
        print()
    
    # 查找所有textarea元素
    print("\n========================================")
    print("查找所有textarea元素")
    print("========================================")
    
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    print(f"\n找到 {len(textareas)} 个textarea元素：\n")
    
    for i, ta in enumerate(textareas, 1):
        ta_name = ta.get_attribute('name')
        ta_id = ta.get_attribute('id')
        ta_class = ta.get_attribute('class')
        
        print(f"Textarea {i}:")
        print(f"  NAME: {ta_name}")
        print(f"  ID: {ta_id}")
        print(f"  CLASS: {ta_class}")
        print()
    
    # 保存页面源代码
    print("\n保存页面源代码到文件...")
    with open("d:\\学习资料\\大三下\\软件测试\\实验模块二\\实验04\\留言板页面源代码.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("✅ 已保存到: 留言板页面源代码.html")
    
    print("\n按回车键关闭浏览器...")
    input()
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    driver.quit()
    print("\n✅ 浏览器已关闭")
