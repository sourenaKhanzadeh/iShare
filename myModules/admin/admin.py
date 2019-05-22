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
        decision = bool(request.form['approve'])

        # take repo title
        title = request.form['repo']

        # if admin approved
        if decision:
            # then approve the paper
            repos.update({'title':title}, {'$set':{'approved':True, 'pending':False}})
            # message admin they successfully approved
            flash("Successfully approved the paper")
            # redirect to admin
            return redirect(f'/{user}/admin')
        # if admin disapproves
        else:
            # then reject the paper
            repos.update({'title':title}, {'$set':{'approved':False, 'pending':False}})
            # message admin they successfully approved
            flash("Successfully disapproved the paper")
            # redirect to admin
            return redirect(f'/{user}/admin')

        # render all time
        return render_template('pages/admin.html', queries=queries)
