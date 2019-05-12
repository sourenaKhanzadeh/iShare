from flask import Flask, render_template, request


app = Flask(__name__)
# app.debug = True

@app.route("/", methods=['Get'])
def landing():
    """
    """
    return render_template('./pages/landingpage.html')

@app.route("/", methods=['Post'])
def login():
    """
    """
    return '' + request.form['username'] + '\n'


if __name__ == '__main__':
    app.run(debug=True)