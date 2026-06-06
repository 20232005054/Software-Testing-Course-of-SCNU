# -*- coding: utf-8 -*-
# 功能：ECShop网站自动化测试 —— 覆盖浏览器前进后退、窗口大小操作、
#        文本框数据处理、按钮/复选框状态获取与选中、模拟鼠标操作、
#        模拟键盘操作、消息框处理、切换窗口与Frame、元素截屏、验证码获取
# 时间：2026年6月
# 作者：（请填写姓名）
# 学号：（请填写学号）
# 版本：v1.0
# 测试环境：Windows + Python 3.x + Selenium + Chrome + ChromeDriver + ECShop V2.7.1

import os
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# ── 全局配置 ─────────────────────────────────────────────
BASE_URL = "http://localhost/upload/"
ADMIN_URL = "http://localhost/upload/admin/"
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def ss(driver, filename):
    """快捷截图函数"""
    path = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(path)
    print(f"   截图已保存: {path}")


print("=" * 60)
print("ECShop网站自动化测试 —— 软件测试大作业")
print("=" * 60)

# 启动Chrome浏览器
print("\n✅ 启动Chrome浏览器")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except Exception:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)

try:
    # ══════════════════════════════════════════════════════
    # 阶段一：窗口大小操作（技术点1）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段一：窗口大小操作")
    print("=" * 40)

    # 步骤1：打开ECShop前台首页并最大化窗口
    driver.get(BASE_URL + "index.php")
    sleep(2)
    driver.maximize_window()
    size = driver.get_window_size()
    pos = driver.get_window_position()
    print(f"最大化后窗口大小: {size['width']} x {size['height']}")
    print(f"窗口左上角坐标: x={pos['x']}, y={pos['y']}")

    # 步骤2：设置窗口为800x600
    driver.set_window_size(800, 600)
    sleep(1)
    size = driver.get_window_size()
    print(f"设置800x600后窗口大小: {size['width']} x {size['height']}")

    # 步骤3：自定义窗口位置为(60, 60)
    driver.set_window_position(60, 60)
    sleep(1)
    pos = driver.get_window_position()
    print(f"自定义位置后窗口坐标: x={pos['x']}, y={pos['y']}")

    # 步骤4：恢复最大化
    driver.maximize_window()
    sleep(1)
    print("已恢复最大化窗口")

    # ══════════════════════════════════════════════════════
    # 阶段二：获取文本框数据 + 模拟键盘操作（技术点2、3）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段二：获取文本框数据 + 模拟键盘操作")
    print("=" * 40)

    # 步骤5：获取搜索框默认值 —— 技术点2：获取文本框数据
    search_box = driver.find_element(By.NAME, "keywords")
    default_value = search_box.get_attribute("value")
    print(f"搜索框默认值: '{default_value}'（读取文本框数据）")

    # 步骤6：在搜索框输入内容，模拟键盘Ctrl+A全选、Ctrl+C复制、Ctrl+V粘贴 —— 技术点3：模拟键盘操作
    search_box.clear()
    search_box.send_keys("100测试")
    sleep(0.5)
    # Ctrl+A 全选
    search_box.send_keys(Keys.CONTROL + 'a')
    sleep(0.5)
    print("键盘操作: Ctrl+A 全选搜索框内容")
    # Ctrl+C 复制
    search_box.send_keys(Keys.CONTROL + 'c')
    sleep(0.5)
    print("键盘操作: Ctrl+C 复制选中内容")
    # 清空后 Ctrl+V 粘贴
    search_box.clear()
    sleep(0.5)
    search_box.send_keys(Keys.CONTROL + 'v')
    sleep(0.5)
    print(f"键盘操作: Ctrl+V 粘贴，结果='{search_box.get_attribute('value')}'")

    # ══════════════════════════════════════════════════════
    # 阶段三：按钮状态获取 + 鼠标操作（技术点4、5、6）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段三：按钮状态获取 + 模拟鼠标操作")
    print("=" * 40)

    # 步骤7：判断搜索按钮状态 —— 技术点4：获取按钮状态
    search_button = driver.find_element(By.NAME, "imageField")
    print(f"搜索按钮是否可用(is_enabled): {search_button.is_enabled()}")
    print(f"搜索按钮是否可见(is_displayed): {search_button.is_displayed()}")

    # 步骤8：鼠标悬停在导航栏"所有分类"上 —— 技术点6：模拟鼠标悬停
    try:
        nav_elem = driver.find_element(By.LINK_TEXT, "所有分类")
    except Exception:
        try:
            nav_elem = driver.find_element(By.PARTIAL_LINK_TEXT, "所有分类")
        except Exception:
            nav_elem = driver.find_element(By.XPATH, "//a[contains(text(),'所有分类')]")
    actions = ActionChains(driver)
    actions.move_to_element(nav_elem).perform()
    sleep(1)
    print("鼠标操作: 悬停'所有分类'")

    # 步骤9：鼠标双击搜索框 —— 技术点6：模拟鼠标双击
    actions = ActionChains(driver)
    actions.double_click(search_box).perform()
    sleep(0.5)
    print("鼠标操作: 双击搜索框")

    # 步骤10：鼠标右键点击页面LOGO —— 技术点6：模拟鼠标右键
    try:
        logo = driver.find_element(By.XPATH, "//a[@href='./']")
    except Exception:
        logo = driver.find_element(By.XPATH, "//div[contains(@class,'logo')]//a")
    actions = ActionChains(driver)
    actions.context_click(logo).perform()
    sleep(1)
    print("鼠标操作: 右键点击页面LOGO")

    # 步骤11：清空搜索框，点击搜索按钮 —— 技术点5：选中按钮
    search_box.clear()
    sleep(0.5)
    search_button.click()
    print("已点击搜索按钮（选中按钮操作）")
    sleep(2)

    # ══════════════════════════════════════════════════════
    # 阶段四：消息框处理（技术点7）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段四：消息框处理（alert 确定 + confirm 取消）")
    print("=" * 40)

    # 步骤12：切换到alert消息框，获取文本 —— 技术点7：消息框确定
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"alert消息框文本: '{alert_text}'")

    # 步骤13：截屏保留消息框状态 —— 技术点7：消息框截屏
    ss(driver, "alert_before_accept.png")
    print("已截屏alert消息框（确定前）")

    # 步骤14：点击"确定"关闭alert
    alert.accept()
    sleep(1)
    print("已点击alert'确定'按钮，消息框关闭")

    # 步骤15：通过JS触发confirm消息框，验证"取消"操作 —— 技术点7：消息框取消
    driver.execute_script("confirm('确定要取消吗？这是confirm消息框测试');")
    sleep(1)
    confirm_alert = driver.switch_to.alert
    print(f"confirm消息框文本: '{confirm_alert.text}'")
    ss(driver, "confirm_before_dismiss.png")
    confirm_alert.dismiss()  # 点击取消
    sleep(1)
    print("已点击confirm'取消'按钮，消息框关闭")

    # ══════════════════════════════════════════════════════
    # 阶段五：浏览器前进后退 + 获取静态文本数据处理（技术点1、2）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段五：浏览器前进后退 + 获取静态文本数据")
    print("=" * 40)

    # 步骤16：输入关键字搜索商品
    search_box = driver.find_element(By.NAME, "keywords")
    search_box.clear()
    search_box.send_keys("P806")
    search_button = driver.find_element(By.NAME, "imageField")
    search_button.click()
    sleep(3)
    search_url = driver.current_url
    print(f"搜索结果页: {search_url}")

    # 步骤17：浏览器后退 —— 技术点1：浏览器后退
    driver.back()
    sleep(2)
    print(f"后退后URL: {driver.current_url}")

    # 步骤18：浏览器前进 —— 技术点1：浏览器前进
    driver.forward()
    sleep(2)
    print(f"前进后URL: {driver.current_url}")

    # 步骤19：点击商品链接进入详情页
    try:
        product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "P806")
    except Exception:
        product_link = driver.find_element(By.XPATH, "//a[contains(@href,'goods.php')]")
    product_link.click()
    sleep(3)
    print(f"商品详情页: {driver.current_url}")

    # 步骤20：获取页面静态文本 —— 技术点2：获取静态文本数据并处理
    try:
        product_name_elem = driver.find_element(
            By.XPATH, "//h1 | //span[contains(@class,'goods_name')] | //div[contains(@class,'goodsName')]"
        )
        product_name = product_name_elem.text
    except Exception:
        product_name = driver.find_element(By.TAG_NAME, "h1").text
    print(f"商品名称: {product_name}")

    # 获取价格文本
    page_text = driver.page_source
    price_match = re.search(r'[¥￥]\s*([\d.]+)', page_text)
    if price_match:
        price_str = price_match.group(1)
        price_num = float(price_str)
        print(f"商品价格: ¥{price_num}")
        # 数据处理：判断价格区间
        if price_num > 100:
            print(f"数据处理: 价格{price_num} > 100，属于高价商品")
        else:
            print(f"数据处理: 价格{price_num} <= 100，属于平价商品")
    else:
        print("未找到价格信息")

    # ══════════════════════════════════════════════════════
    # 阶段六：登录 + 复选框状态获取与选中（技术点4、5补充）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段六：复选框状态获取与选中")
    print("=" * 40)

    # 步骤21：打开注册页，定位"同意协议"复选框
    driver.get(BASE_URL + "user.php?act=register")
    sleep(2)
    try:
        agreement_cb = driver.find_element(By.NAME, "agreement")
    except Exception:
        try:
            agreement_cb = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        except Exception:
            agreement_cb = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

    # 步骤22：获取复选框状态 —— 技术点4补充：获取复选框状态
    print(f"复选框是否选中(is_selected): {agreement_cb.is_selected()}")
    print(f"复选框是否可用(is_enabled): {agreement_cb.is_enabled()}")

    # 步骤23：选中复选框 —— 技术点5补充：选中复选框
    if not agreement_cb.is_selected():
        agreement_cb.click()
        sleep(0.5)
        print("已选中复选框")
    print(f"复选框当前状态(is_selected): {agreement_cb.is_selected()}")

    # ══════════════════════════════════════════════════════
    # 阶段七：切换窗口 + 验证码 + Frame + 元素截屏（技术点8、9、10、11）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段七：切换窗口 + 验证码获取 + Frame + 元素截屏")
    print("=" * 40)

    # 步骤24：保存原始窗口句柄并用JS打开新标签页 —— 技术点8：切换窗口
    original_window = driver.current_window_handle
    print(f"原始窗口句柄: {original_window}")
    driver.execute_script("window.open();")
    sleep(1)
    all_windows = driver.window_handles
    # 切换到新窗口
    driver.switch_to.window(all_windows[-1])
    print(f"已切换到新窗口: {driver.current_window_handle}")

    # 步骤25：在新窗口打开后台管理页
    driver.get(ADMIN_URL + "index.php")
    sleep(3)
    print(f"后台管理页: {driver.current_url}")

    # 步骤26：定位验证码图片并截屏保存 —— 技术点11：验证码获取
    try:
        captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")
    except Exception:
        try:
            captcha_img = driver.find_element(By.CSS_SELECTOR, "img[src*='captcha']")
        except Exception:
            captcha_img = driver.find_element(By.XPATH, "//form//img")
    captcha_path = os.path.join(SCREENSHOT_DIR, "captcha_image.png")
    captcha_img.screenshot(captcha_path)
    print(f"验证码截图已保存: {captcha_path}")

    # 步骤27：输入后台登录信息（万能验证码: 0）
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.NAME, "captcha").clear()
    driver.find_element(By.NAME, "captcha").send_keys("0")
    print("已输入后台登录信息（admin / admin123 / 万能验证码0）")

    # 步骤28：点击登录按钮
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    sleep(5)
    print(f"登录后URL: {driver.current_url}")

    # 步骤29：切换到menu-frame并点击"商品列表" —— 技术点9：切换Frame
    driver.switch_to.frame("menu-frame")
    print("已切换到menu-frame")
    try:
        driver.find_element(By.LINK_TEXT, "商品列表").click()
    except Exception:
        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, "商品列表").click()
        except Exception:
            driver.find_element(By.XPATH, "//a[contains(text(),'商品列表')]").click()
    sleep(3)
    print("已点击'商品列表'菜单")

    # 步骤30：切回主文档，再切换到main-frame —— 技术点9：切换第二个Frame
    driver.switch_to.default_content()
    driver.switch_to.frame("main-frame")
    print("已切换到main-frame")
    sleep(2)

    # 步骤31：对页面元素进行截屏 —— 技术点10：页面元素截屏
    try:
        target_elem = driver.find_element(By.XPATH, "//table//tr[2]")
        target_elem.screenshot(os.path.join(SCREENSHOT_DIR, "element_screenshot.png"))
        print("已对商品列表第一行数据行进行元素截屏")
    except Exception:
        ss(driver, "element_screenshot.png")
        print("已对整页进行截图（元素截屏备用方案）")

    # 步骤32：切回原始前台窗口 —— 技术点8：切换回原窗口
    driver.switch_to.window(original_window)
    print(f"已切回原始窗口: {driver.current_window_handle}")

    # ══════════════════════════════════════════════════════
    # 阶段八：窗口操作收尾（技术点1补充）
    # ══════════════════════════════════════════════════════
    print("\n" + "=" * 40)
    print("阶段八：窗口操作收尾")
    print("=" * 40)

    # 步骤33：最小化窗口
    driver.minimize_window()
    sleep(1)
    size = driver.get_window_size()
    print(f"最小化后窗口大小: {size['width']} x {size['height']}")

    # 步骤34：恢复最大化
    driver.maximize_window()
    sleep(1)
    print("已恢复最大化窗口")

    print("\n" + "=" * 60)
    print("✅ 全部自动化测试流程执行完毕！")
    print("=" * 60)

except Exception as e:
    print(f"\n❌ 测试过程中发生错误: {e}")
    import traceback
    traceback.print_exc()

finally:
    driver.quit()
    print("浏览器已关闭")
