from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the test site!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    return f"Received: {data}"

if __name__ == "__main__":
    app.run(port=5000)  # Runs on http://127.0.0.1:5000
