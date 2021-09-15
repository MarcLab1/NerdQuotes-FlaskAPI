from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Python is ok.  Still prefer Java' #The return value from a view function is automatically converted into a response object for you.


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
