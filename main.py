from flask import Flask, render_template, request
import requests

API_URL = ""

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def get_data():
    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']
    print(f"Username: {username}")
    print(f"Password: {password}")

if __name__ == "__main__":
    app.run(debug=True)
