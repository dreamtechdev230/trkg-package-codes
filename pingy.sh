#!/bin/bash

TARGET="$1"

if [[ -z "$TARGET" ]]; then
    if [[ -f /etc/ping.conf ]]; then
        TARGET=$(cat /etc/ping.conf)
    else
        echo "Kullanım: ping <hedef>"
        exit 1
    fi
fi

echo "Ping atılıyor: $TARGET"
ping -c 4 "$TARGET"
