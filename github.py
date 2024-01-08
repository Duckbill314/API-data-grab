import requests

CLIENT_ID = "cabc601740d416351d52"
CLIENT_SECRET = "cc6c731b5fac52cae7d297786fc6f80ee989e2ff"

REDIRECT_URI = "https://httpbin.org/anything"

def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }
    
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    url = response.url
    return url
    
def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    
    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]

def print_user_info(access_token=None):
    headers = {"Authorization": "token {}".format(access_token)}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print("{} ({}) | private repositories: {}".format(name, username, private_repos_count))
    
link = create_oauth_link()
print("Follow the link to start the authentication with GitHub: {}".format(link))
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print("Exchanged code {} with access token: {}".format(code, access_token))
print_user_info(access_token=access_token)