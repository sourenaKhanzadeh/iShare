from myModules.user.profile import *
from app import app, render_template, request, session, flash
from myModules.tools.tools import validate
from myModules.model.database.database import global_database, ids, repos

@app.route('/<user>/profile/<title>', methods=['GET', 'POST'])
def edit(user,title):
    # get all sections
    sec = global_database.query(ids['section'],
                                limit=global_database.count(ids['section']))

    all_sections = []

    # append all sections
    for section in sec:
        all_sections.append(section)

    # user editing the paper
    if request.method == "GET" and session['username']:
        # get the repo
        query = global_database.find_one(ids['repo'],username= user, title=title)

        return render_template('pages/edit.html',
                               query=query,
                               all_sections =all_sections
                               )
    # user update the paper
    else:
        # get date stars and avatar and validate data
        date, stars, avatar, pdf = validate(request)

        # get the old repo
        prev = repos.find_one({'username': user, 'title':title})

        # Api maximum limit has reached
        if isinstance(stars, dict) or isinstance(avatar, dict):
            # Flash the message
            flash(stars)
            # redirect to homepage
            return redirect('/')

        heroku = True if "heroku" in request.form.get('deploy', []) else False

        # get data from user
        content = {
            'username':session['username'],
            'title': request.form['title'],
            'new_title': request.form['title'] + "<curr>" + prev['title'],
            'url_repo': request.form['repo'],
            'url_pdf': pdf,
            'date': f'{date}',
            'description': request.form['desc'],
            'new_description':request.form['desc'] + "<curr>" + prev['description'],
            'star':stars,
            'avatar':avatar,
            'pending':True,
            'section': request.form['section'],
            'approved':False,
            'heroku':heroku
        }
        # update the repo
        repos.replace_one({'username': user, 'title':title}, content, True)

        # show success
        flash("Successfully updated the paper. now wait for admin to approve")
        return redirect(f'/{user}/profile')