---
title: Selenium 自动化测试实验指南
description: 软件测试实验的标准流程和注意事项
inclusion: auto
---

# Selenium 自动化测试实验指南

## 🎯 项目背景

**项目：** 软件测试课程实验
**测试对象：** ECShop V2.7.1 电商系统（2009年老版本）
**测试工具：** Python + Selenium + Chrome
**工作目录：** `d:\学习资料\大三下\软件测试`

---

## ⚙️ 环境配置

### 必须使用的工具

1. **浏览器：Chrome**（不是 Firefox）
   - 实验要求可能写 Firefox，但统一改用 Chrome
   - 更稳定，兼容性更好

2. **驱动：ChromeDriver**
   - 使用 `webdriver-manager` 自动管理
   - 不需要手动下载

3. **Python 环境**
   - 虚拟环境：`venv`
   - 已安装：selenium, webdriver-manager

### 标准代码模板

```python
# -*- coding: utf-8 -*-
# 实验XX - 标题

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

try:
    # 实验步骤
    pass
    
except Exception as e:
    print(f"❌ 发生错误: {e}")
    
finally:
    driver.quit()
```

---

## 📝 实验流程规范

### 1. 创建实验文件夹

```
实验模块二/
├── 实验01/
│   ├── 实验01.py
│   ├── 实验01总结.md
│   └── README.md
├── 实验02/
│   ├── 实验02_1_xxx.py
│   ├── 实验02_2_xxx.py
│   ├── 实验02总结.md
│   └── README.md
```

### 2. 编写实验脚本

**必须包含：**
- ✅ 文件编码声明：`# -*- coding: utf-8 -*-`
- ✅ 详细的步骤注释
- ✅ 异常处理
- ✅ 执行日志输出
- ✅ 截图保存（可选）

### 3. 创建辅助工具

**推荐创建：**
- `查找元素.py` - 查找页面元素定位方式
- `查找表单字段.py` - 查找表单字段名称

### 4. 编写总结文档

**必须创建：**
- `实验XX总结.md` - 完整的实验总结
- `README.md` - 使用说明

### 5. Git 提交

**提交前检查：**
- ✅ 代码能正常运行
- ✅ 文档已完成
- ✅ 截图已保存
- ✅ 更新 .gitignore

---

## 🐛 常见问题和解决方案

### 问题1：中文输入乱码

**现象：** 输入中文显示乱码

**解决方案：**
```python
# ❌ 不要用 send_keys 输入中文
element.send_keys("中文内容")

# ✅ 使用 JavaScript 设置值
driver.execute_script("arguments[0].value = '中文内容';", element)
```

**必须添加：**
```python
# -*- coding: utf-8 -*-  # 文件开头
```

### 问题2：元素定位失败

**原因：**
- 页面还在加载
- 元素不可见
- 定位方式错误

**解决方案：**
```python
# 1. 增加等待时间
sleep(2)

# 2. 滚动到元素位置
driver.execute_script("arguments[0].scrollIntoView();", element)

# 3. 使用多种定位方式
try:
    element = driver.find_element(By.ID, "xxx")
except:
    element = driver.find_element(By.NAME, "xxx")
```

### 问题3：输入框输入失败

**解决方案：**
```python
# 1. 确保元素可见
driver.execute_script("arguments[0].scrollIntoView();", input_box)
sleep(0.5)

# 2. 清空后等待
input_box.clear()
sleep(0.5)

# 3. 输入内容
input_box.send_keys("内容")

# 4. 验证输入
value = input_box.get_attribute("value")
print(f"输入框当前值: {value}")
```

### 问题4：按钮点击无效

**原因：**
- 按钮被遮挡
- 页面还在加载
- JavaScript 事件未绑定

**解决方案：**
```python
# 1. 滚动到按钮位置
driver.execute_script("arguments[0].scrollIntoView();", button)
sleep(1)

# 2. 点击
button.click()

# 3. 或使用 JavaScript 点击
driver.execute_script("arguments[0].click();", button)
```

### 问题5：搜索结果页面结构不同

**现象：** 不同搜索方式返回的HTML结构不同

**解决方案：**
```python
# ✅ 使用通用的 XPATH，不依赖特定 class
"//a[contains(@href,'goods.php')]"

# ✅ 或同时匹配多种 class
"//div[@class='goods_item' or @class='goodsItem']//a"

# ✅ 或使用 contains
"//div[contains(@class,'goods')]//a"
```

---

## 📊 元素定位最佳实践

### 优先级顺序

1. **ID** - 最快最稳定
2. **NAME** - 常用于表单
3. **LINK_TEXT** - 适合链接
4. **XPATH** - 最灵活但较慢
5. **CSS_SELECTOR** - 快速但语法复杂

### XPATH 使用技巧

