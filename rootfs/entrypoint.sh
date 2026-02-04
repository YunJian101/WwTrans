#!/bin/sh

# Create fcgiwrap directory
mkdir -p /run

# Ensure cgi script has execute permission
chmod +x /app/web/getip.cgi

# Create socket directory with proper permissions
mkdir -p /var/run/fcgiwrap
chmod 755 /var/run/fcgiwrap

# Start fcgiwrap with explicit socket path
fcgiwrap -f -s unix:/var/run/fcgiwrap.sock &

# Wait for fcgiwrap socket to be ready
sleep 2

# Check if socket exists
if [ ! -S /var/run/fcgiwrap.sock ]; then
    echo "ERROR: fcgiwrap socket not found"
    exit 1
fi

# Start nginx
nginx -g "daemon off;"
