import json
import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

# Створюємо додаток
app = FastAPI(title="AXAPTA Status API")

# Описуємо структуру даних, які приходять з адмінки
class ServerStatus(BaseModel):
    ip: str
    name: str
    date: str
    dev: bool
    status: str

# Шлях до файлу даних
DATA_FILE = "data.json"

@app.post("/api/save")
async def save_data(data: List[ServerStatus]):
    """
    Приймає масив серверів з адмінки та зберігає їх у data.json.
    Файл data.json примонтований через Docker Volumes до /opt/sas/data.json
    """
    try:
        # Перетворюємо масив моделей Pydantic у список словників
        json_data = [item.dict() for item in data]
        
        # Записуємо у файл
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ Дані успішно оновлено. Отримано записів: {len(json_data)}")
        return {"status": "success", "message": "Дані збережено на сервері"}
    
    except Exception as e:
        print(f"❌ Помилка при збереженні: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Помилка сервера: {str(e)}")

# --- Роздача фронтенду ---

# 1. Спеціальний маршрут для головної сторінки
@app.get("/")
async def read_index():
    from fastapi.responses import FileResponse
    return FileResponse("index.html")

# 2. Спеціальний маршрут для адмінки
@app.get("/setStatus.html")
async def read_admin():
    from fastapi.responses import FileResponse
    return FileResponse("setStatus.html")

# 3. Підключення всіх інших статичних файлів (картинки, json, стилі)
# Важливо: StaticFiles мають бути останніми в списку маршрутів
app.mount("/", StaticFiles(directory="."), name="static")

if __name__ == "__main__":
    print("🚀 Запуск сервера AXAPTA Status на порту 8000...")
    # host 0.0.0.0 обов'язковий для роботи всередині Docker
    uvicorn.run(app, host="0.0.0.0", port=8000)