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
echo   关闭 WampServer 服务
echo ========================================
echo.

echo 正在停止 WampServer 的 Apache 服务...
net stop wampapache
if %errorlevel% == 0 (
    echo [成功] wampapache 服务已停止
) else (
    echo [提示] wampapache 服务可能已经停止
)
echo.

echo 正在停止 WampServer 的 MySQL 服务...
net stop wampmysqld
if %errorlevel% == 0 (
    echo [成功] wampmysqld 服务已停止
) else (
    echo [提示] wampmysqld 服务可能已经停止
)
echo.

echo ========================================
echo   WampServer 服务已关闭！
echo ========================================
echo.
pause
