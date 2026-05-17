from flask import Flask, render_template, request
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_emails(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    return sorted(set(re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        soup.get_text()
    )))

@app.route("/", methods=["GET", "POST"])
def index():
    emails = []
    if request.method == "POST":
        url = request.form.get("url")
        emails = scrape_emails(url)
    return render_template("index.html", emails=emails)

if __name__ == "__main__":
    app.run(debug=True)
