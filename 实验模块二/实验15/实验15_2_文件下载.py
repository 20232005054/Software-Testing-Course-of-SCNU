# -*- coding: utf-8 -*-
# 实验15-2：文件下载测试
# 测试从网页下载文件到指定目录

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os

# 配置Chrome下载选项
chrome_options = webdriver.ChromeOptions()

# 设置下载目录为 c:\temp
download_dir = r"c:\temp"

# 创建下载目录（如果不存在）
os.makedirs(download_dir, exist_ok=True)

# 配置Chrome下载参数
prefs = {
    "download.default_directory": download_dir,  # 设置默认下载目录
    "download.prompt_for_download": False,        # 禁用下载提示
    "download.directory_upgrade": True,           # 允许目录升级
    "safebrowsing.enabled": True                  # 启用安全浏览
}
chrome_options.add_experimental_option("prefs", prefs)

# 启动Chrome浏览器
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
driver.implicitly_wait(3)
driver.maximize_window()

try:
    print("=" * 60)
    print("实验15-2：文件下载测试")
    print("=" * 60)
    
    # 步骤1：打开网页http://sahitest.com/demo/saveAs.htm
    print("\n✅ 步骤1: 打开测试网页")
    driver.get("http://sahitest.com/demo/saveAs.htm")
    sleep(3)
    print(f"   当前URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")
    print(f"   下载目录: {download_dir}")
    
    # 步骤2：下载testsaveas.zip文件至c:\temp文件夹下
    print("\n✅ 步骤2: 点击下载链接")
    
    # 查找下载链接
    try:
        # 尝试通过链接文本查找
        download_link = driver.find_element(By.LINK_TEXT, "testsaveas.zip")
        print(f"   找到下载链接: testsaveas.zip")
    except:
        try:
            # 尝试通过部分链接文本查找
            download_link = driver.find_element(By.PARTIAL_LINK_TEXT, "testsaveas")
            print(f"   找到下载链接（部分匹配）")
        except:
            # 尝试通过href属性查找
            download_link = driver.find_element(By.XPATH, "//a[contains(@href,'testsaveas.zip')]")
            print(f"   找到下载链接（XPATH匹配）")
    
    # 获取下载链接地址
    download_url = download_link.get_attribute("href")
    print(f"   下载地址: {download_url}")
    
    # 点击下载链接
    download_link.click()
    print(f"   ✅ 已点击下载链接")
    
    # 等待文件下载完成
    print("\n✅ 步骤3: 等待文件下载")
    print("   ⏳ 等待下载完成（最多30秒）...")
    
    # 检查文件是否下载完成
    download_file = os.path.join(download_dir, "testsaveas.zip")
    max_wait_time = 30  # 最多等待30秒
    wait_interval = 1   # 每秒检查一次
    
    for i in range(max_wait_time):
        if os.path.exists(download_file):
            print(f"   ✅ 文件下载完成！")
            print(f"   文件路径: {download_file}")
            
            # 获取文件大小
            file_size = os.path.getsize(download_file)
            print(f"   文件大小: {file_size} 字节")
            break
        else:
            sleep(wait_interval)
            if (i + 1) % 5 == 0:  # 每5秒打印一次进度
                print(f"   ⏳ 已等待 {i + 1} 秒...")
    else:
        print(f"   ⚠️  警告: 等待超时，文件可能未下载完成")
        print(f"   请检查目录: {download_dir}")
    
    # 验证下载结果
    print("\n✅ 步骤4: 验证下载结果")
    if os.path.exists(download_file):
        file_size = os.path.getsize(download_file)
        print(f"   ✅ 文件存在: {download_file}")
        print(f"   文件大小: {file_size} 字节")
        
        # 检查文件是否为空
        if file_size > 0:
            print(f"   ✅ 文件下载成功！")
        else:
            print(f"   ⚠️  警告: 文件大小为0，可能下载失败")
    else:
        print(f"   ❌ 文件不存在: {download_file}")
        print(f"   请检查下载目录: {download_dir}")
        
        # 列出下载目录中的所有文件
        print(f"\n   下载目录中的文件:")
        try:
            files = os.listdir(download_dir)
            if files:
                for file in files:
                    print(f"   - {file}")
            else:
                print(f"   （目录为空）")
        except Exception as e:
            print(f"   无法列出文件: {e}")
    
    # 保存截图
    screenshot_path = "实验模块二/实验15/文件下载结果.png"
    driver.save_screenshot(screenshot_path)
    print(f"\n📸 截图已保存: {screenshot_path}")
    
    print("\n" + "=" * 60)
    print("✅ 实验15-2：文件下载测试完成！")
    print("=" * 60)
    
    # 等待查看结果
    print("\n⏳ 等待5秒后关闭浏览器...")
    sleep(5)
    
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    
    # 保存错误截图
    try:
        driver.save_screenshot("实验模块二/实验15/错误截图_下载.png")
        print("📸 错误截图已保存")
    except:
        pass
    
finally:
    driver.quit()
    print("\n🔚 浏览器已关闭")
