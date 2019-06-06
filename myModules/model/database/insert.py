from myModules.model.database.database import Database

class Insert:

    def __init__(self, db):
        self.database = Database(db)

    def insertAllUser(self,kwargs:dict):
        return self.database.all_users.insert(kwargs)
    def insertRepo(self, kwargs:dict):
        return self.database.repos.insert(kwargs)

    def insertSection(self,kwargs:dict):
        return self.database.sections.insert(kwargs)

    def insertComment(self,kwargs:dict):
        return self.database.comments.insert(kwargs)