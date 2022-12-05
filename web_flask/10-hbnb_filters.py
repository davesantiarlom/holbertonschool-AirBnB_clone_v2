#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__, template_folder='templates')


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Render an html page with the list of states
        with a list of cities in them, and a list of
        amenities. All are hidden in a popover which
        will require a mouse to hover over to """
    return render_template('10-hbnb_filters.html',
                           state=storage.all(State).values(),
                           amenity=storage.all(Amenity).values())


@app.teardown_appcontext
def end_session(self):
    """ Terminate the session to generate a new one """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)