```python
# ✅ 好的 XPATH - 基于属性
"//input[@id='username']"
"//a[contains(@href,'user.php')]"
"//div[@class='box']//a"

# ❌ 不好的 XPATH - 绝对路径
"/html/body/div[1]/div[2]/a"
```

### 多种定位方式备用

```python
try:
    element = driver.find_element(By.ID, "xxx")
except:
    try:
        element = driver.find_element(By.NAME, "xxx")
    except:
        element = driver.find_element(By.XPATH, "//input[@id='xxx']")
```

---

## 📄 文档编写规范

### 实验总结.md 必须包含

1. **实验概述**
   - 实验目标
   - 实验环境
   - 实验时间

2. **实验内容**
   - 实验步骤
   - 实验结果

3. **文件说明**
   - 文件列表
   - 文件用途

4. **关键技术点**
   - 技术说明
   - 代码示例

5. **问题与解决**
   - 遇到的问题
   - 解决方案
   - 原因分析

6. **经验总结**
   - 学到的知识
   - 最佳实践
   - 注意事项

7. **运行方式**
   - 运行命令
   - 前置条件

8. **实验结论**
   - 完成情况
   - 评价

### README.md 必须包含

1. **文件说明**
2. **快速开始**
3. **故障排查**
4. **学习重点**

---

## 🔧 调试技巧

### 1. 添加详细日志

```python
print("✅ 步骤X: 操作描述")
print(f"   当前URL: {driver.current_url}")
print(f"   元素值: {element.get_attribute('value')}")
```

### 2. 保存截图

```python
driver.save_screenshot("实验模块二/实验XX/步骤X截图.png")
```

### 3. 打印页面信息

```python
print(f"页面标题: {driver.title}")
print(f"当前URL: {driver.current_url}")
```

### 4. 验证操作结果

```python
# 输入后验证
input_value = element.get_attribute("value")
print(f"输入框当前值: {input_value}")

# 点击后验证
current_url = driver.current_url
print(f"跳转后URL: {current_url}")
```

---

## 🚀 Git 提交规范

### 提交前检查清单

- [ ] 代码能正常运行
- [ ] 所有步骤都成功
- [ ] 文档已完成
- [ ] 截图已保存
- [ ] 辅助脚本已创建
- [ ] .gitignore 已更新

### 提交信息格式

```bash
# 完成实验
git commit -m "完成实验XX：实验标题"

# 修复问题
git commit -m "修复实验XX：问题描述"

# 优化代码
git commit -m "优化实验XX：优化内容"
```

### .gitignore 必须包含

```gitignore
# Python
venv/
__pycache__/
*.pyc

# Selenium
*.log
screenshots/
chromedriver.exe

# ECShop
ECShop/

# 临时文件
*.tmp
screenshot.png
```

---

## 🎓 ECShop 特殊说明

### 系统信息

- **版本：** ECShop V2.7.1 GBK (2009)
- **技术栈：** PHP 5.3 + MySQL 5.5 + Apache 2.2
- **访问地址：** `http://localhost/upload/`
- **后台地址：** `http://localhost/upload/admin/`

### 测试账号

**前台测试账号：**
- 用户名：vip
- 密码：vip

**后台管理账号：**
- 用户名：admin
- 密码：admin123

### 注意事项

1. **老系统兼容性**
   - HTML 结构可能不规范
   - JavaScript 可能有兼容性问题
   - 页面加载可能较慢

2. **中文编码**
   - 系统使用 GBK 编码
   - 必须使用 JavaScript 输入中文
   - URL 中的中文需要编码

3. **页面结构**
   - 不同搜索方式返回的HTML可能不同
   - class 名称可能不一致（goods_item vs goodsItem）
   - 使用通用的 XPATH 定位

---

## 💡 最佳实践总结

### DO（推荐做法）

✅ 使用 Chrome + ChromeDriver
✅ 添加文件编码声明
✅ 使用 JavaScript 输入中文
✅ 增加适当的等待时间
✅ 滚动到元素可见位置
✅ 验证每个操作的结果
✅ 使用多种定位方式备用
✅ 添加详细的日志输出
✅ 保存截图证据
✅ 编写完整的文档
✅ 及时提交 Git

### DON'T（避免做法）

❌ 不要使用 Firefox
❌ 不要用 send_keys 输入中文
❌ 不要依赖绝对路径 XPATH
❌ 不要依赖特定的 class 名称
❌ 不要吞掉异常不打印
❌ 不要跳过文档编写
❌ 不要忘记验证结果

---

## 📚 参考资料

- [Selenium 官方文档](https://www.selenium.dev/documentation/)
- [Python Selenium 教程](https://selenium-python.readthedocs.io/)
- [XPATH 教程](https://www.w3schools.com/xml/xpath_intro.asp)

---

**最后更新：** 2026年5月12日
**适用范围：** 软件测试实验模块二（Selenium 自动化测试）
