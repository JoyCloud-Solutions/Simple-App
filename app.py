from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Python Docker App</h1><p>Status endpoint: /status</p>"

@app.route("/status")
def status():
    return jsonify({
        "status": "running",
        "time": datetime.utcnow().isoformat() + "Z",
        "message": "Hello from the containerized Python app!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
