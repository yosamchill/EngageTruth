def engagement_risk_points(engagement):
    if engagement < 1:
        return 70
    if engagement > 15:
        return 50
    return 10

def risk_verdict(score):
    if score <= 30:
        return "likely genuine"
    if score <= 60:
        return "suspicious"
    return "high manipulation risk"
