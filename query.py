from time import sleep
import requests

REST = {
  "REPOSITORY": "https://api.github.com/search/repositories?q=stars:%3E100&per_page={per_page}"
}
GRAPHQL = {
  "REPOSITORY":  """
{
  search(query: "stars:>100", type: REPOSITORY, first: {per_page}) {
    repositoryCount
    nodes {
      ... on Repository {
        id
        name
        nameWithOwner
        isPrivate
        owner {
          login
          id
          avatarUrl
          resourcePath
          url
        }
        description
        isFork
        url
        homepageUrl
        diskUsage
        stargazerCount
        watchers {
          totalCount
        }
        primaryLanguage {
          name
        }
        hasIssuesEnabled
        hasProjectsEnabled
        hasWikiEnabled
        forkCount
        mirrorUrl
        isArchived
        isDisabled
        openIssues: issues(states: OPEN) {
          totalCount
        }
        licenseInfo {
          name
          key
          id
          spdxId
          url
        }
        forkingAllowed
        isTemplate
        repositoryTopics(first: 10) {
          nodes {
            topic {
              name
            }
          }
        }
        visibility
        forkCount
        defaultBranchRef {
          name
        }
      }
    }
  }
}
"""
}

def query_runner(api: str, query_type: str, per_page: int, token: str) -> tuple:
    """
    Run a query against the GitHub API.
    Returns a tuple with the response body and the elapsed time.
    """
    headers = {'Authorization': f'token {token}'}
    if api == 'graphql':
        url = 'https://api.github.com/graphql'
        data = {'query': GRAPHQL[query_type].replace('{per_page}', str(per_page))}
        response = requests.post(url, json=data, headers=headers)
    elif api == 'rest':
        url = REST[query_type]
        response = requests.get(url.format(per_page=per_page), headers=headers)
    else:
        raise Exception('Invalid API')
    if response.status_code == 200:
        return response.json(), response.elapsed.total_seconds()
    elif response.status_code == 502:
        sleep(1)
        return query_runner(api, query_type, per_page, token)
    else:
        raise Exception(response.json())