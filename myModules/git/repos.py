from myModules.model.database import repos
from app import app, request, render_template
import requests

# global git api
gitApi = 'https://api.github.com/'

class GitApi:
    pass

class Repo:

    def __init__(self, user, repo=None):
        self.rep = self.getRepos(user, repo)


    def getRepos(self, owner, repo):
        """
        get Json data
        :param owner: the user
        :param repo: the repository
        """
        return requests.get(gitApi + 'repos/' + owner + '/' + repo).json()


    def getStars(self):
        return self.rep['stargazers_count']


class GitUser:

    def __init__(self, user):
        self.users = self.search(user)['items']


    def search(self, user):
        return requests.get(gitApi + 'search/users?q=' + user).json()

    def getRepo(self, repo):
        rep = Repo(self.users['login'], repo)
        return  rep.rep