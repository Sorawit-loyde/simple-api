
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index!"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)

if __name__ == '__main__':
    app.run()
