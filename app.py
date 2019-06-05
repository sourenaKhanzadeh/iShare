from flask import render_template, request, session, redirect, flash
from flask import Flask
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