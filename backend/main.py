from fastapi import FastAPI #type: ignore
from fastapi.middleware.cors import CORSMiddleware #type: ignore
from backend.instagram_analyzer import fetch_instagram_data, calculate_engagement
from scoring import engagement_risk_points, follower_spike_points, risk_verdict
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "follower_history.json")

def load_follower_history():
    if not os.path.exists(data_path):
        return {}
    with open(data_path, "r") as f:
        return json.load(f)

def save_follower_history(history):
    with open(data_path, "w") as f:
        json.dump(history, f)

@app.get("/analyze/{username}")
def analyze(username: str):
    data = fetch_instagram_data(username)

    engagement = calculate_engagement(data)
    engagement_points = engagement_risk_points(engagement)

    history = load_follower_history()
    old_followers = history.get(username, 0)

    spike_points = follower_spike_points(old_followers, data["followers"])

    total_score = engagement_points + spike_points
    verdict = risk_verdict(total_score)

    history[username] = data["followers"]
    save_follower_history(history)

    return {
        "username": username,
        "followers": data["followers"],
        "engagement": engagement,
        "risk_score": total_score,
        "verdict": verdict
    }
