from app import app, request, render_template
from myModules.model.database import all_users
from myModules.model.hash import *

@app.route("/", methods=['GET', 'POST'])
def login():
    """
    """
    #if user is filling the form
    if request.method == "GET":
        return render_template('pages/landingpage.html', sign=False)
    #CHECK IF USER EXIST AND ALLOW THE USER TO ENTER THE PAGE
    # user submit the form
    elif request.method == "POST":
        username = all_users.find({'username': request.form['username']})
        password = username.distinct('password')[0]

        #check if user enter the correct password
        check = check_password_hash(password, request.form['password'])

        # if user enter the correct password
        if check:
            # then welcome the user
            return 'Welcome'
        # else tell the user they entered the wrong password
        # TODO: Flash User The Info


