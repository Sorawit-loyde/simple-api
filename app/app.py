
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Index!"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)


@app.route('/calculate/<num1>/<num2>', methods=['GET'])
def calculate(num1, num2):
    num1 = eval(num1)
    num2 = eval(num2)
    results = {
            'plus' : num1 + num2,
            'minus' : num1 - num2,
            'multiply': num1 * num2,
            'divide' : num1/num2
        }
    return jsonify(results)


if __name__ == '__main__':
    app.run()
