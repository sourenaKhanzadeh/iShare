from app import app, render_template, request
from myModules.model.database import repos
from flask import session, redirect, flash
from myModules.tools.tools import millify

def queryAll():
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

    return queries

@app.route('/<user>/admin', methods=['GET', 'POST'])
def admin(user):
    # admin is judging the post
    if request.method == "GET":

        # get all queries
        queries = queryAll()

        # render all time
        return render_template('pages/admin.html', queries=queries)
    # admin made a decision
    else:

        # get all queries
        queries = queryAll()

        # take admin decision
        decision = request.form['approve']

        # if admin approved
        # if decision:
            # then approve the paper
            # repos.update({'title':request.form['repo']}, {'$set':{'fsr':True}})

        # render all time
        return render_template('pages/admin.html', queries=queries)
