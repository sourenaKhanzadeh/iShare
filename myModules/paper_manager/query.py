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
    query = repos.find().sort('star', -1).limit(limit)
    queries = []

    if limit > 2:
        for i in range(limit-1):
            query.next()
        nex = query.next()
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
        return jsonify(content)


    # query all the repos
    for elem in  query:
        # millify star
        elem['star'] = millify(elem['star'])
        queries.append(elem)

    # render all time
    return render_template('pages/query.html', queries=queries)
