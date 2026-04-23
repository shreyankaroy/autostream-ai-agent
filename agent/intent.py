def detect_intent(text):
    text = text.lower()

    # HIGH INTENT FIRST
    if any(x in text for x in ["buy", "subscribe", "start", "try", "want", "interested"]):
        return "high_intent"

    elif any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in text for x in ["price", "pricing", "plan", "cost", "feature"]):
        return "pricing"

    return "other"