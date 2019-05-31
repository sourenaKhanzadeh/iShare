from myModules.model.database.database import Database

class FindOne:

    def __init__(self, db):
        self.database = Database(db)

    def findOneUser(self,kwargs:dict):
        return self.database.all_users.find_one(kwargs)
    def findOneRepo(self, kwargs:dict):
        return self.database.repos.find_one(kwargs)

    def findOneSection(self,kwargs:dict):
        return self.database.sections.find_one(kwargs)