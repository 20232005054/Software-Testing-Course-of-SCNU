"""
Selenium 测试示例
演示基本的浏览器自动化操作
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_baidu_search():
    """测试网页自动化操作"""
    print("=" * 50)
    print("开始测试：网页自动化操作")
    print("=" * 50)
    
    # 自动下载并配置 ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    try:
        # 1. 打开示例网站
        print("\n步骤 1: 打开测试网站...")
        driver.get("https://www.example.com")
        print(f"页面标题: {driver.title}")
        print(f"当前 URL: {driver.current_url}")
        time.sleep(2)
        
        # 2. 获取页面信息
        print("\n步骤 2: 获取页面信息...")
        h1_element = driver.find_element(By.TAG_NAME, "h1")
        print(f"✓ 页面标题文本: {h1_element.text}")
        
        # 3. 查找链接
        print("\n步骤 3: 查找页面链接...")
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"✓ 找到 {len(links)} 个链接")
        if links:
            print(f"  第一个链接文本: {links[0].text}")
            print(f"  第一个链接 URL: {links[0].get_attribute('href')}")
        
        # 4. 获取页面源代码长度
        print("\n步骤 4: 获取页面信息...")
        page_source_length = len(driver.page_source)
        print(f"✓ 页面源代码长度: {page_source_length} 字符")
        
        # 5. 截图
        print("\n步骤 5: 保存页面截图...")
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)
        print(f"✓ 截图已保存到: {screenshot_path}")
        
        print("\n" + "=" * 50)
        print("测试完成！所有步骤执行成功 ✓")
        print("=" * 50)
        
        time.sleep(2)
        
    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
        
    finally:
        print("\n关闭浏览器...")
        driver.quit()


def test_element_locators():
    """测试不同的元素定位方式"""
    print("\n" + "=" * 50)
    print("开始测试：元素定位方式")
    print("=" * 50)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("https://www.baidu.com")
        print(f"\n访问页面: {driver.current_url}")
        
        # 演示不同的定位方式
        print("\n测试不同的定位方式:")
        
        # 1. By ID
        print("1. By.ID 定位搜索框...")
        element = driver.find_element(By.ID, "kw")
        print(f"   ✓ 找到元素: {element.tag_name}")
        
        # 2. By NAME
        print("2. By.NAME 定位搜索框...")
        element = driver.find_element(By.NAME, "wd")
        print(f"   ✓ 找到元素: {element.tag_name}")
        
        # 3. By CLASS_NAME
        print("3. By.CLASS_NAME 定位...")
        elements = driver.find_elements(By.CLASS_NAME, "s_ipt")
        print(f"   ✓ 找到 {len(elements)} 个元素")
        
        # 4. By CSS_SELECTOR
        print("4. By.CSS_SELECTOR 定位...")
        element = driver.find_element(By.CSS_SELECTOR, "#kw")
        print(f"   ✓ 找到元素: {element.tag_name}")
        
        # 5. By XPATH
        print("5. By.XPATH 定位...")
        element = driver.find_element(By.XPATH, "//input[@id='kw']")
        print(f"   ✓ 找到元素: {element.tag_name}")
        
        print("\n" + "=" * 50)
        print("所有定位方式测试成功 ✓")
        print("=" * 50)
        
        time.sleep(2)
        
    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    print("\n🚀 Selenium 自动化测试开始\n")
    
    # 运行测试
    test_baidu_search()
    
    print("\n" + "-" * 50 + "\n")
    
    test_element_locators()
    
    print("\n✅ 所有测试执行完毕！\n")
