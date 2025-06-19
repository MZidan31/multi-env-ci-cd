from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from ENV: {os.getenv('BASE_URL')} with KEY: {os.getenv('API_KEY')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
