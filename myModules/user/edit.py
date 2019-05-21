from myModules.user.profile import *
from app import app, render_template, request
from myModules.tools.tools import validate

@app.route('/<user>/profile/<title>', methods=['GET', 'POST'])
def edit(user,title):
    # user editing the paper
    if request.method == "GET" and session['username']:
        # get the repo
        query = repos.find_one({'username': user, 'title':title})

        return render_template('pages/edit.html', query=query)
    # user update the paper
    else:
        # get date stars and avatar and validate data
        date, stars, avatar = validate(request)

        # Api maximum limit has reached
        if isinstance(stars, dict) or isinstance(avatar, dict):
            # Flash the message
            flash(stars)
            # redirect to homepage
            return redirect('/')

        # get data from user
        content = {
            'username':session['username'],
            'title': request.form['title'],
            'url_repo': request.form['repo'],
            'url_pdf': request.form['pdf'],
            'date': f'{date}',
            'description': request.form['desc'],
            'star':stars,
            'avatar':avatar
        }
        # update the repo
        repos.replace_one({'username': user, 'title':title}, content, True)

        # show success
        flash("Successfully updated the paper. now wait for admin to approve")
        return redirect(f'/{user}/profile')