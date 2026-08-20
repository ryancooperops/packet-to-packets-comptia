#!/bin/bash
# Basic Network Connection Checker for Security+ Labs

TARGET=${1:-"127.0.0.1"}
PORTS=(22 80 443 3389)

echo "=========================================="
echo "CompTIA Security+ Lab: Scanning $TARGET"
echo "=========================================="

for PORT in "${PORTS[@]}"; do
    (echo >/dev/tcp/$TARGET/$PORT) >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "[+] Port $PORT is OPEN"
    else
        echo "[-] Port $PORT is CLOSED"
    fi
done
