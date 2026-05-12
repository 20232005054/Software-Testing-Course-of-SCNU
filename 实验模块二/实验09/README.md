# 实验09 - 消息框操作

## 📖 实验说明

本实验练习使用Selenium处理JavaScript消息框（alert、confirm），包括切换到消息框、获取文本、点击确定/取消按钮等操作。

## 📂 文件列表

- `实验09_消息框操作.py` - 主实验脚本
- `实验09总结.md` - 详细的实验总结文档
- `README.md` - 本文件

## 🚀 快速开始

### 1. 确保环境准备就绪

```bash
# 检查ECShop是否运行
# 访问 http://localhost/upload/ 应该能看到首页

# 检查Python环境
python --version

# 检查依赖包
pip list | findstr selenium
```

### 2. 运行实验脚本

```bash
# 进入实验目录
cd "d:\学习资料\大三下\软件测试\实验模块二\实验09"

# 运行脚本
python 实验09_消息框操作.py
```

### 3. 观察执行过程

脚本会自动执行以下操作：
1. 打开ECShop首页
2. 点击搜索按钮触发alert消息框
3. 获取并打印消息框文本
4. 点击确定关闭消息框
5. 搜索P806商品
6. 加入购物车
7. 点击删除触发confirm消息框
8. 获取并打印消息框文本
9. 点击取消关闭消息框

## 🔧 故障排查

### 问题1：找不到消息框

**错误信息：**
```
NoAlertPresentException: no such alert
```

**解决方法：**
- 增加等待时间：`sleep(2)`
- 确认操作确实触发了消息框
- 检查消息框是否已经被关闭

### 问题2：搜索按钮点击无效

**可能原因：**
- 元素定位不准确
- 页面还在加载

**解决方法：**
```python
# 尝试多种定位方式
try:
    search_button = driver.find_element(By.NAME, "imageField")
except:
    search_button = driver.find_element(By.CSS_SELECTOR, "input[type='image']")
```

### 问题3：商品链接找不到

**可能原因：**
- 商品不存在
- 搜索结果页面结构不同

**解决方法：**
- 确认P806商品存在于系统中
- 使用更通用的XPATH定位

## 📚 学习重点

### 1. Alert对象的方法

```python
# 切换到消息框
alert = driver.switch_to.alert

# 获取文本
text = alert.text

# 点击确定
alert.accept()

# 点击取消
alert.dismiss()
```

### 2. 消息框类型

| 类型 | 按钮 | 方法 | 用途 |
|------|------|------|------|
| alert | 确定 | accept() | 提示信息 |
| confirm | 确定、取消 | accept() / dismiss() | 确认操作 |
| prompt | 确定、取消、输入框 | send_keys() / accept() / dismiss() | 获取输入 |

### 3. 处理流程

```
触发消息框 → 等待出现 → 切换到消息框 → 操作消息框 → 关闭消息框 → 继续操作页面
```

### 4. 注意事项

- ⚠️ 消息框出现时，页面其他元素无法操作
- ⚠️ 必须先切换到消息框才能操作
- ⚠️ alert只能accept，不能dismiss
- ⚠️ 操作消息框后要等待其关闭

## 💡 实用技巧

### 1. 等待消息框出现

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 显式等待消息框出现
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
```

### 2. 异常处理

```python
from selenium.common.exceptions import NoAlertPresentException

try:
    alert = driver.switch_to.alert
    print(f"消息框文本: {alert.text}")
    alert.accept()
except NoAlertPresentException:
    print("没有找到消息框")
```

### 3. 验证消息内容

```python
alert = driver.switch_to.alert
alert_text = alert.text

# 断言消息内容
assert "请输入关键字" in alert_text, "消息内容不正确"
alert.accept()
```

## 📖 相关文档

- [Selenium官方文档 - Alerts](https://www.selenium.dev/documentation/webdriver/interactions/alerts/)
- [实验09总结.md](./实验09总结.md) - 详细的实验总结

## ✅ 实验检查清单

- [ ] 脚本能正常运行
- [ ] 成功处理alert消息框
- [ ] 成功处理confirm消息框
- [ ] 成功获取消息框文本
- [ ] 成功点击确定和取消按钮
- [ ] 所有步骤都有日志输出
- [ ] 异常处理完善

---

**最后更新：** 2026年5月12日
