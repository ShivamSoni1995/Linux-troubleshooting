from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Flask App is Running Behind NGINX!"

