# 实验04 - CSS_SELECTOR高级定位

## 📖 实验说明

本实验演示如何使用CSS_SELECTOR选择器定位Web页面元素，实现ECShop留言板功能的自动化测试。

**实验要求：** 所有元素必须使用CSS_SELECTOR选择器进行定位

## 📁 文件列表

| 文件名 | 说明 |
|--------|------|
| `实验04_CSS_SELECTOR定位.py` | 主实验脚本 |
| `查找留言板元素.py` | 辅助工具：查找元素CSS选择器 |
| `查找邮箱字段.py` | 辅助工具：查找所有input元素 |
| `留言板页面源代码.html` | 保存的页面源代码 |
| `实验04总结.md` | 详细的实验总结文档 |
| `README.md` | 本文档 |

## 🚀 快速开始

### 1. 确保环境准备就绪

```bash
# 检查WampServer是否运行
# 访问 http://localhost/upload/ 确认ECShop可访问
```

### 2. 运行实验脚本

```bash
# 进入项目目录
cd d:\学习资料\大三下\软件测试

# 激活虚拟环境
venv\Scripts\activate

# 运行实验
python 实验模块二\实验04\实验04_CSS_SELECTOR定位.py
```

### 3. 查看结果

脚本会自动：
- ✅ 打开Chrome浏览器
- ✅ 访问ECShop首页
- ✅ 进入留言板页面
- ✅ 填写留言表单
- ✅ 提交留言
- ✅ 关闭浏览器

## 🔍 CSS选择器示例

本实验使用的CSS选择器：

```python
# 1. 包含匹配 - 定位留言板链接
a[href*='message']

# 2. 属性匹配 - 定位邮箱输入框
input[name='user_email']

# 3. 多属性组合 - 定位"询问"单选按钮
input[type='radio'][name='msg_type'][value='2']

# 4. 属性匹配 - 定位主题输入框
input[name='msg_title']

# 5. 标签+属性 - 定位留言内容
textarea[name='msg_content']

# 6. 类型+值 - 定位提交按钮
input[type='submit'][value='我要留言']
```

## 💡 关键技术点

### 1. CSS_SELECTOR基本语法

```python
# 标签选择器
By.CSS_SELECTOR, "input"

# ID选择器
By.CSS_SELECTOR, "#element_id"

# 类选择器
By.CSS_SELECTOR, ".class_name"

# 属性选择器
By.CSS_SELECTOR, "input[name='username']"

# 多属性组合
By.CSS_SELECTOR, "input[type='text'][name='email']"

# 包含匹配
By.CSS_SELECTOR, "a[href*='keyword']"
```

### 2. 单选按钮操作

```python
# 获取单选按钮
radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='2']")

# 判断是否选中
if radio.is_selected():
    print("已选中")
else:
    radio.click()  # 选中
```

### 3. 中文输入处理

```python
# ❌ 不要用 send_keys（会乱码）
element.send_keys("中文")

# ✅ 使用 JavaScript
driver.execute_script("arguments[0].value = '中文';", element)
```

## 🐛 故障排查

### 问题1：找不到留言板链接

**解决方案：**
- 确认ECShop首页可以正常访问
- 检查页面是否完全加载
- 增加等待时间 `sleep(2)`

### 问题2：邮箱字段定位失败

**原因：** 字段名称是 `user_email` 不是 `email`

**解决方案：**
```python
# ✅ 正确
input[name='user_email']
```

### 问题3：中文输入显示乱码

**解决方案：**
1. 文件开头添加：`# -*- coding: utf-8 -*-`
2. 使用JavaScript输入中文：
   ```python
   driver.execute_script("arguments[0].value = '中文';", element)
   ```

### 问题4：单选按钮点击无效

**解决方案：**
```python
# 滚动到元素可见
driver.execute_script("arguments[0].scrollIntoView();", radio)
sleep(0.5)
radio.click()

# 验证是否选中
if radio.is_selected():
    print("选中成功")
```

## 📚 学习重点

### CSS_SELECTOR vs XPATH

| 特性 | CSS_SELECTOR | XPATH |
|------|--------------|-------|
| 速度 | ⚡ 更快 | 较慢 |
| 语法 | 简洁 | 复杂 |
| 向上查找 | ❌ | ✅ |
| 文本定位 | ❌ | ✅ |

### 何时使用CSS_SELECTOR

✅ **推荐使用：**
- 通过标签、类、ID定位
- 通过属性定位
- 简单的层级关系
- 性能要求高

❌ **不推荐使用：**
- 需要通过文本内容定位
- 需要向上查找父元素
- 复杂的逻辑判断

### 最佳实践

1. **优先使用唯一属性**
   ```python
   # ✅ 好
   input[name='user_email']
   
   # ❌ 不好
   .inputBg
   ```

2. **组合多个属性**
   ```python
   # ✅ 更准确
   input[type='radio'][name='msg_type'][value='2']
   ```

3. **使用包含匹配**
   ```python
   # ✅ 灵活
   a[href*='message']
   ```

## 🔧 辅助工具使用

### 查找元素工具

```bash
# 查找留言板页面元素
python 实验模块二\实验04\查找留言板元素.py

# 查找所有input元素
python 实验模块二\实验04\查找邮箱字段.py
```

这些工具会：
- 打印所有元素的属性信息
- 建议合适的CSS选择器
- 保存页面源代码供分析

## 📖 详细文档

查看 `实验04总结.md` 获取：
- 完整的实验步骤
- 详细的技术说明
- 问题解决方案
- 经验总结

## ✅ 实验检查清单

- [ ] WampServer已启动
- [ ] ECShop可以访问
- [ ] Python虚拟环境已激活
- [ ] 实验脚本运行成功
- [ ] 所有步骤都执行成功
- [ ] 留言提交成功
- [ ] 浏览器正常关闭

## 🎯 下一步

完成本实验后，继续学习：
- 实验05：更多高级定位技巧
- 实验06：等待机制
- 实验07：页面对象模式

---

**实验完成时间：** 2026年5月12日  
**实验状态：** ✅ 已完成
