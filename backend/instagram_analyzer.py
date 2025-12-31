import hashlib
from backend.scoring import engagement_risk_points, risk_verdict

def _seed_from_username(username: str):
    h = hashlib.sha256(username.encode()).hexdigest()
    return int(h[:8], 16)

def fetch_instagram_data(username):
    seed = _seed_from_username(username)

    # realistic follower buckets
    if seed % 4 == 0:
        followers = 8_000 + (seed % 20_000)
    elif seed % 4 == 1:
        followers = 50_000 + (seed % 150_000)
    elif seed % 4 == 2:
        followers = 300_000 + (seed % 700_000)
    else:
        followers = 1_000_000 + (seed % 5_000_000)

    likes = []
    comments = []

    for i in range(10):
        like_ratio = 0.015 + ((seed + i) % 30) / 1000   # 1.5% – 4.5%
        comment_ratio = 0.0003 + ((seed + i) % 10) / 10000

        likes.append(int(followers * like_ratio))
        comments.append(int(followers * comment_ratio))

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
