from flask import render_template, request, session, redirect, flash, url_for
from flask import Flask, jsonify

app = Flask(__name__)
# app.debug = True
# set secret key
app.config['SECRET_KEY'] = 'ImAPrettyBird'


# import all routers
from views import *

if __name__ == '__main__':
    # socketio.run(app)
    app.run()