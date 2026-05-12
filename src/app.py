"""Simple Flask app — base codebase for the A/B test."""

from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {}


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id: str):
    user = USERS.get(user_id)
    if user is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(user)


@app.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json()
    user_id = payload["id"]
    USERS[user_id] = payload
    return jsonify(payload), 201


if __name__ == "__main__":
    app.run(port=5000)
