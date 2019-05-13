from app import app, request, render_template

# import the post login
from myModules.model.login import *
# import the get signUP
from myModules.model.signup import *

@app.route('/')
def welcome():
    return render_template('pages/landingpage.html')