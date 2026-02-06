FROM python:3.10-slim

WORKDIR /app

# Копіюємо ліби
COPY libs /app/libs

# Встановлюємо, додавши pydantic явно
RUN pip install --no-index --find-links=/app/libs fastapi uvicorn python-multipart pydantic

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]