from app import app, render_template, session, request,jsonify, flash, redirect
from myModules.model.database.database import global_database, ids, comments, global_settings
from bson.objectid import ObjectId
from flask import abort

@app.route('/<path:id>/<path:title>')
def detail(id, title):
    # get global settings
    sett = global_settings.find().next()
    try:
        ObjectId(id)
    except Exception:
        return abort(404)
    # get repo out of the database
    repo = global_database.find_one(ids['repo'],
        _id=ObjectId(id)
    )
    print(repo)

    # get repo comments
    all_comments = global_database.find_one(ids['comments'],
            _id=ObjectId(id)
    )

    if repo is not None:
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
                            _id=ObjectId(id)
                    ) is not None:
                    # get data
                    content = {
                        'username':request.args.get('user'),
                        'date':request.args.get('today'),
                        'comment':request.args.get('comment')
                    }
                    # then update the comment section
                    comments.update({'_id':ObjectId(id)},
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
                        _id=ObjectId(id),
                        comments=[content]
                    )
                    # send to ajax
                    return jsonify(content)
        else:
            flash("sign in to leave a comment")
        return render_template('pages/detail.html',
                               repo=repo,
                               session=session,
                               comments=all_comments,
                               set=sett)
    else:
        flash("not found: " + title)
        return redirect('/')

# @socketio.on('message')
# def handleMessage(msg):
#     print(f"Message: {msg}")
#     send(msg, broadcast=True)