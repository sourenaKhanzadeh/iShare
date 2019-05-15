from app import app, request, render_template
from myModules.github.repos import Repo
from myModules.github.users import GitUser
# import the post login
from myModules.model.logout import *
from myModules.model.login import *
from myModules.project_manager.upload import *
# import the get logout
# import the get signUP
from myModules.model.signup import *

@app.route('/')
def welcome():
    # get all users with name

    return render_template('pages/landingpage.html', session=session, page=0)

@app.route('/<user>')
def search(user):
    search = GitUser(user, request.args.get('page'))
    users = []

    if 'items' in search.users:
        # get all gits search result and append it
        for use in search.users['items']:
            users.append(use)

    # if user was not found
    if len(users) == 0:
        # message the user
        flash("No Result Found.....")
    return render_template('pages/landingpage.html',
                           session=session,
                           users=users,
                           page=search.page,
                           search=user)


