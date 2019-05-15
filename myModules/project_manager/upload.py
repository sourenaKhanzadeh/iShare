from app import app, request, render_template
from myModules.model.database import all_users
from myModules.model.hash import *
from flask import session, redirect, flash

@app.route("/<user>/upload", methods=['GET', 'POST'])
def upload(user):
    return render_template('pages/upload.html')