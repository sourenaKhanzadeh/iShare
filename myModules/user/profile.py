from app import app, render_template, request
from myModules.model.database.database import global_database
from flask import session, redirect, flash
from myModules.tools.tools import millify

@app.route('/<user>/profile')
def profile(user):
    # validate if username is signed in
    if session['username'] and session['username'] == user:
        # get all the repos
        # sort by star in descending order
        query = global_database.query(ids['repo'],
        limit=global_database.count(ids['repo']),username=session['username'])

        queries = []

        # query all the repos
        for query in query:
            # millify star
            query['star'] = millify(query['star'])
            # append data into the query
            queries.append(query)
            # render all time
        return render_template('pages/profile.html', queries=queries)
    else:
        # wrong url entered
        flash('failure page does not exist')
        return redirect('/')

# import edit profile
from myModules.user.edit import *