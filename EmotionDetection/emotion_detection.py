# emotion_detection.py

def emotion_detector(text_to_analyze):
    """
    MOCK emotion detection for testing without external API.
    Returns fixed probabilities for demonstration purposes.
    """

    # Example mock values (you can tweak these)
    emotions = {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.9,
        "sadness": 0.04
    }

    dominant_emotion = max(emotions, key=emotions.get)

    result = {**emotions, "dominant_emotion": dominant_emotion}
    return result