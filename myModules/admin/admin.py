from app import app, render_template, request
from myModules.model.database import repos,all_users
from flask import session, redirect, flash
from myModules.tools.tools import millify

def queryAll(type):
    # get all the repos
    # sort by star in descending order
    query = repos.find({'pending':type}).sort('star', -1)
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
    # check  if user is admin
    admin = all_users.find_one({'username':user})['fsr']

    # validate if username is signed in and it is an admin
    if session['username'] and session['username'] == user and admin:

        # get all queries
        queries = queryAll(True)

        # admin is judging the post
        if request.method == "GET":

            # render all time
            return render_template('pages/admin.html', queries=queries)

        # admin made a decision
        else:

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

    else:
        # page does not exist
        flash("Page does not exist")
        return redirect('/')
