from app import app, url_for,redirect, session, flash
from myModules.model.database.database import global_database, ids

@app.route('/<admin>/delete/<title>', methods=['GET'])
def delete_repo(admin, title):
    # check if user is admin
    administrator = global_database.find_one(ids['user'],
                                    username=admin)
    # check if user is admin
    if administrator is not None and session['username'] == admin:
        # delete repo
        global_database.delete_one(ids['repo'], title=title)

        # message admin
        flash("Successfully deleted the repository")

    else:
        flash("page does not exist")

    return redirect(url_for('all_time'))
