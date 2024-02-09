from flask import Flask

app = Flask(__name__)

@app.route("/check")
def checkWorking():
    return "Hello from Flask"

app.run(port=5000, host = "0.0.0.0")