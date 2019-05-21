from app import app, request, render_template
from myModules.model.database import repos
from flask import session, redirect, flash
from myModules.tools.tools import validate


def limitFile(file):
    pass

@app.route("/<user>/upload", methods=['GET', 'POST'])
def upload(user):
    # user is uploading a paper
    if request.method == "GET":
        return render_template('pages/upload.html')
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
            'pending':True,
            'approved':False
        })

        # success flash popped up
        flash("Paper Successfully Uploaded")
        # redirect to the homepage
        return redirect('/')