from flask import Flask, jsonify

app = Flask(_name_)

@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "status": "running",
        "version": "v1"
    })

@app.route("/health")
def health():
    return "OK", 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)