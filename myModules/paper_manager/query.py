from app import app, render_template
from myModules.model.database.database import global_database, ids
from flask import session, redirect, flash, request, jsonify
from myModules.tools.tools import millify

@app.route('/Browse-all-time', methods=['GET'])
def allTime():
    # set a limit
    limit = request.args.get('limit', 2, type=int)

    # get admin
    admin = global_database.find_one(ids['user'], username=session['username'], fsr=True)

    # if clicked on sections
    if request.args.get('section') != None:

        # query according to their section
        query = global_database.query(1,limit=limit,
            approved=True,
            section=request.args.get('section')
        )

    else:

        # query all time
        query = global_database.query(1, limit=limit,
            approved=True
        )

    queries = []

    # user clicked on load_more
    if limit > 2 and query.count() != 0:

        # get its limit
        for i in range(limit-1):
            query.next()

        # get the second last query
        nex = query.next()

        # store the content
        content = {
            'username':nex['username'],
            'title':nex['title'],
            'approved':nex['approved'],
            'date':nex['date'],
            'description':nex['description'],
            'avatar':nex['avatar'],
            'url_pdf':nex['url_pdf'],
            'url_repo':nex['url_repo'],
            'stars':nex['star'],
            'queries_count':query.count(),
            'limit':limit
        }

        # upload as json
        return jsonify(content)


    # query all the repos
    for elem in  query:
        # millify star
        elem['star'] = millify(elem['star'])
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
