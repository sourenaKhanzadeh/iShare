from app import app, request

@app.route("/", methods=['Post'])
def login():
    """
    """
    return '' + request.form['username'] + '\n'


