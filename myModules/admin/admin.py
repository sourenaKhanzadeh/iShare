from app import app, render_template, request
from myModules.model.database.database import repos,all_users, sections
from flask import session, redirect, flash
from myModules.tools.tools import millify


def queryAll(type):
    """
    return all queries that are pending
    :param type: query type pending/approved/disapproved
    :return: all queries
    """
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
    if session.get('username') != None and session['username'] == user and admin:

        # get all queries
        queries = queryAll(True)

        # admin is judging the post
        if request.method == "GET":
            # get all sections from the database
            sec = sections.find()

            all_sections = []
            # get all sections
            for section in sec:
                # append it
                all_sections.append(section)

            # render all time
            return render_template('pages/admin.html',
                                   queries=queries,
                                   all_sections=all_sections)

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

# import admin routs
from myModules.admin.section import *
