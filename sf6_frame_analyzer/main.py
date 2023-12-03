from typing import Annotated
import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/")
async def upload_video(file: UploadFile):
    return {"filename": file.filename}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("sf6_frame_analyzer.main:app", host="0.0.0.0", port=8000, reload=True)
