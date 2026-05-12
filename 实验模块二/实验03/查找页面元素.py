# 查找实验03所需的页面元素

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

print("=" * 60)
print("查找实验03所需的页面元素")
print("=" * 60)

# 打开首页
driver.get("http://localhost/upload/index.php")
sleep(2)

# 1. 查找登录按钮
print("\n[1. 登录按钮]")
try:
    login = driver.find_element(By.LINK_TEXT, "登录")
    print(f"✅ By.LINK_TEXT, '登录'")
except:
    print(f"❌ By.LINK_TEXT, '登录'")

# 2. 查找LOGO
print("\n[2. ECSHOP商标/LOGO]")
try:
    logo = driver.find_element(By.XPATH, "//div[@id='logo']//a")
    print(f"✅ By.XPATH, \"//div[@id='logo']//a\"")
except:
    print(f"❌ By.XPATH, \"//div[@id='logo']//a\"")

# 3. 查找精品推荐区的商品
print("\n[3. 精品推荐区商品]")
try:
    products = driver.find_elements(By.XPATH, "//div[@class='box']//a[contains(@href,'goods.php')]")
    print(f"✅ 找到 {len(products)} 个商品链接")
    if products:
        print(f"   第一个商品: {products[0].text}")
except Exception as e:
    print(f"❌ 未找到商品: {e}")

# 4. 查找高级搜索
print("\n[4. 高级搜索链接]")
try:
    adv_search = driver.find_element(By.LINK_TEXT, "高级搜索")
    print(f"✅ By.LINK_TEXT, '高级搜索'")
except:
    try:
        adv_search = driver.find_element(By.PARTIAL_LINK_TEXT, "高级")
        print(f"✅ By.PARTIAL_LINK_TEXT, '高级'")
    except:
        print(f"❌ 未找到高级搜索")

# 点击高级搜索进入页面
try:
    adv_search.click()
    sleep(2)
    
    # 5. 查找关键字输入框
    print("\n[5. 高级搜索页面 - 关键字输入框]")
    try:
        keyword = driver.find_element(By.NAME, "keywords")
        print(f"✅ By.NAME, 'keywords'")
    except:
        print(f"❌ By.NAME, 'keywords'")
    
    # 6. 查找搜索按钮
    print("\n[6. 高级搜索页面 - 搜索按钮]")
    buttons = driver.find_elements(By.XPATH, "//input[@type='submit']")
    print(f"找到 {len(buttons)} 个提交按钮")
    for i, btn in enumerate(buttons):
        print(f"   按钮{i+1}: value='{btn.get_attribute('value')}'")
    
except:
    print("无法进入高级搜索页面")

# 7. 搜索"夏新N7"
print("\n[7. 搜索结果页面]")
driver.get("http://localhost/upload/search.php?keywords=夏新N7")
sleep(2)

try:
    product = driver.find_element(By.PARTIAL_LINK_TEXT, "夏新N7")
    print(f"✅ 找到商品: {product.text}")
except:
    print(f"❌ 未找到夏新N7商品")

# 8. 查找购物车链接
print("\n[8. 购物车链接]")
try:
    cart = driver.find_element(By.LINK_TEXT, "查看购物车")
    print(f"✅ By.LINK_TEXT, '查看购物车'")
except:
    try:
        cart = driver.find_element(By.PARTIAL_LINK_TEXT, "购物车")
        print(f"✅ By.PARTIAL_LINK_TEXT, '购物车'")
    except:
        print(f"❌ 未找到购物车链接")

print("\n" + "=" * 60)
print("元素查找完成！按任意键关闭浏览器...")
print("=" * 60)
input()

driver.quit()
