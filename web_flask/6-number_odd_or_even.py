#!/usr/bin/python3
"""script that starts web app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displaying Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """displaying HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """display C followed by value of text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followwed by value of text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display n is a number only if n is integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n=None):
    """display a HTML page only if n is integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numEvenOdd(n):
    """display a HTML page ony if n is integer"""
    if isinstance(n, int):
        res = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html', n=n, res=res)


if __name__ == '__main__':
    app.run()
