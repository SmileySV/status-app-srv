FROM python:3.10-slim

WORKDIR /app

# Спробуємо оновити pip і встановити бібліотеки з довшим таймаутом
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 fastapi uvicorn python-multipart

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]