import json
import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Визначаємо шлях до поточної папки
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

class ServerStatus(BaseModel):
    ip: str
    name: str
    date: str
    dev: bool
    status: str

@app.on_event("startup")
async def startup_event():
    print(f"🚀 Сервер запускається в директорії: {BASE_DIR}")
    print(f"📁 Файли в папці: {os.listdir(BASE_DIR)}")
    if not os.path.exists(os.path.join(BASE_DIR, "index.html")):
        print("❌ УВАГА: index.html не знайдено в робочій директорії!")

@app.post("/api/save")
async def save_data(data: List[ServerStatus]):
    try:
        json_data = [item.dict() for item in data]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        return {"status": "success"}
    except Exception as e:
        print(f"❌ Помилка запису: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_index():
    path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(path):
        return FileResponse(path)
    return {"error": "index.html not found on server"}

@app.get("/setStatus.html")
async def read_admin():
    path = os.path.join(BASE_DIR, "setStatus.html")
    if os.path.exists(path):
        return FileResponse(path)
    return {"error": "setStatus.html not found on server"}

# Роздача статики (для css, js, json)
app.mount("/", StaticFiles(directory=BASE_DIR), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)