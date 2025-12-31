import instaloader
from backend.scoring import engagement_risk_points, risk_verdict

def fetch_instagram_data(username):
    L = instaloader.Instaloader(download_pictures=False,
                                download_videos=False,
                                download_comments=False,
                                save_metadata=False,
                                quiet=True)

    profile = instaloader.Profile.from_username(L.context, username)

    likes = []
    comments = []

    for post in profile.get_posts():
        likes.append(post.likes)
        comments.append(post.comments)
        if len(likes) >= 10:
            break

    return {
        "followers": profile.followers,
        "likes": likes,
        "comments": comments
    }

def calculate_engagement(data):
    if not data["likes"]:
        return 0

    avg_likes = sum(data["likes"]) / len(data["likes"])
    avg_comments = sum(data["comments"]) / len(data["comments"])
    engagement = ((avg_likes + avg_comments) / data["followers"]) * 100

    data["risk_score"] = engagement_risk_points(engagement)
    data["verdict"] = risk_verdict(data["risk_score"])

    return round(engagement, 2)
