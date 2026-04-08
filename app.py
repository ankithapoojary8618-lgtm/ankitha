from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "your name" in user_input:
        return "I am your chatbot 🤖"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]
    bot_reply = chatbot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)