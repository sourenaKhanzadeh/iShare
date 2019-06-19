from pymongo import MongoClient
import os

# online host
if os.environ.get('MONGODB_URI'):
    # OPTIONAL: change MONGODB_URI
    URL = os.environ.get('MONGODB_URI')
    client = MongoClient(URL)
    # CHANGE THE NAME OF THE DATABASE TO YOUR CURRENT DATABASE
    db = client.get_database('heroku_dxftrcxt')
    # db.authenticate(user, password)
# localhost
else:
    URL = "mongodb://localhost:27017/"
    client = MongoClient(URL)
    # You can change client here
    db = client['iShare']

# create the user login
all_users = db["allusers"]

# create the repos
repos = db['repos']

# create sections
sections = db['sections']

# create discussions
comments = db['comments']

# global settings
global_settings = db['settings']

# insert the default globals
if global_settings.count() == 0:
    global_settings.insert({
        'wave':1,
        'diss':1,
    })

# collections id
ids = {
    'user':0,
    'repo':1,
    'section':2,
    'comments':3
}

class Database:
    """
    Mongodb
    LOCAL_URL: mongodb://localhost:27017/
    Database Name: iShare
    Collections
    -----------
        -> all_users
        -> repos
        -> sections
        -> comments
    """

    def __init__(self, db):
        self.all_users = all_users
        self.repos = repos
        self.sections = sections
        self.comments = comments

    def query(self, id, sort='star',limit=2, d=-1, **kwargs):
        """
        (int, str, int, int, **dict) -> Cursor
        query the collections
        @id: id of the collection
            ids = {
                'user':0,
                'repo':1,
                'section':2,
                'comments':3
            }
        @sort: sort stars by default
        @limit: determine the limit of the queries
        @d: descending order by default
        @kwargs: filter the query
        :return: Cursor to the next query
        """
        from myModules.model.database.query import Query

        query = Query(client)

        return [
            query.queryAllUsers(kwargs).limit(limit).sort(sort,d),
            query.queryRepo(kwargs).limit(limit).sort(sort,d),
            query.querySections(kwargs).limit(limit).sort(sort,d),
            query.queryComments(kwargs).limit(limit).sort(sort,d)
        ][id]

    def find_one(self, id, **kwargs):
        from myModules.model.database.findone import FindOne

        find_one = FindOne(client)
        return [
            find_one.findOneUser(kwargs),
            find_one.findOneRepo(kwargs),
            find_one.findOneSection(kwargs),
            find_one.findOneComment(kwargs)
        ][id]

    def count(self, id):
        return [
            self.all_users.count(),
            self.repos.count(),
            self.sections.count()
        ][id]

    def insert(self, id, **kwargs):
        from myModules.model.database.insert import Insert

        insert = Insert(client)

        if id == 0:
            insert.insertAllUser(kwargs)
        elif id == 1:
            insert.insertRepo(kwargs)
        elif id == 2:
            insert.insertSection(kwargs)
        elif id == 3:
            insert.insertComment(kwargs)

    def delete_one(self,id, **kwargs):
        from myModules.model.database.deleteone import DeleteOne

        delete = DeleteOne(client)

        if id == 0:
            delete.deleteOneUser(kwargs)
        elif id == 1:
            delete.deleteOneRepo(kwargs)
        elif id == 2:
            delete.deleteOneSection(kwargs)
        elif id == 3:
            delete.deleteOneComment(kwargs)


# export the database
global_database = Database(client)