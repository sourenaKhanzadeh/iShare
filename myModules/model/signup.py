from app import app, request, render_template
from myModules.model.database import all_users
from myModules.model.hash import User

@app.route('/signUp', methods=['GET', 'POST'])
def register():
    """
    """
    # user is trying to register
    if request.method == "POST":
        # HASH THE PASSWORD
        user = User(request.form['username'], request.form['password'])
        # check if user exists in the database
        username = all_users.find({'username': user.username})

        # if user exist in the database then return a flash
        # TODO: CREATE A FLASH FOR THE ERROR
        if username.count()  == 0:
            # get all users data
            user = {
                'username': user.username,
                'email': request.form['email'],
                'password':user.pw_hash
            }
            # insert user into the database
            all_users.insert(user)

            # go back to the landing page
            return '<script>window.location = "/"</script>'

        else:
            #TODO: GET ALL ERRORS AND DISPLAY IT AS WARNING TO THE USER
            return 'User Exist In The Database'

    # User is filling the form
    elif request.method == "GET":
        return render_template('pages/landingpage.html', sign=True)

