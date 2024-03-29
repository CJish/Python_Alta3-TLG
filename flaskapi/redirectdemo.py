#!/usr/bin/python3

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

pic_location = "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

# create a limiter object from Limiter
# limits are being performed by tracking the
# REMOTE ADDRESS of the clients
limiter = Limiter(
        app = app,
        key_func = get_remote_address,
        default_limits = ['200 per day', '50 per hour']
        )

@app.route('/upload')
def upload():
    print(pic_location)
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    global pic_location
    # if the method is GET then do the same thing as /upload
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        file_ext = filename.split('.')[-1]
        pic_location = f'static/newpic.{file_ext}'
        f.save('static/newpic.' + file_ext)
        return redirect('/')

# if user sends GET to / (root)
@app.route('/')
def index():
    # found in templates/
    return render_template("towel.html", pic = pic_location)

# if user sends GET or POST to /login
@app.route('/login', methods = ['POST', 'GET'])
@limiter.limit('3 per day')
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains '42 as the value for 'answer'
        if request.form['answer'] == '42':
            # return a 302 redirect to /success
            return redirect(url_for('success'))
        else:
            # return a 302 redirect to /fail
            return redirect(url_for('fail'))
    elif request.method == 'GET':
        # if they sent a GET to /login send 302 redirect to /
        return redirect(url_for('index'))

@app.route('/httpfail')
def httpfail():
    # send back a HTTP failure
    abort(406)

@app.route('/fail')
def fail():
    # nothing wrong with HTTP layer, we just indicate the user responded incorrectly
    return "That was not correct."

@app.route('/success')
def success():
    return 'Correct!'


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
