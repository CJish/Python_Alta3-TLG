#!/usr/bin/env python3

"""Using the Flask-Limiter package to set limits
   on individual API requests from an IP."""

from flask import Flask
## from python3 -m pip install Flask-Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# create an app object from Flask
app = Flask(__name__)

# create a limiter object from Limiter
# limits are being performed by tracking the 
# REMOTE ADDRESS of the client

limiter = Limiter(
        app = app,
        key_func = get_remote_address,
        default_limits = ['200 per day', '50 per hour']
        )

# we now have TWO decorators on our function
# app.route() describes WHEN to trigger the function
# limiter.limit() describes HOW OFTEN to trigger the function
@app.route('/slow')
@limiter.limit('1 per day')
def slow():
    return 'Enjoy this message, it will only display once per day.'

# no limiter decorator is needed, this function is STILL limited
# by the defaults set above
@app.route('/fast')
def fast():
    return 'I inherit the default limits of 200 per day and 50 per hour.'

# limiter().exempt removes all limits on this API
@app.route('/ping')
def pint():
    return 'PONG FOREVER!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
