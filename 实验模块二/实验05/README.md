# 实验05 - 浏览器基本操作

## 实验说明

练习浏览器窗口控制和导航操作。

## 文件列表

- `实验05_浏览器基本操作.py` - 主实验脚本
- `实验05总结.md` - 实验总结
- `README.md` - 本文档

## 快速开始

```bash
python 实验模块二\实验05\实验05_浏览器基本操作.py
```

## 核心API

### 窗口控制

```python
# 大小
driver.set_window_size(width, height)
driver.get_window_size()

# 位置
driver.set_window_position(x, y)
driver.get_window_position()

# 状态
driver.minimize_window()
driver.maximize_window()
```

### 导航控制

```python
driver.get(url)      # 访问
driver.back()        # 后退
driver.forward()     # 前进
driver.refresh()     # 刷新
```

### 页面信息

```python
driver.title         # 标题
driver.current_url   # URL
```

## 学习重点

- 窗口大小和位置控制
- 浏览器导航操作
- 页面信息获取

---

**实验状态：** ✅ 已完成
