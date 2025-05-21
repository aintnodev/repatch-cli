import requests


def get_git_url(repo):
    api_url = f"https://api.github.com/repos/ReVanced/{repo}/releases/latest"
    res = requests.get(api_url)
    res.raise_for_status()

    data = res.json()
    assets = data.get("assets")

    download_url = assets[0].get("browser_download_url")
    file_name = assets[0].get("name")

    return download_url, file_name
