# Lab 9 - NLP Task: Sentiment Analysis using TextBlob

from textblob import TextBlob

sentences = [
    "I love programming and AI is amazing!",
    "This is a terrible and boring class.",
    "The weather is okay today.",
    "Python is the best language for data science.",
    "I hate bugs in my code."
]

print("=== Sentiment Analysis - Lab 9 ===\n")

for sentence in sentences:
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    print(f"Text: {sentence}")
    print(f"Polarity Score: {polarity:.2f}")
    print(f"Sentiment: {sentiment}")
    print("-" * 50)
