from fastapi import FastAPI

app = FastAPI(
    title="DropPilot AI",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "project": "DropPilot AI",
        "status": "running"
    }