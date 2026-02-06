from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import json
import uvicorn

app = FastAPI()

# Модель даних для перевірки
class ServerStatus(BaseModel):
    ip: str
    name: str
    date: str
    dev: bool
    status: str

# Ендпоінт для збереження даних
@app.post("/api/save")
async def save_data(data: List[ServerStatus]):
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            # Перетворюємо об'єкти назад у список словників і зберігаємо
            json.dump([item.dict() for item in data], f, ensure_ascii=False, indent=4)
        return {"status": "success", "message": "Дані збережено"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Роздача статичних файлів (твій фронтенд)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)