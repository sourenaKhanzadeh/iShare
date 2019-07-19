from app import app, render_template


@app.errorhandler(404)
def error404(error):
    return render_template('404.html')