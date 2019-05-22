from myModules.user.profile import *
from app import app

@app.route('/<user>/profile/<title>/delete', methods=['GET'])
def delete(user,title):
    # user is deleting the disapproved paper
    repos.remove({'username':user, 'title':title})
    # send message to the user the action was a success
    flash("Successfully deleted the paper")
    # redirect to the profile page
    return redirect(f'/{user}/profile')