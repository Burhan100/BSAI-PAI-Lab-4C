from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = Flask(__name__)

# --- Dataset: University Admission QnA ---
qa_data = [
    {"q": "What is the admission deadline?", "a": "The admission deadline is March 31st."},
    {"q": "What programs are offered?", "a": "We offer BS CS, BS AI, and BS Software Engineering."},
    {"q": "What is the fee per semester?", "a": "The semester fee is Rs. 45,000."},
    {"q": "What is the minimum merit?", "a": "Minimum merit is 60% in FSc or equivalent."},
    {"q": "How can I contact admissions?", "a": "Email us at admissions@university.edu.pk"},
    {"q": "Is hostel available?", "a": "Yes, hostel facility is available for outstation students."},
    {"q": "When do classes start?", "a": "Classes begin in September after the admission process."},
    {"q": "What documents are required?", "a": "You need Matric, FSc certificates, CNIC, and 2 photos."},
]

questions = [item["q"] for item in qa_data]
answers = [item["a"] for item in qa_data]

# Load model and build FAISS index
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(questions)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))
print("FAISS index ready!")

def get_answer(user_question):
    query_vec = model.encode([user_question])
    D, I = index.search(np.array(query_vec), k=1)
    return answers[I[0][0]]

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_q = request.form["question"]
        answer = get_answer(user_q)
        chat_history.append(("You", user_q))
        chat_history.append(("Bot", answer))
    return render_template("index.html", chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
