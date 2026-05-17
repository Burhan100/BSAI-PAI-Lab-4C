from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based chatbot responses
responses = {
    "admission": "Admissions are open from January to March every year.",
    "deadline": "The last date for admission is March 31st.",
    "fee": "The semester fee is Rs. 45,000.",
    "programs": "We offer BS Computer Science, BS AI, and BS Software Engineering.",
    "merit": "Minimum merit for CS is 60% in FSc or equivalent.",
    "contact": "You can contact us at admissions@university.edu.pk",
    "hello": "Hello! Welcome to University Admission Chatbot. How can I help you?",
    "hi": "Hi there! Ask me anything about admissions.",
    "thanks": "You're welcome! Feel free to ask more questions."
}

def get_reply(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return responses[key]
    return "Sorry, I didn't understand. Try asking about: admission, deadline, fee, programs, merit, or contact."

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_msg = request.form["message"]
        bot_reply = get_reply(user_msg)
        chat_history.append(("You", user_msg))
        chat_history.append(("Bot", bot_reply))
    return render_template("index.html", chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
