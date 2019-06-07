from flask import render_template, request, session, redirect, flash, url_for
from flask import Flask, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.debug = True
# set secret key
app.config['SECRET_KEY'] = 'ImAPrettyBird'
socketio = SocketIO(app)


# import all routers
from views import *

if __name__ == '__main__':
    socketio.run(app)