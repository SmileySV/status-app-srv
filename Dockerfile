FROM python:3.10-slim

WORKDIR /app

# Копіюємо ліби
COPY libs /app/libs

# Встановлюємо ВСЕ, що лежить у папці libs
RUN pip install --no-index --find-links=/app/libs /app/libs/*.whl

# Копіюємо код
COPY . .

EXPOSE 8000

CMD ["python", "main.py"]