#!/usr/bin/python3
"""
Simple Flask API
Endpoints:
- /              → Welcome message
- /data          → Returns list of usernames
- /status        → Returns API status
- /users/<username> → Returns user object or 404 if not found
- /add_user      → POST endpoint to add a new user
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "alice": {"name": "Alice", "age": 32, "city": "New York"}
}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the flask API"


@app.route("/data")
def get_usernames():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():

    """Add a new user from JSON payload"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
