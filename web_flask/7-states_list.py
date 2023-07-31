#!/usr/bin/python3

"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models import *

app = Flask(__name__)
"""app.url_map.strict_slashes = False"""


@app.route("/state_list", strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def db_teardown(exception):
    """remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
