import pymongo
import os

URL = "mongodb://localhost:27017/"
client = pymongo.MongoClient(os.environ.get('MONGODB_URI', URL))
db = client['iShare']

# create the user login
all_users = db["allusers"]

# create the repos
repos = db['repos']

# create sections
sections = db['sections']

# create discussions
comments = db['comments']

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
    URL: mongodb://localhost:27017/
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