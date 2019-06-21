from app import app, render_template, request, flash, redirect
from myModules.model.database.database import global_settings, global_database, ids

@app.route('/<user>/settings')
def settings(user):
    sett = global_settings.find().next() if global_settings.count() != 0 else {}
    admin_email = sett.get('email', None)
    web_title = sett.get('title', None)

    # check if user is an admin
    admin = global_database.find_one(ids['user'], username=user, fsr=True)

    if admin is not None:
        # admin saving changes
        if request.args.get('wave') is not None:
            # update the global setting
            global_settings.update({},{
                '$set':{
                    'wave':int(request.args['wave']),
                    'diss':int(request.args['dis']),
                    'email':request.args['admin_email'],
                    'email_pass':request.args['admin_pass'],
                    'title':request.args['web_title'],
                    'max_tags':request.args['max_tags']
                    }
            })

            flash('Successfully saved changes')

        return render_template('pages/settings.html',
                               set=sett,
                               email=admin_email,
                               title=web_title)
    else:
        flash("page dose not exist....")
        return redirect('/')