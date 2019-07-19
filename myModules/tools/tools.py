from myModules.github.users import GitUser
import datetime
from app import flash
import math
import difflib

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
    """
    validate pdf and title
    :param request:
    :return:
    """
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


def show_diff(seqm):
    """Unify operations between two compared strings
seqm is a difflib.SequenceMatcher instance whose a & b are strings"""
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append("<ins>" + seqm.b[b0:b1] + "</ins>")
        elif opcode == 'delete':
            output.append("<del>" + seqm.a[a0:a1] + "</del>")
        elif opcode == 'replace':
            # raise (NotImplementedError, "what to do with 'replace' opcode?")
            print(a0, a1)
            print(b1, b0)
            output.append("<del>" + seqm.a[a0:a1] + "</del>")
            output.append("<ins>" + seqm.b[b0:b1] + "</ins>")
        else:
            raise (RuntimeError, "unexpected opcode")
    return ''.join(output)

# sm= difflib.SequenceMatcher(None, "lorem ipsum dolor sit amet", "lorem foo ipsum dolor amet")
# show_diff(sm)
#Output: 'lorem<ins> foo</ins> ipsum dolor <del>sit </del>amet'