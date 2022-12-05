#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print the following message upon connecting to Flask
        at the above app.route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print the following message upon connecting to Flask
        at the above app.route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def fun_c(text):
    """ Print the following message upon connecting to Flask
        at the above app.route. Text is replaced with whatever
        is passed in """
    return "C {}".format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def cool_python(text=None):
    """ Print the following message upon connecting to Flask
        at the above app.route. Text is replaced with whatever
        is passed in, if any """
    if text is None:
        return "Python is cool"
    else:
        return "Python {}".format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """ Print the following message upon connecting to Flask
        at the above app.route. n is replaced with whatever
        is passed in """
    """ n is always passed in as a string. The following does
        not work
    if isinstance(n, str):
        return "{} is a number".format(n)
    else:
        pass
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Render an html page using the passed in argument n if
        valid type """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
