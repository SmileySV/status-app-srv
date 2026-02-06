#!/bin/sh

# Шлях всередині контейнера до змонтованої папки
DATA_DIR="/app/data"
DATA_FILE="$DATA_DIR/data.json"
TEMPLATE_FILE="/app/data_template.json"

echo ">>> Checking data directory and file..."

# Створюємо файл, якщо його немає в папці
if [ ! -s "$DATA_FILE" ]; then
    echo ">>> Initializing data.json from template..."
    cp "$TEMPLATE_FILE" "$DATA_FILE"
    chmod 666 "$DATA_FILE"
else
    echo ">>> Data file exists and is not empty."
fi

# Запускаємо Python
exec python main.py