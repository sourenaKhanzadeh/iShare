
class GitApi:
    """
    All Git Api Urls
    """
    def __init__(self):
        """
        All Git Api
        """
        self.current_user_url =  "https://api.github.com/user"
        self.current_user_authorizations_html_url = "https://github.com/settings/connections/applications{/client_id}"
        self.authorizations_url = "https://api.github.com/authorizations"
        self.code_search_url = "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}"
        self.commit_search_url = "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}"
        self.emails_url = "https://api.github.com/user/emails"
        self.emojis_url =  "https://api.github.com/emojis"
        self.events_url =  "https://api.github.com/events"
        self.feeds_url = "https://api.github.com/feeds"
        self.followers_url =  "https://api.github.com/user/followers"
        self.following_url = "https://api.github.com/user/following{/target}"
        self.gists_url = "https://api.github.com/gists{/gist_id}"
        self.hub_url = "https://api.github.com/hub"
        self.issue_search_url = "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}"
        self.issues_url = "https://api.github.com/issues"
        self.keys_url = "https://api.github.com/user/keys"
        self.notifications_url = "https://api.github.com/notifications"
        self.organization_repositories_url = "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}"
        self.organization_url = "https://api.github.com/orgs/{org}"
        self.public_gists_url = "https://api.github.com/gists/public"
        self.rate_limit_url = "https://api.github.com/rate_limit"
        self.repository_url = "https://api.github.com/repos/" # /{owner}/{repo}
        self.repository_search_url = "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}"
        self.current_user_repositories_url = "https://api.github.com/user/repos{?type,page,per_page,sort}"
        self.starred_url = "https://api.github.com/user/starred{/owner}{/repo}"
        self.starred_gists_url = "https://api.github.com/gists/starred"
        self.team_url = "https://api.github.com/teams"
        self.user_url = "https://api.github.com/users/{user}"
        self.user_organizations_url = "https://api.github.com/user/orgs"
        self.user_search_url = "https://api.github.com/search/users"#q={query}{&page,&per_page,&sort,&order}

    def getUserRepos(self, user, q=''):
        user_repositories_url = f"https://api.github.com/users/{user}/repos{q}"#?type,page,per_page,sort
        return user_repositories_url


# global github api
gitApi = GitApi()