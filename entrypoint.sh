#!/bin/sh

# Шлях до файлу, який примонтований через Volume
DATA_FILE="/app/data.json"
# Шлях до шаблону, який ми зашили в образ
TEMPLATE_FILE="/app/data_template.json"

echo ">>> Checking data file..."

# Якщо файл не існує або має розмір 0 (Docker часто створює порожній файл при монтуванні)
if [ ! -s "$DATA_FILE" ]; then
    echo ">>> Data file is empty or missing. Initializing from template..."
    cp "$TEMPLATE_FILE" "$DATA_FILE"
    # Даємо права, щоб Python міг писати в нього
    chmod 666 "$DATA_FILE"
else
    echo ">>> Data file found and not empty. Skipping initialization."
fi

# Запускаємо основний процес (Python сервер)
echo ">>> Starting FastAPI..."
exec python main.py