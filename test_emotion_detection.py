from EmotionDetection import emotion_detector

def test_emotion_detector():

    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy'

    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger'

    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust'

    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness'

    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear'

test_emotion_detector()

print("All tests passed")
