import random
from backend.scoring import engagement_risk_points, risk_verdict

def fetch_instagram_data(username):
    followers = random.randint(5_000, 5_000_000)

    likes = [random.randint(int(0.01 * followers), int(0.08 * followers)) for _ in range(10)]
    comments = [random.randint(10, 500) for _ in range(10)]

    return {
        "followers": followers,
        "likes": likes,
        "comments": comments
    }

def calculate_engagement(data):
    avg_likes = sum(data["likes"]) / len(data["likes"])
    avg_comments = sum(data["comments"]) / len(data["comments"])

    engagement = ((avg_likes + avg_comments) / data["followers"]) * 100

    score = engagement_risk_points(engagement)
    verdict = risk_verdict(score)

    data["risk_score"] = score
    data["verdict"] = verdict

    return round(engagement, 2)
