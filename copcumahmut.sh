#!/bin/bash

echo "Çöpçü Mahmut 1.0"
echo "Temizlik başlatılıyor.."

rm -rf ~/.cache/* /var/cache/*
echo Cache dosyaları temizlendi.

rm -rf ~/.local/share/Trash/*
echo "Geri dönüşüm kutusu boşaltıldı."

rm -rf /tmp/*
echo "TMP dizini temizlendi."

echo "Temizlik Tamamlandı, Çöpçü Mahmut İyi Günler diler."