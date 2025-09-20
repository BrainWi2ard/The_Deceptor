from fastapi import FastAPI, UploadFile, File, Form
import uuid, os
from typing import List

app = FastAPI()
AVATAR_DIR = "avatars"
PERSONAS = {}

@app.post("/upload_avatar")
async def upload_avatar(avatar: UploadFile = File(...), name: str = Form(...), characteristics: str = Form(...)):
    persona_id = str(uuid.uuid4())
    path = os.path.join(AVATAR_DIR, f"{persona_id}.jpg")
    with open(path, "wb") as f:
        f.write(await avatar.read())
    PERSONAS[persona_id] = {
        "name": name,
        "characteristics": characteristics,
        "avatar_path": path
    }
    return {"persona_id": persona_id}

@app.get("/get_persona/{persona_id}")
async def get_persona(persona_id: str):
    return PERSONAS.get(persona_id, {})

@app.get("/list_personas")
async def list_personas():
    return PERSONAS