@echo off
chcp 65001 >nul

:: 检查管理员权限
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在请求管理员权限...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo ========================================
echo   启动 WampServer 服务
echo ========================================
echo.

echo 正在启动 WampServer 的 Apache 服务...
net start wampapache
if %errorlevel% == 0 (
    echo [成功] wampapache 服务已启动
) else (
    echo [失败] wampapache 服务启动失败
)
echo.

echo 正在启动 WampServer 的 MySQL 服务...
net start wampmysqld
if %errorlevel% == 0 (
    echo [成功] wampmysqld 服务已启动
) else (
    echo [失败] wampmysqld 服务启动失败
)
echo.

echo ========================================
echo   服务启动完成！
echo ========================================
echo.
echo 请检查右下角托盘图标，绿色 W 表示启动成功
echo 然后访问: http://localhost/upload/install/index.php
echo.
pause
