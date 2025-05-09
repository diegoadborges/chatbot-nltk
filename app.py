from flask import Flask, Response, render_template, request, jsonify

from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/message", methods=["POST"])
def message() -> Response:
    request_body = request.json
    if request_body is None:
        return jsonify("body cannot be empty", 422)

    user_message = request_body.get("message", "")
    response = get_response(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
