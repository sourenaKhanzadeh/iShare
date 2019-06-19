from app import app, render_template, request, flash, redirect, url_for
from myModules.model.database.database import global_settings

@app.route('/<user>/settings')
def settings(user):
    sett = global_settings.find().next()
    admin_email = sett.get('email', None)
    web_title = sett.get('title', None)
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
                }
        })

        flash('Successfully saved changes')

    return render_template('pages/settings.html',
                           set=sett,
                           email=admin_email,
                           title=web_title)