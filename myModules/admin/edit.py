from app import app, url_for,redirect, session, flash
from myModules.model.database.database import global_database, ids
@app.route('/<admin>/edit/<title>', methods=['GET'])
def edit_repo(admin, title):
    # check if user is admin
    administrator = global_database.find_one(ids['user'],
                                             username=admin)
    # check if user is admin
    if administrator is not None and session['username'] == admin:
        pass

    else:
        flash("page does not exist")

    return redirect(url_for('all_time'))