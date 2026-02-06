FROM python:3.10-slim

WORKDIR /app

# Встановлюємо необхідні бібліотеки
RUN pip install --no-cache-dir fastapi uvicorn

# Копіюємо всі файли проекту
COPY . .

# Відкриваємо порт
EXPOSE 8000

# Запускаємо сервер
CMD ["python", "main.py"]