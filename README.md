# 软件测试实验项目

## 项目说明
本项目用于软件测试课程的实验练习，主要包含 Selenium 自动化测试相关内容。

## 环境配置

### Python 版本
- Python 3.13.2

### 安装依赖

1. 激活虚拟环境：
```bash
# Windows CMD
venv\Scripts\activate

# Windows PowerShell
venv\Scripts\Activate.ps1
```

2. 安装依赖包：
```bash
pip install -r requirements.txt
```

## 项目结构

```
.
├── 实验模块一/          # 测试计划与测试设计
├── 实验模块二/          # Selenium 自动化测试实验
├── test.py             # 测试脚本
├── requirements.txt    # Python 依赖
└── README.md          # 项目说明
```

## 实验内容

### 模块一：测试计划与测试设计
- Deepseek 工具辅助测试
- 测试计划编写
- 手工测试用例设计

### 模块二：Selenium 自动化测试
- Selenium 基础定位
- XPath 高级定位
- CSS Selector 高级定位
- 自动化测试实战

## 使用说明

运行测试脚本：
```bash
python test.py
```

## 注意事项
- 确保已安装 Chrome 浏览器
- webdriver-manager 会自动下载对应的 ChromeDriver
