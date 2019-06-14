from app import app, request, render_template
from myModules.model.database.database import all_users, global_database, ids
from myModules.model.hash import User
from myModules.admin.email_service.admin_email import admin_email, attachment
from flask import flash, redirect

@app.route('/account/register', methods=['GET', 'POST'])
def register():
    """
    """
    # user is trying to register
    if request.method == "POST":
        # HASH THE PASSWORD
        user = User(request.form['username'], request.form['password'])
        # check if user exists in the database
        username = global_database.find_one(ids['user'], username=user.username)
        # if user does not exist in the database then return a flash
        # CREATE A FLASH FOR THE ERROR
        if username == None:
            # send the new member an email with html attachment
            # admin_email.send_to(request.form['email'], 'Welcome to iShare', '',
            #                     attachment.replace('[USER]', user.username))

            # get all users data
            user = {
                'username': user.username,
                'email': request.form['email'],
                'password':user.pw_hash,
                'fsr':False
            }
            # insert user into the database
            all_users.insert(user)
            # user created...
            flash("User Successfully Registered")
            # go back to the landing page
            return redirect('/?Register=success')

        else:
            #TODO: GET ALL ERRORS AND DISPLAY IT AS WARNING TO THE USER
            flash("Username Already Taken")
            return render_template('pages/login-register.html', sign=True)

    # User is filling the form
    elif request.method == "GET":
        return render_template('pages/login-register.html', sign=True)

