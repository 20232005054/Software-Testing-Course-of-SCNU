# 实验12 - 下拉列表操作

## 📋 实验概述

本实验练习使用Selenium的Select类操作下拉列表（`<select>`元素），包括选择、取消选择、获取选中选项等操作。

## 📁 文件说明

- `实验12_下拉列表操作.py` - 主实验脚本
- `README.md` - 本说明文档
- `实验12总结.md` - 实验总结文档

## 🎯 实验目标

1. 掌握Select类的基本使用方法
2. 学会通过索引、值、文本选择选项
3. 掌握取消选择的方法
4. 学会获取已选中的选项

## 🚀 快速开始

### 前置条件

1. ECShop系统已启动（http://localhost/upload/）
2. 后台账号：admin / admin123
3. Python环境已配置
4. 已安装selenium和webdriver-manager

### 运行实验

```bash
cd 实验模块二/实验12
python 实验12_下拉列表操作.py
```

## 📝 实验步骤

1. 打开ECShop后台页面
2. 登录后台（admin/admin123，验证码0）
3. 点击"进入管理中心"，等待8秒
4. 点击"个人设置"，等待5秒
5. 选中右侧下拉列表的第1-6个选项，等待5秒
6. 取消特定选项（商品管理、第2个、特定value），等待5秒
7. 取消右侧下拉列表所有选项
8. 选择"商品类型"选项，等待3秒
9. 检查并点击"增加"按钮（如果可用），等待5秒
10. 选中左侧下拉列表的最后两个选项，等待3秒
11. 打印左侧下拉列表所有已选中选项的文本
12. 打印第一个已选中选项的文本

## 🔑 关键技术点

### Select类的使用

```python
from selenium.webdriver.support.ui import Select

# 创建Select对象
select_element = driver.find_element(By.NAME, "nav[]")
select = Select(select_element)

# 选择选项
select.select_by_index(0)           # 通过索引
select.select_by_value("value")     # 通过value属性
select.select_by_visible_text("文本") # 通过可见文本

# 取消选择（仅多选列表）
select.deselect_by_index(0)
select.deselect_by_value("value")
select.deselect_by_visible_text("文本")
select.deselect_all()               # 取消所有

# 获取选项
all_options = select.options                    # 所有选项
selected_options = select.all_selected_options  # 所有已选中选项
first_selected = select.first_selected_option   # 第一个已选中选项
```

### Frame切换

```python
# 切换到header frame
driver.switch_to.frame("header-frame")

# 切换到main frame
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")
```

### 检查按钮状态

```python
button = driver.find_element(By.XPATH, "//input[@value='增加']")
is_enabled = button.is_enabled()
if is_enabled:
    button.click()
```

## ⚠️ 注意事项

1. **多选列表**：ECShop的个人导航设置使用多选下拉列表（`<select multiple>`）
2. **Frame切换**：后台页面使用frameset布局，需要切换到对应frame
3. **等待时间**：操作后需要适当等待，确保页面更新
4. **选项索引**：索引从0开始，第1个选项的索引是0
5. **取消选择**：deselect方法仅适用于多选列表

## 🐛 故障排查

### 问题1：找不到下拉列表

**解决方案：**
- 确认已切换到正确的frame
- 检查元素的name或id属性
- 使用XPATH定位多选列表：`//select[@multiple]`

### 问题2：选择选项失败

**解决方案：**
- 确认选项存在（检查options列表）
- 使用正确的选择方法（索引/值/文本）
- 对于多选列表，先deselect_all()再选择

### 问题3：获取不到已选中选项

**解决方案：**
- 确认选项已成功选中
- 使用all_selected_options获取所有已选中选项
- 检查是否在正确的Select对象上操作

## 📚 学习重点

1. **Select类的三种选择方法**
   - by_index：适合按位置选择
   - by_value：适合已知value属性
   - by_visible_text：最直观，适合已知显示文本

2. **多选列表的特殊操作**
   - deselect_all()：清空所有选择
   - all_selected_options：获取多个已选中选项

3. **选项的访问方式**
   - options：所有选项列表
   - options[-1]：最后一个选项
   - options[-2]：倒数第二个选项

4. **Frame操作**
   - 后台系统常用frameset布局
   - 操作前必须切换到正确的frame

## 🎓 扩展练习

1. 尝试选择所有奇数位置的选项
2. 实现选项的批量选择和取消
3. 打印所有选项的text和value
4. 实现选项的条件筛选和选择

## 📖 参考资料

- [Selenium Select类文档](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.select)
- [HTML Select元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/select)
