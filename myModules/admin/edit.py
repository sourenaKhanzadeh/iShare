from myModules.user.profile import *
from app import app, url_for,redirect, session, flash, render_template, request
from myModules.model.database.database import global_database, ids, repos, global_settings

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

        # get tags
        tags = str(request.form.get('tags'))
        tags = tags.split(';')
        tags.pop()

        max_tags = int(global_settings.find().next().get('max_tags', 5))

        # tag overload
        if len(tags) > max_tags:
            flash("Maximum Tags Reached")
            return redirect(url_for('edit_repo', admin=admin,user=user, title=title))

        heroku = True if "heroku" in request.form.get('deploy',[None]) else False

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
            'tags':tags,
            'section': request.form['section'],
            'heroku':heroku,
            'approved': True,
            'pending': False
        }
        # update the repo
        repos.replace_one({'username': user, 'title': title}, content, True)

        # show success
        flash("Successfully updated the paper")
        return redirect(f'/{user}/profile')