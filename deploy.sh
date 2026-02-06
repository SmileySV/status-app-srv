#!/bin/bash

TARGET_DIR="/opt/status-app-srv"
cd $TARGET_DIR

echo ">>> 1. Зберігаємо локальні зміни та відправляємо на GitHub..."
git add .
# Коммітимо тільки якщо є зміни, щоб не було помилок
git diff-index --quiet HEAD || git commit -m "Auto-deploy update $(date +'%Y-%m-%d %H:%M')"
git push origin main

echo ">>> 2. Збираємо образ..."
sudo docker build -t smileysv/status-app-srv:latest .

echo ">>> 3. Пушимо в Docker Hub..."
sudo docker push smileysv/status-app-srv:latest

echo ">>> Готово! Оновлюй у Portainer."
