# 实验08 - 模拟鼠标和键盘操作

## 实验说明

练习使用ActionChains类模拟鼠标操作和焦点管理。

## 文件列表

- `实验08_鼠标键盘操作.py` - 主实验脚本
- `实验08总结.md` - 实验总结
- `README.md` - 本文档

## 快速开始

```bash
python 实验模块二\实验08\实验08_鼠标键盘操作.py
```

## 核心API

### ActionChains类

```python
from selenium.webdriver.common.action_chains import ActionChains

# 创建对象
actions = ActionChains(driver)

# 鼠标操作
actions.click(element)              # 单击
actions.double_click(element)       # 双击
actions.context_click(element)      # 右键
actions.move_to_element(element)    # 移动到元素
actions.drag_and_drop(src, target)  # 拖拽

# 执行动作（必须调用）
actions.perform()
```

### 焦点管理

```python
# 获取当前焦点元素
current = driver.switch_to.active_element

# Tab键切换焦点
element.send_keys(Keys.TAB)
```

## 实验演示

本实验演示了完整的登录流程：

1. 鼠标点击登录链接
2. 鼠标移动到用户名框并单击
3. 输入用户名
4. Tab键切换到密码框
5. 输入密码
6. Tab键切换到登录按钮
7. 回车登录

## 学习重点

- ActionChains类的使用
- 鼠标操作模拟
- 焦点元素获取和操作
- Tab键切换焦点

---

**实验状态：** ✅ 已完成
