from myModules.model.database import repos
from app import app, request, render_template
from myModules.github.github_api import gitApi
import requests

class Repo:

    def __init__(self, user, repo=None):
        self.rep = self.getRepos(user, repo)


    def getRepos(self, owner, repo):
        """
        get Json data
        :param owner: the user
        :param repo: the repository
        """
        return requests.get(gitApi.repository_url + owner + '/' + repo).json()


    def getStars(self):
        """
        get repo star
        :return: repo star
        """
        try:
            return self.rep['stargazers_count']
        except KeyError:
            return self.rep

    def getAvatar(self):
        """
        get repo avatar
        :return: repo avatar
        """
        try:
            return self.rep['owner']['avatar_url']
        except KeyError:
            return self.rep
