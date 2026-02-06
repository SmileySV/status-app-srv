import json
import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ServerStatus(BaseModel):
    ip: str
    name: str
    date: str
    dev: bool
    status: str

DATA_FILE = "data.json"

@app.post("/api/save")
async def save_data(data: List[ServerStatus]):
    try:
        json_data = [item.dict() for item in data]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print("✅ Data saved successfully")
        return {"status": "success"}
    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ПРІОРИТЕТНІ РОУТИ ДЛЯ HTML
@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.get("/setStatus.html")
async def read_admin():
    return FileResponse("setStatus.html")

# ВСЕ ІНШЕ (data.json, стилі і т.д.)
# directory="." означає поточну папку /app всередині контейнера
app.mount("/", StaticFiles(directory="."), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)