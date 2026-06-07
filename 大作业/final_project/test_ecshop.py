# -*- coding: utf-8 -*-
# 功能：ECShop网站自动化测试 —— 整合平时模块二实验05/06/07/08/09/10/11/13/14，
#        覆盖大作业全部11个核心技术点：浏览器前进后退、窗口大小操作、
#        获取文本框/静态文本数据并处理、获取按钮/复选框状态、选中按钮/复选框、
#        模拟鼠标操作（悬停/双击/右键）、模拟键盘操作（全选/复制/粘贴）、
#        消息框处理（确定/取消/截屏）、切换浏览器窗口和Frame、
#        页面元素截屏操作、验证码获取操作
# 时间：2026年6月
# 作者：（填写姓名）
# 学号：（填写学号）
# 班级：（填写班级）
# 版本：v1.0
# 测试环境：Windows 11 + Python 3.x + Selenium 4.x + Chrome浏览器 + ChromeDriver（webdriver-manager自动管理）
# 被测系统：ECShop V2.7.1（PHP + MySQL），部署在本地 localhost

import os
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# ============================================================
# 全局配置
# ============================================================
BASE_URL = "http://localhost/upload/"
ADMIN_URL = "http://localhost/upload/admin/"
# 测试账号：前台 vip/vip，后台 admin/admin123（万能验证码：0）
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def ss(driver, filename):
    """快捷全屏截图函数，保存到screenshots目录"""
    path = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(path)
    print(f"   📸 截图已保存: {filename}")


def elem_shot(element, filename):
    """快捷元素截图函数"""
    path = os.path.join(SCREENSHOT_DIR, filename)
    element.screenshot(path)
    print(f"   📸 元素截图已保存: {filename}")


print("=" * 60)
print("ECShop 网站自动化测试 —— 软件测试大作业")
print("整合实验05/06/07/08/09/10/11/13/14，覆盖11个核心技术点")
print("=" * 60)

# ============================================================
# 初始化浏览器驱动
# ============================================================
print("\n>>> 初始化浏览器驱动...")
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except Exception:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)

