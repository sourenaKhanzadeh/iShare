from app import app, request, render_template
from myModules.model.database import repos
from flask import session, redirect, flash


@app.route('/Browse-all-time')
def allTime():
    query = repos.find()
    queries = []
    for i in range(query.count()):
        queries.append(query.next())
    return render_template('pages/query.html', queries=queries)