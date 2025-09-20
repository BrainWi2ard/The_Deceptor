from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/send_phish")
async def send_phish(request: Request):
    data = await request.json()
    target = data.get("target")
    pretext = data.get("pretext")
    return {"status": "sent", "target": target, "pretext": pretext}

@app.post("/request_money_transfer")
async def request_money(request: Request):
    data = await request.json()
    target = data.get("target")
    return {"message": f"{target}, can you send me some money urgently?"}