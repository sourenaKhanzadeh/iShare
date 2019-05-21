from app import app, render_template, request
from myModules.model.database import repos
from flask import session, redirect, flash
from myModules.tools.tools import millify

@app.route('/<user>/admin')
def admin(user):
    # get all the repos
    # sort by star in descending order
    query = repos.find().sort('star', -1)
    queries = []

    # query all the repos
    for i in range(query.count()):
        # get the next data
        next_query = query.next()
        # millify star
        next_query['star'] = millify(next_query['star'])
        # append data into the query
        queries.append(next_query)
        # render all time

    return render_template('pages/admin.html', queries=queries)