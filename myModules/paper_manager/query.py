from app import app, render_template
from myModules.model.database.database import global_database, ids
from flask import session, redirect, flash, request, jsonify
from myModules.tools.tools import millify
import slugify

@app.route('/', methods=['GET'])
def all_time():
    # set a limit
    limit = request.args.get('limit', 2, type=int)

    # user logged in
    if session.get('username') is not None:
        # check if admin
        admin = global_database.find_one(ids['user'], username=session['username'], fsr=True)
    else:
        admin = None

    # if clicked on sections
    if request.args.get('section') != None:

        # query according to their section
        query = global_database.query(ids['repo'],limit=limit,
            approved=True,
            section=request.args.get('section')
        )
    elif request.args.get('tag') != None:
        # query according to their tags
        query = global_database.query(ids['repo'], limit=limit,
                                      approved=True,
                                      tags=request.args.get('tag')
                                      )
    else:

        # query all time
        query = global_database.query(ids['repo'], limit=limit,
            approved=True
        )

    queries = []

    # user clicked on load_more
    if limit > 2 and query.count() != 0 and limit <= query.count():

        try:
            # get the second last query
            nex = query[limit-1]

            # store the content
            content = {
                'username':nex['username'],
                '_id':str(nex['_id']),
                'title':nex['title'],
                'url_title':slugify.slugify(nex['title']),
                'approved':nex['approved'],
                'date':nex['date'],
                'description':nex['description'],
                'avatar':nex['avatar'],
                'url_pdf':nex['url_pdf'],
                'url_repo':nex['url_repo'],
                'stars':millify(nex['star']),
                'queries_count':query.count(),
                'limit':limit,
                'section':nex['section'],
                'tags':nex.get('tags',[]),
                'heroku':nex.get('heroku', None)
            }

            if admin is not None:
                content.update({"admin":admin['username']})

        except IndexError:
            content = None


        # upload as json
        return jsonify(content)

    # query all the repos
    for elem in  query:
        # millify star
        elem['star'] = millify(elem['star'])
        elem['url_title'] = slugify.slugify(elem['title'])
        queries.append(elem)

    # get all sections
    sec = global_database.query(2 ,limit=global_database.count(2))

    all_sections = []

    for section in sec:
        # append section to the list
        all_sections.append(section)

    # render all time
    return render_template('pages/query.html',
                           queries=queries,
                           all_sections=all_sections,
                           admin=admin)
