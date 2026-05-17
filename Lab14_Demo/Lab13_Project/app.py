from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = "Positive 😊"
            color = "green"
        elif polarity < 0:
            sentiment = "Negative 😞"
            color = "red"
        else:
            sentiment = "Neutral 😐"
            color = "gray"

        result = {
            "sentiment": sentiment,
            "polarity": round(polarity, 2),
            "subjectivity": round(subjectivity, 2),
            "color": color
        }

    return render_template("index.html", result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)
