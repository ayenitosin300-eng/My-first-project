from flask import Flask, request, jsonify
import json, os

DB_FILE = "accounts.json"

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        accounts = json.load(f)
else:
    accounts = {}

app = Flask(__name__)

@app.route("/create", methods=["POST"])
def create():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    if username in accounts:
        return jsonify({"error": "User exists"}), 400
    accounts[username] = {"password": password}
    with open(DB_FILE, "w") as f:
        json.dump(accounts, f, indent=2)
    return jsonify({"success": True, "user": username})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if accounts.get(username, {}).get("password") == password:
        return jsonify({"success": True, "user": username})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
