"""
server.py

Flask web server for NLP Emotion Detection application.
Provides endpoints for rendering the home page and
processing emotion detection requests using the EmotionDetection package.
Handles blank input with appropriate error messages.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """
    Render the home page (index.html) for the NLP Emotion Detection app.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Process POST requests containing a statement to analyze.
    Returns formatted emotion detection results.
    If input is blank, returns an error message.
    """
    try:
        data = request.get_json()
        text_to_analyze = data.get('statement', '')

        result = emotion_detector(text_to_analyze)

        if result['dominant_emotion'] is None:
            return {"formatted": "Invalid text! Please try again!"}

        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']}, "
            f"and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return {"formatted": response_text}

    except Exception as exc:  # pylint: disable=broad-exception-caught
        return {"formatted": f"Error analyzing text: {exc}"}


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
    