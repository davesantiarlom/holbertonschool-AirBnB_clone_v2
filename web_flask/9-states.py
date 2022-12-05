#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__, template_folder='templates')


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_list(id=None):
    """ Render an html page with the list of states,
        or list of cities by the given state """
    return render_template('9-states.html',
                           state=storage.all(State).values(), id=id)


@app.teardown_appcontext
def end_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
