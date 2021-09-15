import re
from flask import jsonify, request, render_template
from quotes import them_quotes
from markupsafe import escape
import random
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Hello"

#because we are returning html, we use escape() to prevent from injection attacks
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("hello.html")
    elif request.method == 'POST':
        return "POST"
    else:
        return str(request.method)  #it should never get here as only GET and POST are permitted

@app.route("login/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)