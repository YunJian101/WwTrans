#!/bin/sh
# CGI脚本 - 动态获取服务器公网IP并返回更新时间

# 检查环境变量是否显示公网IP，默认为显示
SHOW_PUBLIC_IP="${SHOW_PUBLIC_IP:-true}"

if [ "$SHOW_PUBLIC_IP" != "true" ]; then
    echo "Content-Type: text/plain"
    echo ""
    echo "已禁用"
    exit 0
fi

# 保存IP和时间的文件路径
IP_CACHE_FILE="/tmp/public_ip_cache.txt"

echo "Content-Type: text/plain"
echo ""

# 获取当前时间戳（秒）
CURRENT_TIME=$(date +%s)

# 获取已保存的IP和时间
if [ -f "$IP_CACHE_FILE" ]; then
    CACHED_DATA=$(cat "$IP_CACHE_FILE" 2>/dev/null)
    CACHED_IP=$(echo "$CACHED_DATA" | cut -d'|' -f1 | tr -d '[:space:]')
    CACHED_TIME=$(echo "$CACHED_DATA" | cut -d'|' -f2)
else
    CACHED_IP=""
    CACHED_TIME=""
fi

# 尝试多个 API 获取公网 IP
NEW_IP=""
for API in "https://api.ipify.org" "https://api.ip.sb/ip" "https://ifconfig.me/ip"; do
    NEW_IP=$(curl -s --connect-timeout 3 "$API" 2>/dev/null | tr -d '[:space:]')
    if [ -n "$NEW_IP" ]; then
        break
    fi
done

if [ -z "$NEW_IP" ]; then
    echo "获取失败"
    exit 1
fi

# 对比IP是否变化
if [ "$NEW_IP" != "$CACHED_IP" ]; then
    # IP有变化，保存新IP和当前时间
    echo "$NEW_IP|$CURRENT_TIME" > "$IP_CACHE_FILE"
    printf "%s|%s" "$NEW_IP" "$CURRENT_TIME"
else
    # IP未变化，不写入文件，返回已保存的时间
    if [ -z "$CACHED_TIME" ]; then
        # 首次访问，保存
        echo "$NEW_IP|$CURRENT_TIME" > "$IP_CACHE_FILE"
        printf "%s|%s" "$NEW_IP" "$CURRENT_TIME"
    else
        printf "%s|%s" "$NEW_IP" "$CACHED_TIME"
    fi
fi
