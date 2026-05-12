# 实验07 - 模拟键盘操作

## 实验说明

练习使用Selenium的Keys类模拟键盘按键操作。

## 文件列表

- `实验07_模拟键盘操作.py` - 主实验脚本
- `实验07总结.md` - 实验总结
- `README.md` - 本文档

## 快速开始

```bash
python 实验模块二\实验07\实验07_模拟键盘操作.py
```

## 核心API

### 导入Keys类

```python
from selenium.webdriver.common.keys import Keys
```

### 常用按键

```python
# 特殊键
Keys.ENTER          # 回车
Keys.TAB            # Tab
Keys.ESCAPE         # Esc
Keys.BACKSPACE      # 退格
Keys.DELETE         # 删除

# 导航键
Keys.HOME           # Home（行首）
Keys.END            # End（行尾）
Keys.ARROW_UP       # 上
Keys.ARROW_DOWN     # 下
Keys.ARROW_LEFT     # 左
Keys.ARROW_RIGHT    # 右

# 组合键
Keys.CONTROL + 'c'  # Ctrl+C
Keys.CONTROL + 'v'  # Ctrl+V
Keys.CONTROL + 'a'  # Ctrl+A
Keys.SHIFT + Keys.ARROW_RIGHT  # Shift+右箭头
```

### 使用方法

```python
# 发送按键
element.send_keys(Keys.ENTER)

# 组合键
element.send_keys(Keys.CONTROL + 'c')

# 多个按键
element.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
element.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
```

## 实验演示

本实验演示了完整的键盘操作流程：

1. 输入文本 → Home键回到行首
2. Shift+右箭头选中文本
3. Ctrl+C复制
4. Ctrl+V粘贴到其他输入框
5. Enter回车换行/提交

## 学习重点

- Keys类的使用
- 组合键的写法
- 复制粘贴操作
- 文本选中技巧
- 回车键在不同元素的行为

---

**实验状态：** ✅ 已完成
