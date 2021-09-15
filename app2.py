import flask
from flask import jsonify, request
from quotes import them_quotes
import random


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1> StAr WaRs QuOtEs </h1>
<p>Use /quotes to get all quotes or /onequote to get one quote </p>
/addquote to add one quote or /getnumquotes to get the number of quotes </p>'''

# A route to return all of the available entries in our catalog.
@app.route('/quotes', methods=['GET'])
def get_all():
    return jsonify(them_quotes)


@app.route('/onequote/', methods=['GET'])
def get_one():
    number = random.randint(0, len(them_quotes) -1 )
    return jsonify(them_quotes[number])

@app.route('/addquote', methods=['POST'])
def add_one():
    them_quotes.append({"quote":"Human sacrifice, dogs and cats living together... mass hysteria!", "author": "Dr. Peter Venkman"})
    return '''<h1> Added new quote </h1> '''

@app.route('/getnumquotes', methods=['GET'])
def get_number():
    return str(len(them_quotes))

@app.route('/addquotetwo', methods=['POST'])
def add_two():
    author = request.args.get('author')
    quote = request.args.get('quote')
    if author is None or author == "" or quote is None or quote == "":  #quote == "" if the user doesn't include it in the url
        author = "Chief Brody"
        quote = "We're going to need a bigger boat."
   
    them_quotes.append({"quote":quote, "author": author})
    return '''<h1> Added brand new quote </h1> '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    