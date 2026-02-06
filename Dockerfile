FROM python:3.10-slim

# Щоб логи відразу виводилися в консоль
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Офлайн встановлення ліб
COPY libs /app/libs
RUN pip install --no-index --find-links=/app/libs fastapi uvicorn python-multipart

# Копіюємо проєкт
COPY . .

EXPOSE 8000

CMD ["python", "main.py"]