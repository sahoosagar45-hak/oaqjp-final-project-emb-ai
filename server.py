from flask import Flask, render_template, request, jsonify, redirect, url_for
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Make the home page redirect to /emotionDetector
@app.route("/")
def home():
    return redirect(url_for("emotionDetector"))

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        data = request.get_json() or request.form
        statement = data.get("statement", "")

        try:
            result = emotion_detector(statement)
            formatted = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']}, "
                f"and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
            return jsonify({"raw": result, "formatted": formatted})
        except Exception as e:
            return jsonify({"error": f"Error analyzing text: {str(e)}"})

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)