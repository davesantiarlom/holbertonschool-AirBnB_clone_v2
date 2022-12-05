#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ Render an html page with the list of states and cities """
    return render_template('7-states_list.html',
                           state=storage.all(State).values())


@app.teardown_appcontext
def end_session(exception):
    """ Terminate a session to generate a new one """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
