from app import app, request, render_template
from myModules.model.database import repos
from flask import session, redirect, flash
from myModules.github.users import GitUser
import datetime

def limitFile(file):
    pass

@app.route("/<user>/upload", methods=['GET', 'POST'])
def upload(user):
    # user is uploading a file
    if request.method == "GET":
        return render_template('pages/upload.html')
    # user is submitting the paper
    else:
        # get current date
        current = datetime.datetime.now()
        date = current.strftime('%d %B %Y')

        # trim repo
        repo = request.form['repo'].replace('https://github.com/', '')
        user, repo = repo.split('/')

        # Get user Repo
        user = GitUser(user)

        # get Users stars
        stars = user.getRepoStar(repo)

        # insert into the database
        repos.insert({
            'username':session['username'],
            'title': request.form['title'],
            'url_repo': request.form['repo'],
            'url_pdf': request.form['pdf'],
            'date': f'{date}',
            'description': request.form['desc'],
            'star':stars
        })
        # success flash popped up
        flash("Paper Successfully Uploaded")
        # redirect to the homepage
        return redirect('/')