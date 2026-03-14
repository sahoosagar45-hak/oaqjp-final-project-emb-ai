def emotion_detector(text_to_analyse):
    """
    Emotion detection with blank input handling.
    Returns dictionary with emotion scores and dominant emotion.
    If input is blank, returns all values as None.
    """
    if not text_to_analyse or text_to_analyse.strip() == "":
        # Blank input handling
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Mock emotion detection logic (replace with actual API if available)
    emotions = {'anger': 0.01, 'disgust': 0.02, 'fear': 0.03, 'joy': 0.01, 'sadness': 0.01}
    text_lower = text_to_analyse.lower()

    if "glad" in text_lower or "happy" in text_lower or "fun" in text_lower:
        emotions['joy'] = 0.9
    elif "mad" in text_lower or "hate" in text_lower:
        emotions['anger'] = 0.9
    elif "disgusted" in text_lower:
        emotions['disgust'] = 0.9
    elif "sad" in text_lower:
        emotions['sadness'] = 0.9
    elif "afraid" in text_lower or "scared" in text_lower:
        emotions['fear'] = 0.9

    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions