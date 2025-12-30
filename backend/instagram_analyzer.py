import json
import os
from backend.scoring import (  # type: ignore
    engagement_risk_points,
    follower_spike_points,
    comment_repetition_points,
    risk_verdict
)

import instaloader # type: ignore

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "follower_history.json")

def fetch_instagram_data(username):
    try:
        for c in post.get_comments():
            comment_texts.append(c.text.lower())
    except:
        pass    

    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)

    followers = profile.followers
    likes = []
    comments = []
    comment_texts = []

    for post in profile.get_posts():
        likes.append(post.likes)
        comments.append(post.comments)

        try:
            for c in post.get_comments():
                comment_texts.append(c.text.lower())
        except:
            pass


        if len(likes) == 10:
            break

    return {
        "followers": followers,
        "likes": likes,
        "comments": comments,
        "comment_texts": comment_texts
    }



def calculate_engagement(data):
    if len(data["likes"]) == 0:
        return 0
    avg_likes = sum(data["likes"]) / len(data["likes"])
    avg_comments = sum(data["comments"]) / len(data["comments"])
    engagement = ((avg_likes + avg_comments) / data["followers"]) * 100
    return round(engagement, 2)


def load_follower_history():
    if not os.path.exists(data_path):
        return {}
    with open(data_path, "r") as f:
        return json.load(f)

def save_follower_history(history):
    with open(data_path, "w") as f:
        json.dump(history, f)

def calculate_comment_repetition(comments):
    total = len(comments)
    if total == 0:
        return 0
    unique = len(set(comments))
    repetition_ratio = (total - unique) / total
    return round(repetition_ratio, 2)


if __name__ == "__main__":
    username = input("enter instagram username: ")
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
    repetition_ratio = calculate_comment_repetition(data["comment_texts"])
    comment_points = comment_repetition_points(repetition_ratio)
    total_score = engagement_points + spike_points + comment_points
    

    print("\n--- engagetruth analysis report ---")
    print("username:", username)
    print("followers:", data["followers"])
    print("engagement rate:", engagement, "%")
    print("comment repetition ratio:", repetition_ratio)
    print("risk score:", total_score)
    print("final verdict:", verdict)
    print("----------------------------------\n")



