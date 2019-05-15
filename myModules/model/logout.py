from app import app
from flask import session, redirect, flash

@app.route("/account/logout", methods=['GET'])
def logout():
    """
    """
    # destroy the session
    session.pop('username')
    # message the user
    flash("Successfully Logged Out")
    # redirect back to the homepage
    return redirect('/?logout=success')


