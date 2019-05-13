from flask import render_template, request
from flask import Flask

app = Flask(__name__)
# app.debug = True
# set secret key
app.secret_key = "ImAPrettyBird"


# import all routers
from views import *

if __name__ == '__main__':
    app.run(debug=True)