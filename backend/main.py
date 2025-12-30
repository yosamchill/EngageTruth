from fastapi import FastAPI, HTTPException
from backend.instagram_analyzer import fetch_instagram_data, calculate_engagement

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "engagetruth api is live",
        "usage": "/analyze/{instagram_username}"
    }

@app.get("/analyze/{username}")
def analyze(username: str):
    try:
        data = fetch_instagram_data(username)
        if not data:
            raise Exception("data fetch failed")

        engagement = calculate_engagement(data)

        return {
            "username": username,
            "followers": data["followers"],
            "engagement": engagement,
            "risk_score": data.get("risk_score", 0),
            "verdict": data.get("verdict", "unknown")
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"analysis failed: {str(e)}"
        )
