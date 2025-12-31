from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend.instagram_analyzer import fetch_instagram_data, calculate_engagement

app = FastAPI()

# serve static files (css, js)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# homepage (UI)
@app.get("/")
def serve_ui():
    return FileResponse("frontend/index.html")

# api endpoint
@app.get("/analyze/{username}")
def analyze(username: str):
    data = fetch_instagram_data(username)
    engagement = calculate_engagement(data)

    return {
        "username": username,
        "followers": data["followers"],
        "engagement": engagement,
        "risk_score": data.get("risk_score", 0),
        "verdict": data.get("verdict", "likely genuine")
    }
