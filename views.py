# import app
from app import app, request, render_template
import re
import slugify

# import database
from myModules.model.database.database import repos, global_settings
from myModules.model.logout import *
from myModules.model.login import *
from myModules.user.profile import *
from myModules.user.delete import *
from myModules.user.settings import *
from myModules.user.about import *
from myModules.paper_manager.detail import *
from myModules.paper_manager.upload import *
from myModules.paper_manager.query import *
from myModules.admin.admin import *
from myModules.admin.delete import *
from myModules.admin.edit import *
from myModules.error_codes import *

# import logout
# import signUP
from myModules.model.signup import *

@app.route('/Browse-all-time')
def welcome():
    #get settings
    sett = global_settings.find().next()

    return render_template('pages/landingpage.html',
                           session=session, page=0, set=sett)

@app.route('/<repo>')
def search(repo):
    """
    search engine logic
    :param repo: search user, title ,tags or section
    :return: query result
    """
    # get settings
    sett = global_settings.find().next()

    #PAGE PAGINATION SETTINGS
    user = repo

    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))


    # regex pattern
    pattern = re.compile(repo , re.IGNORECASE)

    search_logic = {'$or':[{'title':pattern},
                        {'username':pattern},
                        {'section':pattern}],
                         '$and':[{'approved':True}]}

    # get all liked repos or username and sort it deafeningly by the amount of repo star
    temp = repos.find(search_logic).sort('star', -1)
    if temp.count() != 0:
        if offset >= temp.count():
            offset = temp.count() - 1

        last_id = temp[offset]['star']

        if {'$gte':last_id} not in  search_logic['$and']:
            search_logic['$and'].append({'star':{'$lte': last_id}})
        else:
            search_logic['$and']['star']['$lte'] = last_id


        search = repos.find(search_logic).sort('star', -1).limit(limit)

        # list of repositories
        repository = []

        # append the repos
        for repo in search:
            repo['url_title'] = slugify.slugify(repo['title'])
            repository.append(repo)

    # if repos do not exist
    else:
        repository = None
        # then message the user
        flash("Could not find a result.....")

    #get the page
    page = request.args.get('page', 1)

    # render the landing page
    return render_template('pages/landingpage.html',
                           repositories=repository,
                           page=page,
                           user=user,
                           set=sett,
                           limit=limit,
                           offset=offset,
                           maxx = temp.count())


