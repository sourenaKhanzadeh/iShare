from app import app, request, render_template
from myModules.model.database import all_users

@app.route('/signUp', methods=['Get'])
def signUp():
    return render_template('pages/landingpage.html', sign=True)


@app.route('/signUp', methods=['Post'])
def signedUp():
    return render_template('pages/landingpage.html', sign=True)
