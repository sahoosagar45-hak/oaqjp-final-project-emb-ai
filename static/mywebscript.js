let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ statement: textToAnalyze })
    })
        .then(response => response.json())
        .then(data => {
            if (data.formatted) {
                document.getElementById("system_response").innerHTML = data.formatted;
            } else if (data.error) {
                document.getElementById("system_response").innerHTML = data.error;
            }
        })
        .catch(err => {
            document.getElementById("system_response").innerHTML = "Error analyzing text: " + err;
        });
}