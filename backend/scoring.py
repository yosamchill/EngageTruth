def engagement_risk_points(engagement):
    if engagement < 1:
        return 40
    if engagement > 15:
        return 25
    return 0

def risk_verdict(score):
    if score <= 30:
        return "likely genuine"
    if score <= 60:
        return "suspicious"
    return "high manipulation risk"

def follower_spike_points(old_followers, new_followers):
    if old_followers == 0:
        return 0
    growth = ((new_followers - old_followers) / old_followers) * 100
    if growth > 10:
        return 30
    return 0

def comment_repetition_points(repetition_ratio):
    if repetition_ratio > 0.4:
        return 30
    if repetition_ratio > 0.25:
        return 15
    return 0
