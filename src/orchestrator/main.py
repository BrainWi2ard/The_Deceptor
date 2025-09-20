from fastapi import FastAPI, Request, Depends
from jose import JWTError, jwt
import requests

app = FastAPI()

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

@app.post("/orchestrate/")
async def orchestrate(request: Request):
    data = await request.json()
    transcription = requests.post("http://whisper-agent:8000/transcribe/", files={"audio": data["audio"]}).json()
    # Add calls to LLM, TTS, Video, Bridge as needed
    return {"transcription": transcription}
