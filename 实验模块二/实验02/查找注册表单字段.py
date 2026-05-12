# 查找注册表单所有字段的脚本

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

# 打开注册页
driver.get("http://localhost/upload/user.php?act=register")
sleep(2)

print("=" * 60)
print("查找注册表单所有输入字段")
print("=" * 60)

# 查找所有 input 元素
inputs = driver.find_elements(By.TAG_NAME, "input")

print(f"\n找到 {len(inputs)} 个 input 元素：\n")

for i, inp in enumerate(inputs, 1):
    input_type = inp.get_attribute("type")
    input_name = inp.get_attribute("name")
    input_id = inp.get_attribute("id")
    input_value = inp.get_attribute("value")
    
    if input_name:  # 只显示有 name 属性的
        print(f"{i}. Type: {input_type:10} | Name: {input_name:20} | ID: {input_id}")

# 查找所有 select 元素
print("\n" + "=" * 60)
print("查找所有下拉选择框")
print("=" * 60)

selects = driver.find_elements(By.TAG_NAME, "select")
print(f"\n找到 {len(selects)} 个 select 元素：\n")

for i, sel in enumerate(selects, 1):
    select_name = sel.get_attribute("name")
    select_id = sel.get_attribute("id")
    print(f"{i}. Name: {select_name:20} | ID: {select_id}")

print("\n按任意键关闭浏览器...")
input()

driver.quit()
