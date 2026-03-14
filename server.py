from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # your function

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.get_json() or request.form
    statement = data.get("statement", "").strip()

    if not statement:
        # Blank input handling
        return jsonify({
            "raw": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            },
            "formatted": "Invalid text! Please try again!"
        })

    try:
        result = emotion_detector(statement)
        if not result.get("dominant_emotion"):
            formatted = "Invalid text! Please try again!"
        else:
            formatted = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']}, "
                f"and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
    except Exception as e:
        result = {}
        formatted = f"Error analyzing text: {str(e)}"

    return jsonify({"raw": result, "formatted": formatted})


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)