from myModules.user.profile import *
from app import app, url_for,redirect, session, flash, render_template, request
from myModules.model.database.database import global_database, ids, repos

@app.route('/<admin>/edit/<user>/<title>', methods=['GET', 'POST'])
def edit_repo(admin, user, title):
    # check if user is admin
    administrator = global_database.find_one(ids['user'],
                                             username=admin)
    # admin editing the paper
    if request.method == "GET":
        # check if user is admin
        if administrator is not None \
                and session['username'] == admin:
            # find repo
            query = global_database.find_one(ids['repo'],
                                             username=user,
                                             title=title)
            # find section
            sections = global_database.query(ids['section'],
            limit=global_database.count(ids['section']))

            return render_template('pages/edit.html',query=query, all_sections=sections)

        else:
            flash("page does not exist")
            return redirect(url_for('all_time'))

    # admin saved edited paper
    else:
        # get date stars and avatar and validate data
        date, stars, avatar, pdf = validate(request)

        # Api maximum limit has reached
        if isinstance(stars, dict) or isinstance(avatar, dict):
            # Flash the message
            flash(stars)
            # redirect to homepage
            return redirect('/')

        # get data from user
        content = {
            'username': user,
            'title': request.form['title'],
            'url_repo': request.form['repo'],
            'url_pdf': pdf,
            'date': f'{date}',
            'description': request.form['desc'],
            'star': stars,
            'avatar': avatar,
            'pending': True,
            'section': request.form['section'],
            'approved': True
        }
        # update the repo
        repos.replace_one({'username': user, 'title': title}, content, True)

        # show success
        flash("Successfully updated the paper")
        return redirect(f'/{user}/profile')