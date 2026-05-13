@echo off
chcp 65001 >nul
echo ========================================
echo 安装OCR验证码识别库
echo ========================================
echo.

echo 正在安装ddddocr...
..\..\venv\Scripts\pip.exe install ddddocr

echo.
echo ========================================
echo 安装完成！
echo ========================================
echo.
echo 现在可以运行 实验14_OCR版本.py 进行自动识别
echo.
pause
