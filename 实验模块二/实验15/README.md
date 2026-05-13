# 实验15：文件上传下载

## 📋 实验概述

本实验测试Selenium自动化处理文件上传和下载的功能。

**实验内容：**
1. **文件上传测试** - 在ECShop前台用户留言中上传附件
2. **文件下载测试** - 从测试网站下载文件到指定目录

## 📁 文件说明

```
实验15/
├── 实验15_1_文件上传.py      # 文件上传测试脚本
├── 实验15_2_文件下载.py      # 文件下载测试脚本
├── README.md                  # 使用说明（本文件）
├── 实验15总结.md              # 实验总结文档
├── 实验15.docx                # 实验要求文档
├── 文件上传结果.png           # 上传测试截图
└── 文件下载结果.png           # 下载测试截图
```

## 🚀 快速开始

### 前置条件

1. **ECShop系统运行**
   - 确保ECShop已安装并运行在 `http://localhost/upload/`
   - 测试账号：用户名 `vip`，密码 `vip`

2. **下载目录准备**
   - 确保 `c:\temp` 目录存在（脚本会自动创建）
   - 上传测试文件 `c:\temp\777.txt` 会自动创建

3. **Python环境**
   - 已安装 selenium
   - 已安装 webdriver-manager

### 运行测试

**方式1：运行单个测试**

```bash
# 测试文件上传
python 实验15_1_文件上传.py

# 测试文件下载
python 实验15_2_文件下载.py
```

**方式2：按顺序运行所有测试**

```bash
python 实验15_1_文件上传.py
python 实验15_2_文件下载.py
```

## 🔍 测试步骤详解

### 测试1：文件上传

1. 打开ECShop前台登录页
2. 输入用户名 `vip`、密码 `vip`
3. 点击"立即登陆"，等待5秒
4. 点击上方"用户中心"，等待3秒
5. 点击左侧"我的留言"，等待3秒
6. 输入主题 `hello`
7. 输入留言内容 `welcome to this world!`
8. 选择文件 `c:\temp\777.txt`（自动创建）
9. 点击"提交"
10. 验证提交结果

### 测试2：文件下载

1. 打开测试网页 `http://sahitest.com/demo/saveAs.htm`
2. 配置Chrome下载目录为 `c:\temp`
3. 点击下载链接 `testsaveas.zip`
4. 等待文件下载完成（最多30秒）
5. 验证文件是否下载成功
6. 检查文件大小

## 🎯 关键技术点

### 1. 文件上传

```python
# 定位文件上传控件（type="file"的input元素）
file_input = driver.find_element(By.NAME, "message_img")

# 使用send_keys发送文件路径
file_path = r"c:\temp\777.txt"
file_input.send_keys(file_path)
```

**注意事项：**
- 文件路径必须是绝对路径
- Windows路径使用原始字符串 `r"路径"` 或双反斜杠 `\\`
- 文件必须存在，否则上传会失败
- 不需要点击"浏览"按钮，直接send_keys即可

### 2. 文件下载

```python
# 配置Chrome下载选项
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": r"c:\temp",  # 下载目录
    "download.prompt_for_download": False,     # 禁用下载提示
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# 启动浏览器时应用配置
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
```

**注意事项：**
- 必须在启动浏览器前配置下载选项
- 下载是异步的，需要等待文件下载完成
- 使用循环检查文件是否存在来判断下载完成

### 3. 等待文件下载完成

```python
# 检查文件是否下载完成
download_file = os.path.join(download_dir, "testsaveas.zip")
max_wait_time = 30  # 最多等待30秒

for i in range(max_wait_time):
    if os.path.exists(download_file):
        print("文件下载完成！")
        break
    else:
        sleep(1)
else:
    print("等待超时")
```

## ⚠️ 常见问题

### 问题1：文件上传失败

**可能原因：**
- 文件路径不正确
- 文件不存在
- 文件上传控件定位错误

**解决方案：**
```python
# 1. 检查文件是否存在
if not os.path.exists(file_path):
    print("文件不存在，正在创建...")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write("测试内容")

# 2. 使用绝对路径
file_path = r"c:\temp\777.txt"  # 使用原始字符串

# 3. 确认元素类型
file_input = driver.find_element(By.NAME, "message_img")
print(file_input.get_attribute("type"))  # 应该是 "file"
```

### 问题2：文件下载失败

**可能原因：**
- 下载目录配置不正确
- 网络问题
- 下载链接失效

**解决方案：**
```python
# 1. 确保下载目录存在
os.makedirs(download_dir, exist_ok=True)

# 2. 增加等待时间
max_wait_time = 60  # 增加到60秒

# 3. 检查下载目录中的文件
files = os.listdir(download_dir)
print(f"下载目录中的文件: {files}")
```

### 问题3：下载目录配置无效

**可能原因：**
- Chrome选项配置在启动浏览器之后
- 路径格式不正确

**解决方案：**
```python
# ✅ 正确：在启动浏览器前配置
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"c:\temp"}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

# ❌ 错误：启动浏览器后无法修改下载目录
driver = webdriver.Chrome()
# 此时配置下载目录无效
```

### 问题4：无法判断下载是否完成

**解决方案：**
```python
# 方法1：检查文件是否存在
while not os.path.exists(download_file):
    sleep(1)

# 方法2：检查.crdownload临时文件
# Chrome下载时会创建.crdownload文件，下载完成后删除
temp_file = download_file + ".crdownload"
while os.path.exists(temp_file):
    sleep(1)

# 方法3：检查文件大小是否稳定
prev_size = 0
while True:
    if os.path.exists(download_file):
        curr_size = os.path.getsize(download_file)
        if curr_size == prev_size and curr_size > 0:
            break  # 文件大小不再变化，下载完成
        prev_size = curr_size
    sleep(1)
```

## 📚 学习重点

### 1. 文件上传原理

- 文件上传使用 `<input type="file">` 元素
- Selenium通过 `send_keys()` 发送文件路径
- 不需要模拟点击"浏览"按钮
- 文件路径必须是绝对路径

### 2. 文件下载原理

- 浏览器下载是异步操作
- 需要配置Chrome选项来控制下载行为
- 下载完成需要通过文件系统检查
- 不同浏览器的下载配置方式不同

### 3. 路径处理

```python
# Windows路径的三种写法
path1 = r"c:\temp\file.txt"      # 原始字符串（推荐）
path2 = "c:\\temp\\file.txt"     # 双反斜杠
path3 = "c:/temp/file.txt"       # 正斜杠（也可以）

# 路径拼接
import os
path = os.path.join("c:\\temp", "file.txt")  # 跨平台
```

### 4. 文件操作

```python
import os

# 检查文件是否存在
os.path.exists(file_path)

# 获取文件大小
os.path.getsize(file_path)

# 创建目录
os.makedirs(dir_path, exist_ok=True)

# 列出目录中的文件
os.listdir(dir_path)
```

## 🎓 实验总结

通过本实验，你将学会：

1. ✅ 使用Selenium自动化文件上传
2. ✅ 配置Chrome浏览器的下载选项
3. ✅ 等待和验证文件下载完成
4. ✅ 处理Windows文件路径
5. ✅ 使用Python进行文件系统操作

## 📖 参考资料

- [Selenium文件上传](https://www.selenium.dev/documentation/webdriver/elements/file_upload/)
- [Chrome下载配置](https://chromedriver.chromium.org/capabilities)
- [Python os模块](https://docs.python.org/3/library/os.html)

---

**最后更新：** 2026年5月13日
