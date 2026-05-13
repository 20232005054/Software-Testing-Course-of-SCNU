# 实验14 - 验证码测试

## 📋 实验概述

本实验练习在自动化测试中处理验证码，包括识别验证码、使用万能验证码、截图保存等方法。

## 📁 文件说明

- `实验14_验证码测试.py` - 主实验脚本
- `captcha_screenshots/` - 验证码截图目录（自动创建）
- `README.md` - 本说明文档
- `实验14总结.md` - 实验总结文档

## 🎯 实验目标

1. 了解验证码在Web应用中的作用
2. 掌握验证码的处理方法
3. 学会使用万能验证码进行测试
4. 了解OCR识别验证码的基本原理

## 🚀 快速开始

### 前置条件

1. ECShop系统已启动（http://localhost/upload/）
2. Python环境已配置
3. 已安装selenium和webdriver-manager
4. **已安装ddddocr**（用于验证码识别）

### 安装OCR库

```bash
# 方法1：使用批处理文件
双击运行：安装OCR库.bat

# 方法2：命令行安装
cd 实验模块二\实验14
..\..\venv\Scripts\pip.exe install ddddocr
```

### 运行实验

```bash
cd 实验模块二\实验14
..\..\venv\Scripts\python.exe 实验14_验证码测试.py
```

**注意：**
- 如果未安装ddddocr，脚本会使用占位符验证码（会导致提交失败）
- 安装ddddocr后可以自动识别验证码

## 📝 实验步骤

1. 打开P806商品详情页（`goods.php?id=24`）
2. 输入E-mail：`a@b.com`
3. 输入评论内容：`It's excellent`
4. 识别验证码图片（截图保存）
5. 输入正确的验证码（使用万能验证码`0`）
6. 点击"提交评论"按钮

## 🔑 关键技术点

### 1. 验证码的作用

- 防止自动化脚本攻击
- 防止恶意注册、登录
- 防止垃圾评论、刷票
- 保护系统安全

### 2. 验证码处理方法

#### 方法1：万能验证码（测试环境）

```python
# ECShop支持万能验证码"0"
captcha_input.send_keys("0")
```

**优点：**
- 简单快速
- 适合测试环境

**缺点：**
- 仅限测试环境
- 生产环境不可用

#### 方法2：截图保存

```python
# 截取验证码图片
captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")
captcha_img.screenshot("captcha.png")
```

**用途：**
- 保存测试证据
- 人工识别
- 训练OCR模型

#### 方法3：OCR识别

```python
# 使用pytesseract识别
import pytesseract
from PIL import Image

captcha_img.screenshot("captcha.png")
image = Image.open("captcha.png")
captcha_text = pytesseract.image_to_string(image)
```

**优点：**
- 自动化程度高
- 适合简单验证码

**缺点：**
- 识别率受验证码复杂度影响
- 需要安装OCR引擎

#### 方法4：第三方打码平台

```python
# 使用打码平台API
# 1. 截取验证码图片
# 2. 上传到打码平台
# 3. 获取识别结果
# 4. 输入验证码
```

**优点：**
- 识别率高
- 支持复杂验证码

**缺点：**
- 需要付费
- 响应时间较长

### 3. 查找验证码元素

```python
# 方法1：通过src属性
captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")

# 方法2：通过ID
captcha_img = driver.find_element(By.ID, "captcha_img")

# 方法3：通过alt/title属性
captcha_img = driver.find_element(By.XPATH, "//img[contains(@alt,'验证码')]")
```

### 4. 输入验证码

```python
# 查找验证码输入框
captcha_input = driver.find_element(By.NAME, "captcha")

# 输入验证码
captcha_input.clear()
captcha_input.send_keys("0")
```

## ⚠️ 注意事项

1. **万能验证码**：仅在测试环境使用，生产环境需要真实识别
2. **验证码刷新**：某些验证码点击可刷新，需要重新识别
3. **验证码有效期**：验证码可能有时效性，过期需要刷新
4. **识别准确率**：OCR识别准确率受验证码复杂度影响
5. **法律合规**：使用打码平台需遵守相关法律法规

## 🐛 故障排查

### 问题1：找不到验证码图片

**解决方案：**
```python
# 尝试多种定位方式
try:
    captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")
except:
    try:
        captcha_img = driver.find_element(By.ID, "captcha_img")
    except:
        captcha_img = driver.find_element(By.XPATH, "//img[contains(@alt,'验证码')]")
```

### 问题2：验证码输入后提示错误

**可能原因：**
- 验证码已过期
- 验证码识别错误
- 验证码区分大小写

**解决方案：**
- 使用万能验证码测试
- 刷新验证码重新识别
- 检查大小写

### 问题3：OCR识别率低

**解决方案：**
- 图片预处理（灰度化、二值化、降噪）
- 使用更好的OCR引擎（如ddddocr）
- 训练自定义OCR模型

## 📚 学习重点

### 1. 验证码类型

| 类型 | 特点 | 识别难度 |
|------|------|----------|
| 数字验证码 | 纯数字 | ⭐ |
| 字母验证码 | 纯字母 | ⭐⭐ |
| 混合验证码 | 数字+字母 | ⭐⭐⭐ |
| 算术验证码 | 简单运算 | ⭐⭐ |
| 滑块验证码 | 拖动滑块 | ⭐⭐⭐⭐ |
| 点选验证码 | 点击指定位置 | ⭐⭐⭐⭐ |

### 2. OCR工具对比

| 工具 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| pytesseract | 开源免费 | 识别率一般 | 简单验证码 |
| ddddocr | 识别率高 | 需要训练 | 中等复杂度 |
| 百度OCR | 识别率高 | 需要付费 | 生产环境 |
| 打码平台 | 识别率最高 | 费用较高 | 复杂验证码 |

### 3. 验证码处理策略

```
测试环境：
  ├─ 万能验证码（最优）
  ├─ 关闭验证码功能
  └─ 简化验证码

开发环境：
  ├─ OCR识别
  ├─ 人工输入
  └─ 打码平台

生产环境：
  ├─ 不建议自动化
  └─ 人工测试
```

## 🎓 扩展练习

1. 实现验证码刷新功能
2. 使用pytesseract识别简单验证码
3. 实现验证码识别失败重试机制
4. 对比不同OCR工具的识别率
5. 实现滑块验证码的自动化

## 📖 参考资料

- [pytesseract文档](https://github.com/madmaze/pytesseract)
- [ddddocr文档](https://github.com/sml2h3/ddddocr)
- [Selenium截图文档](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webelement.WebElement.screenshot)
