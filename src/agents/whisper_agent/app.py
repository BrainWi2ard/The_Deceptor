from fastapi import FastAPI, UploadFile, File
import whisper

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    with open("audio.wav", "wb") as f:
        f.write(audio_bytes)
    result = model.transcribe("audio.wav")
    return {"text": result["text"]}
