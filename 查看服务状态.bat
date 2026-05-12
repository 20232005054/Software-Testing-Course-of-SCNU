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
echo   Apache 和 MySQL 服务状态
echo ========================================
echo.

echo [MySQL 8.0 服务状态]
sc query MySQL80 | findstr "STATE"
echo.

echo [WampServer Apache 服务状态]
sc query wampapache | findstr "STATE"
echo.

echo [WampServer MySQL 服务状态]
sc query wampmysqld | findstr "STATE"
echo.

echo ========================================
echo   端口占用情况
echo ========================================
echo.

echo [80 端口占用情况 - Apache]
netstat -ano | findstr ":80 "
echo.

echo [3306 端口占用情况 - MySQL]
netstat -ano | findstr ":3306 "
echo.

echo ========================================
pause
