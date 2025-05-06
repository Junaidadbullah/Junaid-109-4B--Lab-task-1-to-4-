from flask import Flask, render_template, request, jsonify
from university_chabot import chatbot_app

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get("msg")
    response = chatbot_app(user_text)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
