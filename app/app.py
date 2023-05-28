
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inex():
    return "Index!"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + name

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
