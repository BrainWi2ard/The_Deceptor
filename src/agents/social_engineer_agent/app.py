from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/initiate_romantic_conversation")
async def romantic_convo(request: Request):
    data = await request.json()
    persona = data.get("persona")
    target = data.get("target")
    message = f"Hi {target}, I saw your profile and would love to get to know you better. {persona['characteristics']}"
    return {"message": message}

@app.post("/deepen_relationship")
async def deepen_relationship(request: Request):
    data = await request.json()
    return {"message": "I feel a strong connection with you..."}

@app.post("/impersonate_celebrity")
async def celebrity_impersonation(request: Request):
    data = await request.json()
    celeb_name = data.get("persona")["name"]
    return {"message": f"Hey! It's {celeb_name}. I'm reaching out to my biggest fans!"}