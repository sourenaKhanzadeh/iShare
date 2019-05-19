from myModules.github.repos import Repo
from myModules.github.github_api import gitApi
import requests

class GitUser:

    def __init__(self, user, page=1,per_page=18):
        if page is None:
            page = 1
        self.page = page
        self.per_page = per_page
        self.user = user
        self.repos = self.allRepo(user)
        self.users = self.search(user)



    def search(self, user):
        return requests.get(gitApi.user_search_url + f'?q={user}'
                                     f'&page={self.page}'
                                     f'&per_page={self.per_page}').json()

    def getRepo(self, repo):
        return Repo(self.user, repo)


    def allRepo(self, user):
        return requests.get(gitApi.getUserRepos(user))

    def getRepoStar(self, repo):
        repo = self.getRepo(repo)
        return repo.getStars()