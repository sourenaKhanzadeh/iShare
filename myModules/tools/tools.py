from myModules.github.users import GitUser
import datetime
import math

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


    # return validated data
    return (date, stars, avatar)