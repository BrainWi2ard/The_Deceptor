from fastapi import FastAPI, Request
import os

app = FastAPI()

SCENARIOS = {
    "bec": "docs/bec_simulation.yaml",
    "romance": "docs/romance_scam.yaml",
    "ceo_fraud": "docs/ceo_fraud.yaml",
    "celebrity_impersonation": "docs/celebrity_impersonation.yaml"
}

@app.post("/get_blueprint")
async def get_blueprint(request: Request):
    data = await request.json()
    scenario = data.get("scenario")
    blueprint_path = SCENARIOS.get(scenario)
    if blueprint_path and os.path.exists(blueprint_path):
        with open(blueprint_path) as f:
            return {"blueprint": f.read()}
    return {"error": "Scenario not found"}