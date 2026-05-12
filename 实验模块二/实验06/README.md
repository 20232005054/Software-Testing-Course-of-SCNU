# 实验06 - 页面元素基本操作

## 实验说明

练习页面元素的状态判断、属性获取、值修改等操作。

## 文件列表

- `实验06_页面元素基本操作.py` - 主实验脚本
- `查找商品页面元素.py` - 辅助工具
- `实验06总结.md` - 实验总结
- `README.md` - 本文档

## 快速开始

```bash
python 实验模块二\实验06\实验06_页面元素基本操作.py
```

## 核心API

### 元素状态判断

```python
element.is_enabled()   # 是否可用
element.is_selected()  # 是否选中（复选框/单选框）
element.is_displayed() # 是否可见
```

### 属性获取

```python
element.get_attribute('value')  # 获取value属性
element.get_attribute('class')  # 获取class属性
element.text                    # 获取文本内容
```

### 元素操作

```python
element.clear()         # 清空
element.send_keys(text) # 输入
element.click()         # 点击
```

### 文本提取

```python
import re
# 提取数字
match = re.search(r'(\d+)', text)
number = int(match.group(1))

# 从页面源代码查找
page_source = driver.page_source
match = re.search(r'关键字[：:]\s*(\d+)', page_source)
```

## 学习重点

- 元素状态判断（可用/选中/可见）
- 属性获取和文本提取
- 复选框操作
- 正则表达式提取数字

---

**实验状态：** ✅ 已完成
