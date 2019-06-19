from app import app, render_template, request, flash, redirect, url_for
from myModules.model.database.database import global_settings

@app.route('/<user>/settings')
def settings(user):
    sett = global_settings.find().next()
    if request.args.get('wave') is not None:
        global_settings.update({},{
            '$set':{
                'wave':int(request.args['wave']),
                'diss':int(request.args['dis']),
                'email':request.args['email'],
                'email_pass':request.args['email_pass'],
                }
        })

        flash('Successfully saved changes')

    return render_template('pages/settings.html',
                           set=sett)