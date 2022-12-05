#!/usr/bin/python3
""" This script starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__, template_folder='templates')


@app.route('/cities_by_states', strict_slashes=False)
def city_states():
    """ Render an html page with the list of states.
        In the html page, also lists cities by state """
    return render_template('8-cities_by_states.html',
                           state=storage.all(State).values())


@app.teardown_appcontext
def end_session(self):
    """ Terminate the session to generate a new one """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
