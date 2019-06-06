from myModules.model.database.database import Database

class Query:

    def __init__(self, db):
        self.database = Database(db)

    def queryAllUsers(self,kwargs:dict):
        return self.database.all_users.find(kwargs)
    def queryRepo(self, kwargs:dict):
        return self.database.repos.find(kwargs)

    def querySections(self,kwargs:dict):
        return self.database.sections.find(kwargs)

    def queryComments(self,kwargs:dict):
        return self.database.comments.find(kwargs)