from app import app, request, render_template
from myModules.model.database import repos
from flask import session, redirect, flash
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


@app.route('/Browse-all-time')
def allTime():
    # get all the repos
    # sort by star in descending order
    query = repos.find().sort('star', -1)
    queries = []

    # query all the repos
    for i in range(query.count()):
        # get the next data
        next_query = query.next()
        # millify star
        next_query['star'] = millify(next_query['star'])
        # append data into the query
        queries.append(next_query)
    # render all time
    return render_template('pages/query.html', queries=queries)