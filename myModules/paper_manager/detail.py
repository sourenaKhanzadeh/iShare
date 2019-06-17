from app import app, render_template, session, request,jsonify, flash
from myModules.model.database.database import global_database, ids, comments



@app.route('/<user>/<title>')
def detail(user, title):

    # get repo out of the database
    repo = global_database.find_one(ids['repo'],
        username=user,
        title=title
    )

    # get repo comments
    all_comments = global_database.find_one(ids['comments'],
            title=title
    )

    # if comment section exist in the repo
    if all_comments is not None:
        all_comments = all_comments['comments']

    # make star human readable
    repo['star'] = "{:,}".format(repo['star'])

    # check if user is signed in
    if session.get('username') is not None:
        # user made comments
        if request.args.get('user') is not None:

            # if comment section exist
            if global_database.find_one(ids['comments'],
                        title=title
                ) is not None:
                # get data
                content = {
                    'username':request.args.get('user'),
                    'date':request.args.get('today'),
                    'comment':request.args.get('comment')
                }
                # then update the comment section
                comments.update({'title':title},
                                {
                                '$push':{
                                    'comments':content
                                }
                })
                # send to ajax
                return jsonify(content)
            else:
                # get data
                content = {
                        'username':request.args.get('user'),
                        'date':request.args.get('today'),
                        'comment':request.args.get('comment')
                    }
                # insert to the first comment to the database
                global_database.insert(ids['comments'],
                    title=title,
                    comments=[content]
                )
                # send to ajax
                return jsonify(content)
    else:
        flash("sign in to leave a comment")

    return render_template('pages/detail.html',
                           repo=repo,
                           session=session,
                           comments=all_comments)

# @socketio.on('message')
# def handleMessage(msg):
#     print(f"Message: {msg}")
#     send(msg, broadcast=True)