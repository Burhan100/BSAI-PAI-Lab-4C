from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            current = data["current_condition"][0]
            weather = {
                "city": city,
                "temp": current["temp_C"],
                "feels_like": current["FeelsLikeC"],
                "humidity": current["humidity"],
                "wind": current["windspeedKmph"],
                "description": current["weatherDesc"][0]["value"]
            }
        else:
            error = "City not found!"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
