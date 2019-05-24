from app import app, render_template
from myModules.model.database import repos
from flask import session, redirect, flash, request, jsonify
from myModules.tools.tools import millify

@app.route('/Browse-all-time', methods=['GET'])
def allTime():
    # set a limit
    limit = request.args.get('limit', 2, type=int)

    # get all the repos
    # sort by star in descending order
    query = repos.find({'approved':True}).sort('star', -1).limit(limit)
    queries = []

    # user clicked on load_more
    if limit > 2:
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

    # render all time
    return render_template('pages/query.html', queries=queries)
