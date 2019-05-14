from app import app, request, render_template
from myModules.git.repos import Repo, GitUser
# import the post login
from myModules.model.login import *
# import the get signUP
from myModules.model.signup import *

@app.route('/')
def welcome():
    # get all users with name

    return render_template('pages/landingpage.html', session=session)

@app.route('/<user>')
def search(user):
    search = GitUser(user)
    users = []
    for use in search.users:
        users.append(use)

    return render_template('pages/landingpage.html', session=session, users=users)
