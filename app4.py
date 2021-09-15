from flask import jsonify, request, render_template
from quotes import them_quotes
from markupsafe import escape
import flask
from quotes import them_quotes

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return {
        "fname": "Bobby",
        "lname": "Boucher",
        "age": 18
    }  #if we return a dict obj it is converted into json automatically


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    

