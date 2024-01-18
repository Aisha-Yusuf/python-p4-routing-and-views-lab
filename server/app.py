#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'
     

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1*num2
    elif operation == 'div':
        result = num1/num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
