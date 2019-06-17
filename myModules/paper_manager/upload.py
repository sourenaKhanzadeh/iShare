from app import app, request, render_template, url_for
from myModules.model.database.database import global_database, ids
from flask import session, redirect, flash
from myModules.tools.tools import validate
import re

def limitFile(file):
    pass

@app.route("/<user>/upload", methods=['GET', 'POST'])
def upload(user):
    # get all sections
    sec = global_database.query(ids['section'],
                                limit=global_database.count(ids['section']))

    all_sections = []

    # append all sections
    for section in sec:
        all_sections.append(section)

    # validate if username is signed in
    if session.get('username') != None and session['username'] == user:

        # user is uploading a paper
        if request.method == "GET":
            return render_template('pages/upload.html',
                                   all_sections=all_sections)
        # user is submitting the paper
        else:
            # get date stars and avatar and validate data
            #check if user enter the correct information
            date, stars, avatar, pdf = validate(request)

            # Api maximum limit has reached
            if isinstance(stars, dict) or isinstance(avatar, dict):
                # Flash the message
                flash(stars)
                # redirect to homepage
                return redirect('/')

            # check if paper is valid
            if None in {date, stars, avatar, pdf}:

                flash("Could not upload paper")

                return redirect(url_for('upload', user=user))

            else:
                # check if title exist in the database
                if global_database.find_one(ids['repo'],
                    title=request.form['title']) is not None or \
                    any(char in request.form.get('title') for char in {'?', '!', '/', '\\'}):
                    flash("A Paper With The Same Title is Uploaded Or The Title Has Symbols In It")

                    return redirect(url_for('upload', user=user))

                else:

                    #TODO:// prevent html injection

                    # insert into the database
                    global_database.insert(ids['repo'],
                        username = session['username'],
                        title = request.form['title'],
                        url_repo = request.form['repo'],
                        url_pdf = pdf,
                        date = f'{date}',
                        description = request.form['desc'],
                        star = stars,
                        avatar = avatar,
                        section = request.form['section'],
                        pending = True,
                        approved = False

                    )

                    # success flash popped up
                    flash("Paper Successfully Uploaded")
                    # redirect to the homepage
                    return redirect('/')

        # user entered the wrong url
    else:
        # wrong url entered
        flash('failure page does not exist')
        # redirect to the homepage
        return redirect('/')
