from myModules.github.users import GitUser
import datetime
from app import flash
import math
import re

millnames = ['','K',' M',' B','T']

def millify(n):
    """
    (int) -> int
    turn numbers human readable
    1 -> 1
    15550 -> 1.5k
    """
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.1f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


def validate(request):
    # get current date
    current = datetime.datetime.now()
    date = current.strftime('%d %B %Y')

    try:
        # trim repo
        repo = request.form['repo'].replace('https://github.com/', '')
        user, repo = repo.split('/')

        # Get user
        user = GitUser(user)
        # Get user repo
        user_repo = user.getRepo(repo)

        # get Users stars
        stars = user_repo.getStars()

        # get owner avatar
        avatar = user_repo.getAvatar()

        # validate pdf
        pdf = request.form['pdf'] if (request.form['pdf'].endswith('.pdf')) and \
        (request.form['pdf'].startswith('https://') or request.form['pdf'].startswith('http://'))\
        else None


        # check if it is a pdf file
        if pdf is None:
            flash("Please Insert A PDF Url")

        print(date, stars, avatar, pdf)

        # return validated data
        return (date, stars, avatar, pdf)

    except Exception:
        flash("Please Enter a Git Repository")

        return None, None, None, None

