#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_c(text):
    """display “C ” followed by the value of the text"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text_python(text):
    """display “Python ”, followed by the value of the text"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    num = 'odd' if n % 2 != 0 else 'even'

    return render_template('6-number_odd_or_even.html', n=n, num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
