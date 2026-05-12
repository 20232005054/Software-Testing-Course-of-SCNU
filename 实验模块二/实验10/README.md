# 实验10 - 切换浏览器窗口

## 📖 实验说明

本实验练习使用Selenium切换浏览器窗口（标签页），包括获取窗口句柄、切换窗口、关闭窗口等操作。

## 📂 文件列表

- `实验10_切换浏览器窗口.py` - 主实验脚本
- `查找首页元素.py` - 辅助脚本：查找首页元素
- `查找论坛页面元素.py` - 辅助脚本：查找论坛页面元素
- `实验10总结.md` - 详细的实验总结文档
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
cd "d:\学习资料\大三下\软件测试\实验模块二\实验10"

# 运行脚本
python 实验10_切换浏览器窗口.py
```

### 3. 观察执行过程

脚本会自动执行以下操作：
1. 打开ECShop首页
2. 点击注册按钮
3. 点击用户协议（打开新窗口）
4. 保存原始窗口句柄
5. 切换到新窗口
6. 在新窗口中点击链接
7. 打开EC论坛（第三个窗口）
8. 关闭EC论坛窗口
9. 切换回原始窗口
10. 输入用户名

## 🔧 故障排查

### 问题1：注册按钮找不到

**错误信息：**
```
NoSuchElementException: no such element: Unable to locate element: {"method":"link text","selector":"注册"}
```

**解决方法：**
- 注册按钮是图片链接，使用XPATH定位
- 已在脚本中修复

### 问题2：窗口切换失败

**可能原因：**
- 新窗口还在加载
- 窗口句柄不正确

**解决方法：**
```python
# 增加等待时间
sleep(3)

# 确认窗口已打开
print(f"窗口数量: {len(driver.window_handles)}")
```

### 问题3：关闭窗口后无法操作

**可能原因：**
- 关闭窗口后没有切换到其他窗口

**解决方法：**
```python
# 关闭窗口后立即切换
driver.close()
driver.switch_to.window(driver.window_handles[0])
```

## 📚 学习重点

### 1. 窗口句柄操作

```python
# 获取当前窗口句柄
current_handle = driver.current_window_handle

# 获取所有窗口句柄
all_handles = driver.window_handles

# 切换到指定窗口
driver.switch_to.window(handle)

# 关闭当前窗口
driver.close()
```

### 2. 窗口切换模式

| 操作 | 方法 | 说明 |
|------|------|------|
| 获取当前窗口 | current_window_handle | 返回当前窗口句柄 |
| 获取所有窗口 | window_handles | 返回所有窗口句柄列表 |
| 切换窗口 | switch_to.window(handle) | 切换到指定窗口 |
| 关闭窗口 | close() | 关闭当前窗口 |
| 退出浏览器 | quit() | 关闭所有窗口并退出 |

### 3. 常用操作模式

**模式1：切换到最新窗口**
```python
# 新窗口通常是列表的最后一个
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
```

**模式2：保存并切换回原窗口**
```python
# 保存原始窗口
original = driver.current_window_handle

# 打开新窗口并操作
# ...

# 切换回原窗口
driver.switch_to.window(original)
```

**模式3：查找特定窗口**
```python
# 遍历所有窗口
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "目标URL" in driver.current_url:
        # 找到目标窗口
        break
```

### 4. 注意事项

- ⚠️ 必须先切换到窗口才能操作该窗口的元素
- ⚠️ 关闭窗口后要立即切换到其他窗口
- ⚠️ 新窗口打开需要时间，要增加等待
- ⚠️ 窗口句柄在浏览器会话中是唯一的
- ⚠️ close()关闭当前窗口，quit()关闭所有窗口

## 💡 实用技巧

### 1. 等待新窗口打开

```python
# 记录打开前的窗口数量
before_count = len(driver.window_handles)

# 点击打开新窗口的链接
link.click()

# 等待新窗口打开
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > before_count
)
```

### 2. 安全地关闭窗口

```python
# 确保不是最后一个窗口
if len(driver.window_handles) > 1:
    driver.close()
    # 切换到剩余的第一个窗口
    driver.switch_to.window(driver.window_handles[0])
```

### 3. 识别窗口

```python
# 通过URL识别
if "user.php" in driver.current_url:
    print("这是用户中心窗口")

# 通过标题识别
if "用户协议" in driver.title:
    print("这是用户协议窗口")
```

## 📖 相关文档

- [Selenium官方文档 - Windows](https://www.selenium.dev/documentation/webdriver/interactions/windows/)
- [实验10总结.md](./实验10总结.md) - 详细的实验总结

## ✅ 实验检查清单

- [ ] 脚本能正常运行
- [ ] 成功打开多个窗口
- [ ] 成功获取窗口句柄
- [ ] 成功切换窗口
- [ ] 成功关闭指定窗口
- [ ] 成功切换回原窗口
- [ ] 所有步骤都有日志输出
- [ ] 异常处理完善

## 🎯 扩展练习

1. **练习1：窗口计数**
   - 在每个步骤后打印当前窗口数量
   - 验证窗口打开和关闭是否正确

2. **练习2：窗口信息**
   - 打印每个窗口的URL和标题
   - 创建窗口信息表格

3. **练习3：批量关闭**
   - 关闭除原始窗口外的所有窗口
   - 使用循环实现

4. **练习4：窗口切换优化**
   - 使用显式等待等待窗口打开
   - 添加窗口切换失败的重试机制

---

**最后更新：** 2026年5月12日
