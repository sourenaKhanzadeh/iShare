from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, \
                              check_password_hash

app = Flask(__name__)
# app.debug = True

class User(object):

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


@app.route("/", methods=['Get'])
def landing():
    return render_template('./pages/landingpage.html')

@app.route("/", methods=['Post'])
def login():
    user = User(request.form['username'], request.form['password'])
    return '' + request.form['username'] + '\n' +  str(user.check_password(user.pw_hash))


if __name__ == '__main__':
    app.run(debug=True)