from app import app, request, render_template
from myModules.model.database import repos
from flask import session, redirect, flash

@app.route("/<user>/upload", methods=['GET', 'POST'])
def upload(user):
    # user is uploading a file
    if request.method == "GET":
        return render_template('pages/upload.html')
    # user is submitting the paper
    else:
        # insert into the database
        repos.insert({
            'username':session['username'],
            'Title: ': request.form['title'],
            'url_repo: ': request.form['repo'],
            'url_pdf: ': request.form['pdf'],
            'description: ': request.form['desc']
        })
        # success flash popped up
        flash("Paper Successfully Uploaded")
        # redirect to the homepage
        return redirect('/')