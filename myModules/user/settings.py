from app import app, render_template


@app.route('/<user>/settings')
def settings(user):
    return render_template('pages/settings.html')