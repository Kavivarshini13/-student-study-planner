from flask import Flask, render_template, request, jsonify
from planner_agent import generate_plan
from chatbot_agent import chatbot_reply

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    plan = ""
    if request.method == "POST":
        subject = request.form.get("subject")
        if subject:
            plan = generate_plan(subject)
    return render_template("index.html", plan=plan)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = chatbot_reply(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
