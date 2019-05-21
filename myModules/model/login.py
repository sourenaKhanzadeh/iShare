from app import app, request, render_template
from myModules.model.database import all_users
from myModules.model.hash import *
from flask import session, redirect, flash


@app.route("/account/login", methods=['GET', 'POST'])
def login():
    """
    """
    # if user is filling the form
    if request.method == "GET":
        return render_template('pages/login-register.html', sign=False)
    # CHECK IF USER EXIST AND ALLOW THE USER TO ENTER THE PAGE
    # user submit the form
    elif request.method == "POST":
        username = all_users.find_one({'username': request.form['username']})
        # user not in the database
        if username is None:
            # User Does Not Exist Message Sent
            flash("User Does Not Exist....")
            return render_template('pages/login-register.html', sign=False)
        else:
            password = username['password']

            # check if user enter the correct password
            check = check_password_hash(password, request.form['password'])

            # if user enter the correct password
            if check:
                # store username in a session
                session['username'] = request.form['username']
                # store user status in the session
                session['fsr'] = all_users.distinct('fsr', {'username':session['username']})[0]
                # inform the user they have succesfully signed in
                flash('Login Successful')
                # then redirect to the homepage
                return redirect('/?login=success')

            # else tell the user they entered the wrong password
            # Flash User The Info
            flash("Password Incorrect...")
            return render_template('pages/login-register.html', sign=False)
