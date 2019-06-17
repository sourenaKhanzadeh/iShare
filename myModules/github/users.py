from myModules.github.repos import Repo
from myModules.github.github_api import gitApi
import requests

class GitUser:

    def __init__(self, user, page=1,per_page=18):
        """
        (str, int, int) -> None
        :param user: git username
        :param page: page
        :param per_page: how many users per page allowed
        """
        # if page does not exist
        # if page is None:
            # got to page 1
            # page = 1

        # self.page = page
        # self.per_page = per_page
        self.user = user
        # self.repos = self.getAllRepo(user)
        # self.users = self.search(user)



    def search(self, user):
        """
        (str) -> Json
        Search for the user
        :param user: name of the user
        :return: query the user
        """
        return requests.get(gitApi.user_search_url + f'?q={user}'
                                     f'&page={self.page}'
                                     f'&per_page={self.per_page}').json()

    def getRepo(self, repo):
        """
        (str) -> Repo
        get user repo
        :param repo: users repo
        :return: repo
        """
        return Repo(self.user, repo)


    def getAllRepo(self, user):
        """
        (str) -> Json
        :param user: git user
        :return: get all of users repo
        """
        return requests.get(gitApi.getUserRepos(user)).json()

    def getRepoStar(self, repo):
        """
        (str) -> int
        Get a star of a repo
        :param repo: users repo
        :return: star of a repo
        """
        repo = self.getRepo(repo)
        return repo.getStars()