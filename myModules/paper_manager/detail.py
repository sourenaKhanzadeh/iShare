from app import app, render_template, socketio, send, session, request
from myModules.model.database.database import global_database
import locale


@app.route('/<user>/<title>')
def detail(user, title):
    # set local to US
    locale.setlocale(locale.LC_ALL, 'en_US')

    # get repo out of the database
    repo = global_database.find_one(1,
        username=user,
        title=title
    )

    # make star human readable
    repo['star'] = locale.format('%d', repo['star'], True)

    # user made comments
    if request.args.get('user') is not None:
        print(request.args.get('today'))
        print(request.args.get('user'))
        print(request.args.get('comment'))

    return render_template('pages/detail.html',
                           repo = repo,
                           session=session)

@socketio.on('message')
def handleMessage(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)