from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Serverless Computing!"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Student")
    return f"Hello {name}! Welcome to Cloud ML Lab."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)