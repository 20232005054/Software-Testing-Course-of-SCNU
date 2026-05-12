# 实验13 - 截屏操作

## 📋 实验概述

本实验练习使用Selenium的截屏功能，包括全屏截图和元素截图，掌握在自动化测试中保存测试证据的方法。

## 📁 文件说明

- `实验13_截屏操作.py` - 主实验脚本
- `screenshots/` - 截图保存目录（自动创建）
- `README.md` - 本说明文档
- `实验13总结.md` - 实验总结文档

## 🎯 实验目标

1. 掌握全屏截图方法（`save_screenshot()`）
2. 掌握元素截图方法（`element.screenshot()`）
3. 学会在测试流程中保存截图证据
4. 理解截图在自动化测试中的应用

## 🚀 快速开始

### 前置条件

1. ECShop系统已启动（http://localhost/upload/）
2. 后台账号：admin / admin123
3. 前台账号：vip / vip
4. Python环境已配置
5. 已安装selenium和webdriver-manager

### 运行实验

```bash
cd 实验模块二\实验13
..\..\venv\Scripts\python.exe 实验13_截屏操作.py
```

或双击运行：
```bash
运行实验.bat
```

## 📝 实验步骤

1. 打开后台登录页
2. 输入登录信息（admin/admin123/0），等待3秒，**截屏**
3. 点击"进入管理中心"，等待5秒，**截屏**
4. 对左侧菜单栏进行**元素截屏**
5. 点击"商品列表"，等待3秒，对右侧商品列表区域进行**元素截屏**
6. 点击"夏新N7"的查看按钮，等待3秒，切换到新窗口，**截屏**
7. 点击登录按钮，等待3秒，**截屏**
8. 点击"立即登陆"按钮，等待2秒，**截屏**
9. 确认消息框
10. 输入用户名vip，密码vip
11. 点击"立即登陆"按钮，等待3秒，**截屏**
12. 对包含ECSHOP图标的顶部区域进行**元素截屏**
13. 关闭浏览器

## 🔑 关键技术点

### 1. 全屏截图

```python
# 截取整个浏览器窗口
driver.save_screenshot("screenshot.png")

# 使用绝对路径
import os
screenshot_path = os.path.join("screenshots", "01_登录页面.png")
driver.save_screenshot(screenshot_path)
```

**特点：**
- 截取整个浏览器窗口内容
- 包含所有可见元素
- 文件格式通常为PNG
- 适合记录整体页面状态

### 2. 元素截图

```python
# 截取特定元素
element = driver.find_element(By.ID, "menu")
element.screenshot("menu.png")

# 使用绝对路径
screenshot_path = os.path.join("screenshots", "03_左侧菜单栏.png")
element.screenshot(screenshot_path)
```

**特点：**
- 只截取指定元素的区域
- 更精确，文件更小
- 适合截取特定组件
- 需要元素可见

### 3. 创建截图目录

```python
import os

screenshot_dir = "screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
```

### 4. 截图命名规范

```python
# 使用序号和描述性名称
"01_登录页面.png"
"02_管理中心首页.png"
"03_左侧菜单栏.png"

# 使用时间戳
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
f"screenshot_{timestamp}.png"
```

### 5. 异常处理

```python
try:
    element = driver.find_element(By.ID, "menu")
    element.screenshot("menu.png")
except Exception as e:
    # 元素截图失败，使用全屏截图
    driver.save_screenshot("menu.png")
```

## ⚠️ 注意事项

1. **截图时机**：确保页面加载完成后再截图
2. **元素可见性**：元素截图要求元素在视口内可见
3. **文件路径**：使用`os.path.join()`确保跨平台兼容
4. **目录创建**：截图前确保目录存在
5. **文件命名**：使用有意义的名称，便于识别
6. **文件格式**：推荐使用PNG格式（无损压缩）

## 🐛 故障排查

### 问题1：截图文件为空或黑屏

**原因：**
- 页面还在加载
- 元素不可见
- 浏览器窗口最小化

**解决方案：**
```python
# 1. 增加等待时间
sleep(2)
driver.save_screenshot("screenshot.png")

# 2. 确保窗口最大化
driver.maximize_window()

# 3. 滚动到元素位置
element = driver.find_element(By.ID, "menu")
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(1)
element.screenshot("menu.png")
```

### 问题2：元素截图失败

**原因：**
- 元素不在视口内
- 元素被遮挡
- 元素尺寸为0

**解决方案：**
```python
try:
    element = driver.find_element(By.ID, "menu")
    # 滚动到元素位置
    driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(0.5)
    element.screenshot("menu.png")
except Exception as e:
    print(f"元素截图失败: {e}")
    # 使用全屏截图作为备选
    driver.save_screenshot("menu.png")
```

### 问题3：截图目录不存在

**解决方案：**
```python
import os

screenshot_dir = "screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
    print(f"创建截图目录: {screenshot_dir}")
```

### 问题4：中文路径问题

**解决方案：**
```python
# 使用英文目录名
screenshot_dir = "screenshots"  # ✅ 推荐

# 避免中文目录名
screenshot_dir = "截图"  # ❌ 可能有问题

# 或使用绝对路径
import os
screenshot_dir = os.path.abspath("screenshots")
```

## 📚 学习重点

### 1. 截图方法对比

| 方法 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| `driver.save_screenshot()` | 全屏截图 | 简单，包含所有内容 | 文件较大 |
| `element.screenshot()` | 元素截图 | 精确，文件小 | 需要元素可见 |

### 2. 截图应用场景

1. **测试证据**：记录测试执行过程
2. **错误诊断**：失败时自动截图
3. **报告生成**：在测试报告中插入截图
4. **视觉对比**：UI自动化测试中的基准对比

### 3. 最佳实践

```python
def take_screenshot(driver, name, element=None):
    """
    统一的截图方法
    
    Args:
        driver: WebDriver实例
        name: 截图文件名
        element: 可选，要截图的元素
    """
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
    
    try:
        if element:
            # 元素截图
            driver.execute_script("arguments[0].scrollIntoView();", element)
            sleep(0.5)
            element.screenshot(screenshot_path)
        else:
            # 全屏截图
            driver.save_screenshot(screenshot_path)
        
        print(f"📸 已截屏: {screenshot_path}")
        return screenshot_path
    except Exception as e:
        print(f"❌ 截屏失败: {e}")
        return None

# 使用示例
take_screenshot(driver, "01_登录页面")
menu = driver.find_element(By.ID, "menu")
take_screenshot(driver, "02_菜单", menu)
```

## 🎓 扩展练习

1. 实现失败时自动截图的装饰器
2. 创建带时间戳的截图文件名
3. 实现截图对比功能
4. 生成包含截图的HTML测试报告
5. 实现视频录制功能

## 📖 参考资料

- [Selenium截图文档](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.save_screenshot)
- [Python os.path模块](https://docs.python.org/3/library/os.path.html)
- [PIL/Pillow图像处理](https://pillow.readthedocs.io/)
