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
echo   停止 Apache 和 MySQL 服务
echo ========================================
echo.

echo 正在停止 MySQL 8.0 服务...
net stop MySQL80
if %errorlevel% == 0 (
    echo [成功] MySQL80 服务已停止
) else (
    echo [提示] MySQL80 服务可能已经停止或需要管理员权限
)
echo.

echo 正在停止所有 Apache 相关服务...
for /f "tokens=2" %%a in ('sc query state^= all ^| findstr /i "apache"') do (
    echo 发现服务: %%a
    net stop %%a
)
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
echo   服务停止完成！
echo ========================================
echo.
echo 提示：如果提示"拒绝访问"，请右键以管理员身份运行此脚本
echo.
pause
