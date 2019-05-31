from app import app, request, render_template
from myModules.model.database.database import repos ,global_database, ids
from flask import session, redirect, flash
from myModules.tools.tools import validate


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
            date, stars, avatar = validate(request)

            # Api maximum limit has reached
            if isinstance(stars, dict) or isinstance(avatar, dict):
                # Flash the message
                flash(stars)
                # redirect to homepage
                return redirect('/')

            # insert into the database
            repos.insert({
                'username':session['username'],
                'title': request.form['title'],
                'url_repo': request.form['repo'],
                'url_pdf': request.form['pdf'],
                'date': f'{date}',
                'description': request.form['desc'],
                'star':stars,
                'avatar':avatar,
                'section':request.form['section'],
                'pending':True,
                'approved':False
            })

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
