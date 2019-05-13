from app import app, request, render_template




@app.route("/", methods=['Get'])
def landing():
    """
    """
    return render_template('pages/landingpage.html', sign=False)

# import the post login
from myModules.model.login import *
# import the get signUP
from myModules.model.signup import *