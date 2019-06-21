from app import app, render_template

@app.route('/about', methods=['GET'])
def about():
    return render_template('pages/about.html')