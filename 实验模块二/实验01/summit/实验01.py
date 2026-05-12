# 实验01 - Selenium基础操作

# 1. 从selenium中导入webdriver模块
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 2. 从selenium.webdriver.common.by导入By
from selenium.webdriver.common.by import By

# 3. 从time导入sleep
from time import sleep

# 4. 启动Chrome浏览器（自动下载并管理ChromeDriver）
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 5. 隐式等待3秒
driver.implicitly_wait(3)

# 6. 打开前台首页
driver.get("http://localhost/upload/index.php")

# 7. 在首页的文本框中输入"30"
search_box = driver.find_element(By.NAME, "keywords")
search_box.send_keys("30")

# 8. 点击搜索按钮
search_button = driver.find_element(By.NAME, "imageField")
search_button.click()

# 9. 等待5秒
sleep(5)

# 10. 关闭浏览器
driver.quit()

print("实验01完成！")
