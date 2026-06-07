# -*- coding: utf-8 -*-
# 诊断脚本：获取P806商品详情页HTML，分析价格元素定位失败原因

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except Exception:
    driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

# 1. 打开P806商品详情页
driver.get("http://localhost/upload/goods.php?id=24")
sleep(3)
print(f"URL: {driver.current_url}")
print(f"Title: {driver.title}")

# 2. 保存完整页面源码
source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p806_source.html")
with open(source_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)
print(f"\n页面源码已保存到: {source_path}")

# 3. 尝试各种方式定位价格 ----------
print("\n" + "=" * 60)
print("尝试定位价格元素：")
print("=" * 60)

strategies = [
    # 策略1: 常见class名
    ("CSS", "//*[contains(@class,'price')]"),
    # 策略2: 常见id名
    ("CSS", "//*[contains(@id,'price')]"),
    # 策略3: 含￥符号的元素
    ("XPATH", "//*[contains(text(),'￥')]"),
    # 策略4: 含"元"的元素
    ("XPATH", "//*[contains(text(),'元')]"),
    # 策略5: shop_price
    ("CSS", "//*[contains(@class,'shop')]"),
    # 策略6: 商品价格专用id (ECShop常见)
    ("ID", "ECS_SHOPPRICE"),
    # 策略7: 直接用goods_price id (ECShop常见)
    ("ID", "ECS_GOODS_AMOUNT"),
    # 策略8: font标签 (老ECShop)
    ("TAG", "font"),
]

for method, selector in strategies:
    try:
        elements = driver.find_elements(By.XPATH, selector)
        for el in elements:
            txt = el.text.strip()
            tag = el.tag_name
            cls = el.get_attribute("class") or ""
            eid = el.get_attribute("id") or ""
            if txt and len(txt) < 50:
                print(f"  [{method}] selector={selector}")
                print(f"    tag=<{tag}> class=\"{cls}\" id=\"{eid}\"")
                print(f"    text=\"{txt}\"")
    except Exception as e:
        print(f"  [{method}] selector={selector} -> ERROR: {e}")

# 4. 打印body里所有含数字的element文本 ----------
print("\n" + "=" * 60)
print("页面中所有含'￥'或数字的可见文本块：")
print("=" * 60)
try:
    all_elements = driver.find_elements(By.XPATH, "//*[string-length(text())>0]")
    for el in all_elements:
        txt = el.text.strip()
        if txt and len(txt) < 100:
            if '￥' in txt or '元' in txt or any(c.isdigit() for c in txt):
                tag = el.tag_name
                cls = el.get_attribute("class") or ""
                eid = el.get_attribute("id") or ""
                print(f"  <{tag}> class=\"{cls}\" id=\"{eid}\"")
                print(f"  text: \"{txt}\"")
                print()
except Exception as e:
    print(f"ERROR: {e}")

# 5. 特别检查h1和标题区域 ----------
print("=" * 60)
print("商品名称区域：")
print("=" * 60)
try:
    # h1
    h1s = driver.find_elements(By.TAG_NAME, "h1")
    for h in h1s:
        print(f"  h1: \"{h.text}\"")
    # title
    print(f"  driver.title: \"{driver.title}\"")
    # goodsName
    for el in driver.find_elements(By.XPATH, "//*[contains(@class,'goodsName') or contains(@class,'goods')]"):
        if el.text.strip():
            print(f"  goods: <{el.tag_name}> class=\"{el.get_attribute('class')}\" text=\"{el.text.strip()}\"")
except Exception as e:
    print(f"ERROR: {e}")

driver.quit()
print("\nDone.")
