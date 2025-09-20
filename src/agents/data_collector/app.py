from fastapi import FastAPI, Request

app = FastAPI()

logs = []

@app.post("/log_and_report")
async def log_and_report(request: Request):
    entry = await request.json()
    logs.append(entry)
    return {"report": logs}