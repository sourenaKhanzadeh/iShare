from myModules.model.database.database import Database

class DeleteOne:

    def __init__(self, db):
        self.database = Database(db)

    def deleteOneUser(self,kwargs:dict):
        return self.database.all_users.delete_one(kwargs)
    def deleteOneRepo(self, kwargs:dict):
        return self.database.repos.delete_one(kwargs)

    def deleteOneSection(self,kwargs:dict):
        return self.database.sections.delete_one(kwargs)

    def deleteOneComment(self,kwargs:dict):
        return self.database.comments.delete_one(kwargs)