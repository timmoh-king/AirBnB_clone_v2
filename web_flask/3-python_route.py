#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
