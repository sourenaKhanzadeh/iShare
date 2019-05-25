from app import app, render_template
from myModules.model.database import repos
import locale


@app.route('/<user>/<title>')
def detail(user, title):
    # set local to US
    locale.setlocale(locale.LC_ALL, 'en_US')

    # get repo out of the database
    repo = repos.find_one(
        {
        'username':user,
        'title':title
        }
    )

    # make star human readable
    repo['star'] = locale.format('%d', repo['star'], True)

    return render_template('pages/detail.html',
                           repo = repo)