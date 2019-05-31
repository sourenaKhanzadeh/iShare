from app import app, render_template, request
from myModules.model.database.database import sections, all_users
from flask import session, redirect, flash



@app.route('/<user>/admin/<section>/add', methods=['POST'])
def add(user, section):
    # get admin
    admin = all_users.find_one({'username':user, 'fsr':True})
    # check if session exist
    if session.get('username') != None \
        and admin != None:

        # add if duplicate does not exist
        if sections.find({'section':section}).count() == 0:
            #insert the section
            sections.insert({'section':str(section)})

            # message admin
            flash("Successfully added a new section....")
        else:
            flash("section already exist...")

        # redirect back to admin page
        return redirect(f'/')

    flash('page does not exist....')
    return redirect(f'/')


@app.route('/<user>/admin/<section>/remove', methods=['POST'])
def remove(user, section):
    # get admin
    admin = all_users.find_one({'username': user, 'fsr': True})

    # check if session exist
    if session.get('username') != None \
            and admin != None:

        # Delete the section
        sections.remove({'section': section})

        # message admin
        flash("Successfully removed the section")

        # redirect back to admin page
        return redirect(f'/')


    flash('page does not exist....')
    return redirect(f'/')