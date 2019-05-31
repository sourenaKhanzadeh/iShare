# import app
from app import app, request, render_template

# import database
from myModules.model.database.database import repos

# import regex
import re

# import the post login
from myModules.model.logout import *
from myModules.model.login import *
from myModules.user.profile import *
from myModules.paper_manager.detail import *
from myModules.paper_manager.upload import *
from myModules.admin.admin import *
from myModules.user.delete import *
from myModules.paper_manager.query import *

# import logout
# import signUP
from myModules.model.signup import *

@app.route('/')
def welcome():
    # get all users with name

    return render_template('pages/landingpage.html', session=session, page=0)

@app.route('/<repo>')
def search(repo):
    user = repo

    # regex pattern
    pattern = re.compile(repo , re.IGNORECASE)
    # get all liked repos or username and sort it deafeningly by the amount of repo star
    search = repos.find({'$or':[{'title':pattern},
                        {'username':pattern}],
                         '$and':[{'approved':True}]}).sort('star', -1)

    # list of repositories
    repository = []

    # append the repos
    for repo in search:
        repository.append(repo)

    # if repos do not exist
    if len(repository) == 0:
        # then message the user
        flash("Could not find a result.....")

    #get the page
    page = request.args.get('page', 1)

    # render the landing page
    return render_template('pages/landingpage.html',
                           repositories=repository,
                           page=page,
                           user=user)


