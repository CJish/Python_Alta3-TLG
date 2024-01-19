#!/usr/bin/env python3

"""
Making use of HTTP non-200 type responses.
https://tools.ietf.org/html/rfc2616 # rfc spec describing HTTP
1xx - informational
2xx - success / ok
3xx - redirection
4xx - errors
5xx - server errors
"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

# if user sends GET to root (/)
@app.route('/')
def index():
    # found in ./templates
    return render_template('log_in.html')

# if user sends GET or POST to /login
@app.route('/login', methods = ['GET','POST'])
def login():
    # if user sends a POST
    if request.method == 'POST':
        # if the POST contains 'admin' as the value for username
        if request.form['username'] == 'admin':
            # returns a 302 redirect to /success
            return redirect(url_for('success')) 
        else:
            # if they didn't supply the username 'admin', send back a 401, auth failure
            abort(401)
    elif request.method == 'GET':
        # if the send a GET to /login send 302 redirect to /
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

