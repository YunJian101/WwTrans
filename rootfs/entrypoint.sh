#!/bin/sh

# 创建 fcgiwrap 所需目录
mkdir -p /run

# 确保cgi脚本有执行权限
chmod +x /app/web/getip.cgi

# 启动 fcgiwrap
fcgiwrap -f -s unix:/run/fcgiwrap.sock &

# 启动 nginx
nginx -g "daemon off;"
