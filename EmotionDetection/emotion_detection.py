# emotion_detection.py
def emotion_detector(text_to_analyze):
    """
    Simulated emotion detection for testing without external API.
    Returns fake but valid outputs.
    """
    if not text_to_analyze.strip():
        # Blank input handling
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Simple fake logic for testing
    text_lower = text_to_analyze.lower()
    result = {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.9,
        "sadness": 0.04,
        "dominant_emotion": "joy"
    }

    if "mad" in text_lower:
        result.update({"anger": 0.9, "joy": 0.05, "dominant_emotion": "anger"})
    elif "sad" in text_lower:
        result.update({"sadness": 0.9, "joy": 0.05, "dominant_emotion": "sadness"})
    elif "afraid" in text_lower or "fear" in text_lower:
        result.update({"fear": 0.9, "joy": 0.05, "dominant_emotion": "fear"})
    elif "disgust" in text_lower:
        result.update({"disgust": 0.9, "joy": 0.05, "dominant_emotion": "disgust"})
    
    return result