try:
    # ========================================================
    # 阶段一：浏览器窗口操作（来源：实验05）
    # 技术点：窗口大小操作（最大化、自定义尺寸、位置设置）
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段一：浏览器窗口大小与位置操作")
    print("=" * 60)

    # 步骤1：打开ECShop前台首页，最大化窗口
    print("\n[步骤1] 打开ECShop前台首页并最大化窗口")
    driver.get(BASE_URL + "index.php")
    driver.maximize_window()
    sleep(1)
    size = driver.get_window_size()
    pos = driver.get_window_position()
    print(f"   最大化后窗口尺寸: 宽{size['width']}px, 高{size['height']}px")
    print(f"   窗口左上角坐标: x={pos['x']}, y={pos['y']}")
    ss(driver, "01_window_maximized.png")

    # 步骤2：设置窗口为自定义尺寸 800x600，打印尺寸
    print("\n[步骤2] 设置窗口大小为 800×600")
    driver.set_window_size(800, 600)
    sleep(1)
    size = driver.get_window_size()
    print(f"   当前窗口尺寸: 宽{size['width']}px, 高{size['height']}px")
    ss(driver, "02_window_800x600.png")

    # 步骤3：设置窗口位置为 (60, 60)，打印坐标
    print("\n[步骤3] 设置窗口左上角坐标为 (60, 60)")
    driver.set_window_position(60, 60)
    sleep(1)
    pos = driver.get_window_position()
    print(f"   当前窗口左上角坐标: x={pos['x']}, y={pos['y']}")
    ss(driver, "03_window_position.png")

    # 步骤4：恢复最大化窗口，打印尺寸
    print("\n[步骤4] 恢复最大化窗口")
    driver.maximize_window()
    sleep(1)
    size = driver.get_window_size()
    print(f"   恢复后窗口尺寸: 宽{size['width']}px, 高{size['height']}px")

    # ========================================================
    # 阶段二：文本框数据获取 + 模拟键盘操作（来源：实验06 + 实验07）
    # 技术点：获取文本框数据、模拟键盘操作（全选/复制/粘贴）
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段二：获取文本框数据 + 模拟键盘操作")
    print("=" * 60)

    # 步骤5：获取搜索框的默认文本值
    print("\n[步骤5] 获取搜索框默认文本值")
    search_box = driver.find_element(By.NAME, "keywords")
    default_value = search_box.get_attribute("value")
    print(f"   搜索框默认值: '{default_value}'（应为空字符串）")

    # 步骤6：向搜索框输入内容，然后模拟键盘操作
    print("\n[步骤6] 向搜索框输入内容并执行键盘操作")
    search_box.clear()
    search_box.send_keys("100测试")
    sleep(0.5)
    print(f"   输入后搜索框内容: '{search_box.get_attribute('value')}'")

    # Ctrl+A 全选
    print("   → 执行 Ctrl+A 全选")
    search_box.send_keys(Keys.CONTROL + 'a')
    sleep(0.5)

    # Ctrl+C 复制
    print("   → 执行 Ctrl+C 复制")
    search_box.send_keys(Keys.CONTROL + 'c')
    sleep(0.5)

    # 清空搜索框
    search_box.clear()
    sleep(0.5)
    print(f"   清空后搜索框内容: '{search_box.get_attribute('value')}'")

    # Ctrl+V 粘贴
    print("   → 执行 Ctrl+V 粘贴")
    search_box.send_keys(Keys.CONTROL + 'v')
    sleep(0.5)
    pasted_value = search_box.get_attribute("value")
    print(f"   粘贴后搜索框内容: '{pasted_value}'")
    if pasted_value == "100测试":
        print("   ✓ 复制粘贴验证成功，内容一致")
    else:
        print("   ⚠ 粘贴内容与原始内容不一致")
    ss(driver, "04_keyboard_actions.png")

    # ========================================================
    # 阶段三：按钮/复选框状态 + 模拟鼠标操作 + 消息框处理
    #         （来源：实验06 + 实验08 + 实验09）
    # 技术点：获取按钮/复选框状态、选中按钮、模拟鼠标操作、
    #         消息框确定/取消/截屏
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段三：按钮状态检测 + 模拟鼠标操作 + 消息框处理")
    print("=" * 60)

    # 步骤7：获取搜索按钮的可用状态和可见状态
    print("\n[步骤7] 获取搜索按钮的状态")
    search_button = driver.find_element(By.NAME, "imageField")
    is_enabled = search_button.is_enabled()
    is_displayed = search_button.is_displayed()
    print(f"   搜索按钮 is_enabled() = {is_enabled}")
    print(f"   搜索按钮 is_displayed() = {is_displayed}")

    # 步骤8：模拟鼠标操作 —— 悬停"登录"导航链接
    # 注：ECShop首页不存在"所有分类"，用实验03/08确认存在的"登录"替代
    print("\n[步骤8] 鼠标悬停'登录'导航链接")
    try:
        hover_target = driver.find_element(By.LINK_TEXT, "登录")
    except Exception:
        try:
            hover_target = driver.find_element(By.PARTIAL_LINK_TEXT, "登")
        except Exception:
            hover_target = driver.find_element(
                By.XPATH, "//a[contains(@href,'user.php')]")
    actions = ActionChains(driver)
    actions.move_to_element(hover_target).perform()
    sleep(1.5)
    print("   ✓ 鼠标悬停'登录'链接成功")
    ss(driver, "05_mouse_hover.png")

    # 步骤9：模拟鼠标操作 —— 双击搜索框
    print("\n[步骤9] 鼠标双击搜索框")
    actions = ActionChains(driver)
    actions.double_click(search_box).perform()
    sleep(1)
    print("   ✓ 鼠标双击搜索框成功")

    # 步骤10：模拟鼠标操作 —— 右键点击页面LOGO
    # 参考实验03的LOGO定位方式：//div[@id='logo']//a
    print("\n[步骤10] 鼠标右键点击页面LOGO")
    try:
        logo = driver.find_element(By.XPATH, "//div[@id='logo']//a")
    except Exception:
        try:
            logo = driver.find_element(By.XPATH, "//a[@href='./']//img")
        except Exception:
            logo = driver.find_element(By.XPATH, "//img[contains(@src,'logo')]")
    actions = ActionChains(driver)
    actions.context_click(logo).perform()
    sleep(1.5)
    print("   ✓ 鼠标右键点击LOGO成功（已触发浏览器上下文菜单）")
    ss(driver, "06_mouse_right_click.png")

    # 步骤11：清空搜索框后点击搜索按钮（触发alert消息框）
    print("\n[步骤11] 清空搜索框，点击搜索按钮触发alert")
    search_box.clear()
    sleep(0.5)
    search_button.click()
    sleep(2)
    print("   已点击搜索按钮（空关键字）")

    # 步骤12：处理alert消息框 —— 获取文本 → 点击确定 → 截屏
    # 注：alert打开期间Selenium禁止执行save_screenshot等WebDriver命令，
    #     因此参照实验09做法：先获取文本再accept，关闭后截图证明页面恢复正常
    print("\n[步骤12] 处理alert消息框：获取文本 → 点击确定")
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"   alert消息框文本: '{alert_text}'")
    alert.accept()
    sleep(1)
    print("   ✓ 已点击alert的'确定'按钮，消息框关闭")
    ss(driver, "07_after_alert_closed.png")

    # 步骤13：用JS触发confirm对话框 —— 点击取消 → 截屏
    print("\n[步骤13] JS触发confirm对话框: 获取文本 → 点击取消")
    driver.execute_script("confirm('您确定要执行此操作吗？测试confirm取消功能')")
    sleep(1.5)
    alert = driver.switch_to.alert
    confirm_text = alert.text
    print(f"   confirm消息框文本: '{confirm_text}'")
    alert.dismiss()
    sleep(1)
    print("   ✓ 已点击confirm的'取消'按钮，消息框关闭")
    ss(driver, "08_after_confirm_closed.png")

    # ========================================================
    # 阶段四：商品搜索 + 浏览器前进后退 + 获取静态文本数据处理
    #         （来源：实验05 + 实验06）
    # 技术点：浏览器前进后退、获取静态文本数据并处理
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段四：商品搜索 + 浏览器前进后退 + 静态文本处理")
    print("=" * 60)

    # 步骤14：输入关键字搜索商品
    print("\n[步骤14] 输入关键字'P806'搜索商品")
    search_box = driver.find_element(By.NAME, "keywords")
    search_box.clear()
    search_box.send_keys("P806")
    sleep(0.5)
    search_button = driver.find_element(By.NAME, "imageField")
    search_button.click()
    sleep(3)
    print(f"   搜索后页面URL: {driver.current_url}")
    search_url = driver.current_url
    ss(driver, "09_search_result.png")

    # 步骤15：浏览器后退到首页
    print("\n[步骤15] 浏览器后退 (driver.back())")
    driver.back()
    sleep(3)
    print(f"   后退后URL: {driver.current_url}")
    ss(driver, "10_after_back.png")

    # 步骤16：浏览器前进回搜索结果
    print("\n[步骤16] 浏览器前进 (driver.forward())")
    driver.forward()
    sleep(3)
    print(f"   前进后URL: {driver.current_url}")
    if driver.current_url == search_url:
        print("   ✓ 前进/后退URL一致，导航正确")

    # 步骤17：点击商品进入详情页
    print("\n[步骤17] 点击第一个搜索结果进入商品详情页")
    try:
        product = driver.find_element(By.XPATH, "//a[contains(@href,'goods.php')]")
    except Exception:
        product = driver.find_element(By.PARTIAL_LINK_TEXT, "P806")
    product.click()
    sleep(3)
    print(f"   商品详情页URL: {driver.current_url}")

    # 步骤18：获取静态文本数据（商品名称和价格）并进行处理
    # 基于实际DOM分析：商品名→<p class="f_l">, 价格→<font id="ECS_SHOPPRICE">
    print("\n[步骤18] 获取商品名称和价格静态文本，进行数据处理")
    # 获取商品名称：ECShop商品页无h1，商品名在 <p class="f_l">
    try:
        goods_name = driver.find_element(By.XPATH, "//p[@class='f_l']").text
    except Exception:
        try:
            goods_name = driver.find_element(By.XPATH, "//h1").text
        except Exception:
            goods_name = driver.title
    if not goods_name:
        goods_name = "（未获取到商品名）"
    print(f"   商品名称: {goods_name}")
    # 获取价格：ECShop价格元素id明确——ECS_SHOPPRICE(本店售价)、ECS_GOODS_AMOUNT(总价)
    price_text = ""
    for price_id in ["ECS_SHOPPRICE", "ECS_GOODS_AMOUNT"]:
        try:
            price_text = driver.find_element(By.ID, price_id).text
            if price_text:
                break
        except Exception:
            continue
    if not price_text:
        try:
            price_text = driver.find_element(
                By.XPATH, "//*[contains(text(),'￥') or contains(text(),'元')]").text
        except Exception:
            match = re.search(r'￥(\d+(?:\.\d+)?)元?', driver.page_source)
            if match:
                price_text = "￥" + match.group(1)
            else:
                price_text = "￥0"
    print(f"   价格文本: '{price_text}'")
    # 使用正则表达式从价格文本中提取数字并判断价格区间
    price_match = re.search(r'(\d+)', price_text.replace(',', ''))
    if price_match:
        price_num = int(price_match.group(1))
        print(f"   提取的价格数字: {price_num}")
        if price_num < 100:
            print("   → 该商品为低价商品（<100元）")
        elif price_num < 500:
            print("   → 该商品为中价商品（100-500元）")
        else:
            print("   → 该商品为高价商品（>500元）")
    else:
        print("   ⚠ 未能从价格文本中提取数字")
    ss(driver, "11_product_detail.png")

    # ========================================================
    # 阶段五：复选框状态获取与选中（来源：实验06）
    # 技术点：获取复选框状态、选中复选框
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段五：复选框状态获取与选中操作")
    print("=" * 60)

    # 步骤19：打开注册页面
    print("\n[步骤19] 打开用户注册页面")
    driver.get(BASE_URL + "user.php?act=register")
    sleep(3)
    print(f"   注册页面URL: {driver.current_url}")

    # 步骤20：定位"用户协议"复选框，获取状态
    print("\n[步骤20] 定位'我已看过并同意用户协议'复选框，获取状态")
    try:
        agreement_cb = driver.find_element(By.NAME, "agreement")
    except Exception:
        try:
            agreement_cb = driver.find_element(By.ID, "agreement")
        except Exception:
            agreement_cb = driver.find_element(
                By.XPATH, "//input[@type='checkbox']")
    cb_selected = agreement_cb.is_selected()
    cb_enabled = agreement_cb.is_enabled()
    print(f"   复选框 is_selected() = {cb_selected}")
    print(f"   复选框 is_enabled() = {cb_enabled}")

    # 步骤21：选中复选框并验证状态变化
    print("\n[步骤21] 选中复选框并验证状态")
    if not cb_selected:
        driver.execute_script("arguments[0].scrollIntoView();", agreement_cb)
        sleep(0.5)
        agreement_cb.click()
        sleep(1)
        new_state = agreement_cb.is_selected()
        print(f"   点击后 is_selected() = {new_state}")
        if new_state:
            print("   ✓ 复选框选中成功")
        else:
            print("   ⚠ 复选框选中失败")
    else:
        print("   复选框原本已选中，无需操作")
    ss(driver, "12_checkbox_selected.png")

    # ========================================================
    # 阶段六：切换浏览器窗口 + Frame切换 + 验证码获取 + 元素截屏
    #         （来源：实验10 + 实验11 + 实验13 + 实验14）
    # 技术点：切换窗口、切换Frame、验证码获取、元素截屏
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段六：切换窗口 + Frame切换 + 验证码获取 + 元素截屏")
    print("=" * 60)

    # 步骤22：保存原始窗口句柄，用JS打开新标签页
    print("\n[步骤22] 用JS打开新标签页（后台管理登录页）")
    original_window = driver.current_window_handle
    print(f"   原始前台窗口句柄: {original_window[:20]}...")
    driver.execute_script(f"window.open('{ADMIN_URL}index.php');")
    sleep(3)

    # 步骤23：切换到新窗口（后台管理登录页）
    print("\n[步骤23] 切换到新窗口（后台管理登录页）")
    all_windows = driver.window_handles
    print(f"   当前窗口总数: {len(all_windows)}")
    driver.switch_to.window(all_windows[-1])
    print(f"   已切换到后台窗口，URL: {driver.current_url}")
    print(f"   页面标题: {driver.title}")

    # 步骤24：定位验证码图片元素并截图保存（验证码获取操作）
    print("\n[步骤24] 定位验证码图片元素并截屏保存")
    try:
        captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")
        elem_shot(captcha_img, "13_captcha_image.png")
        print("   ✓ 验证码截图已保存")
    except Exception as e:
        print(f"   ⚠ 验证码图片定位失败: {e}")

    # 步骤25：输入后台登录信息并登录
    print("\n[步骤25] 输入后台账号信息并登录（使用万能验证码0）")
    admin_username = driver.find_element(By.NAME, "username")
    admin_username.clear()
    admin_username.send_keys("admin")
    admin_pwd = driver.find_element(By.NAME, "password")
    admin_pwd.clear()
    admin_pwd.send_keys("admin123")
    admin_captcha = driver.find_element(By.NAME, "captcha")
    admin_captcha.clear()
    admin_captcha.send_keys("0")  # ECShop后台万能验证码
    print(f"   已输入: admin / admin123 / 验证码=0")
    ss(driver, "14_admin_login_form.png")

    # 点击"进入管理中心"登录
    login_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_btn.click()
    sleep(5)
    print(f"   登录后URL: {driver.current_url}")

    # 步骤26：切换Frame —— 左侧菜单frame (menu-frame)
    print("\n[步骤26] 切换到左侧菜单Frame (menu-frame)")
    driver.switch_to.default_content()
    driver.switch_to.frame("menu-frame")
    print("   ✓ 已切换到 menu-frame")
    sleep(1)

    # 在菜单Frame中点击"商品列表"
    try:
        menu_item = driver.find_element(By.LINK_TEXT, "商品列表")
    except Exception:
        menu_item = driver.find_element(By.PARTIAL_LINK_TEXT, "商品列表")
    menu_item.click()
    print("   已点击左侧菜单'商品列表'")
    sleep(3)

    # 步骤27：切换Frame —— 回到主文档再进入 main-frame
    print("\n[步骤27] 切换回主文档 → 切换到主内容Frame (main-frame)")
    driver.switch_to.default_content()
    driver.switch_to.frame("main-frame")
    print("   ✓ 已切换到 main-frame")
    sleep(2)

    # 步骤28：对商品列表区域的元素进行截图（页面元素截屏操作）
    # 参考实验13的多级回退策略
    print("\n[步骤28] 对商品列表表格区域进行元素截图")
    try:
        # 方法1：定位商品列表表格第一行数据
        first_row = driver.find_element(By.XPATH, "//table//tr[2]")
        elem_shot(first_row, "15_element_screenshot.png")
        print("   ✓ 商品列表行元素截图已保存")
    except Exception:
        try:
            # 方法2：尝试实验13用过的容器选择器
            for sel in [".list-div", "#listDiv", "form", "body"]:
                try:
                    el = driver.find_element(By.CSS_SELECTOR, sel)
                    elem_shot(el, "15_element_screenshot.png")
                    print(f"   ✓ 商品列表区域截图已保存（使用 {sel}）")
                    break
                except Exception:
                    continue
            else:
                raise Exception("所有选择器均失败")
        except Exception as e:
            print(f"   ⚠ 元素截图失败，使用全屏截图: {e}")
            ss(driver, "15_element_screenshot_fallback.png")

    # 步骤29：切回原始前台窗口
    print("\n[步骤29] 切换回原始前台窗口")
    driver.switch_to.window(original_window)
    print(f"   已切回前台窗口，URL: {driver.current_url}")
    ss(driver, "16_back_to_frontend.png")

    # ========================================================
    # 阶段七：窗口最小化 + 恢复最大化收尾（来源：实验05）
    # 技术点：窗口大小操作
    # ========================================================
    print("\n" + "=" * 60)
    print("阶段七：窗口最小化与恢复收尾")
    print("=" * 60)

    # 步骤30：最小化窗口并打印尺寸
    print("\n[步骤30] 最小化浏览器窗口")
    driver.minimize_window()
    sleep(2)
    size = driver.get_window_size()
    print(f"   最小化后窗口尺寸: 宽{size['width']}px, 高{size['height']}px")

    # 步骤31：恢复最大化窗口，最终验证
    print("\n[步骤31] 恢复最大化窗口并最终验证")
    driver.maximize_window()
    sleep(1)
    size = driver.get_window_size()
    pos = driver.get_window_position()
    print(f"   最终窗口尺寸: 宽{size['width']}px, 高{size['height']}px")
    print(f"   最终窗口坐标: x={pos['x']}, y={pos['y']}")
    ss(driver, "17_final_maximized.png")

    # ========================================================
    # 完成
    # ========================================================
    print("\n" + "=" * 60)
    print("✅ 大作业自动化测试全部完成！")
    print("=" * 60)

    # 汇总覆盖的11个技术点
    print("\n覆盖的技术点一览：")
    tech_points = [
        ("① 浏览器前进后退",        "步骤15(driver.back()) / 步骤16(driver.forward())"),
        ("② 窗口大小操作",          "阶段一(最大化/800×600/位置60,60) + 阶段七(最小化/恢复)"),
        ("③ 获取文本框/静态文本并处理","步骤5(搜索框默认值) / 步骤18(商品名称/价格+正则处理)"),
        ("④ 获取按钮/复选框状态",    "步骤7(is_enabled/is_displayed) / 步骤20(is_selected/is_enabled)"),
        ("⑤ 选中按钮/复选框",       "步骤11(点击搜索按钮) / 步骤21(选中协议复选框)"),
        ("⑥ 模拟鼠标操作",          "步骤8(悬停) / 步骤9(双击) / 步骤10(右键)"),
        ("⑦ 模拟键盘操作",          "步骤6(Ctrl+A全选 / Ctrl+C复制 / Ctrl+V粘贴)"),
        ("⑧ 消息框确定/取消/截屏",   "步骤12(alert确定+截屏) / 步骤13(confirm取消+截屏)"),
        ("⑨ 切换窗口和Frame",       "步骤22-23(窗口切换) / 步骤26-27(Frame切换)"),
        ("⑩ 页面元素截屏操作",      "步骤28(商品列表行元素截图) + 辅助函数elem_shot()"),
        ("⑪ 验证码获取操作",        "步骤24(验证码图片定位+截图保存)"),
    ]
    for name, detail in tech_points:
        print(f"   {name}: {detail}")

    print(f"\n所有截图已保存到: {SCREENSHOT_DIR}")
    print(f"共生成约17张截图作为测试证据")

except Exception as e:
    print(f"\n❌ 测试过程中发生错误: {e}")
    import traceback
    traceback.print_exc()
    # 发生错误时也保存一张现场截图
    try:
        ss(driver, "99_error_screenshot.png")
    except Exception:
        pass

finally:
    print("\n等待3秒后关闭浏览器...")
    sleep(3)
    driver.quit()
    print("✅ 浏览器已关闭")
    print("=" * 60)
    print("测试结束")
    print("=" * 60)
