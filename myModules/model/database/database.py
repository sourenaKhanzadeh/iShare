import pymongo

URL = "mongodb://localhost:27017/"
client = pymongo.MongoClient(URL)
db = client['iShare']

# create the user login
all_users = db["allusers"]

# create the repos
repos = db['repos']

# create sections
sections = db['sections']

# collections id
ids = {
    'user':0,
    'repo':1,
    'section':2
}

class Database:

    def __init__(self, db):
        self.all_users = all_users
        self.repos = repos
        self.sections = sections

    def query(self, id, sort='star',limit=2, d=-1, **kwargs):
        from myModules.model.database.query import Query

        query = Query(client)

        return [
            query.queryAllUsers(kwargs).limit(limit).sort(sort,d),
            query.queryRepo(kwargs).limit(limit).sort(sort,d),
            query.querySections(kwargs).limit(limit).sort(sort,d)
        ][id]

    def find_one(self, id, **kwargs):
        from myModules.model.database.findone import FindOne

        find_one = FindOne(client)
        return [
            find_one.findOneUser(kwargs),
            find_one.findOneRepo(kwargs),
            find_one.findOneSection(kwargs)
        ][id]

    def count(self, id):
        return [
            self.all_users.count(),
            self.repos.count(),
            self.sections.count()
        ][id]




# export the database
global_database = Database(client)