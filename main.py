import json
import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Шлях до файлу в змонтованій папці
DATA_FILE = "/app/data/data.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ServerStatus(BaseModel):
    ip: str
    name: str
    date: str
    dev: bool
    status: str

@app.post("/api/save")
async def save_data(data: List[ServerStatus]):
    try:
        json_data = [item.dict() for item in data]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print("✅ Зміни записано в /app/data/data.json")
        return {"status": "success"}
    except Exception as e:
        print(f"❌ Помилка запису: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Цей роут з'єднує фронтенд із реальним файлом у Volume
@app.get("/data.json")
async def get_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data, headers={"Cache-Control": "no-cache"})
    return {"error": "Data file not found"}

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

@app.get("/setStatus.html")
async def read_admin():
    return FileResponse(os.path.join(BASE_DIR, "setStatus.html"))

app.mount("/", StaticFiles(directory=BASE_DIR), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)