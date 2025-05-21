import requests
from bs4 import BeautifulSoup
from src.api import app_version
from config import SEARCH_API, SEARCH_CX, HEADERS


def search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"q": query, "key": SEARCH_API, "cx": SEARCH_CX, "num": 1}

    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json().get("items")

    if results:
        return results[0]["link"]
    else:
        return None


def get_app_url(pkg_name):
    pkg_arch = "arm64-v8a"
    pkg_version = app_version(pkg_name)
    query = f"{pkg_name}+{pkg_version}+{pkg_arch}"
    file_name = f"{query.replace('+', '-')}.apk"

    app_url = search(query)
    res = requests.get(app_url, headers=HEADERS)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    down_elem = soup.find("a", class_="downloadButton")
    app_url = app_url + down_elem.get("href")

    res = requests.get(app_url, headers=HEADERS)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    down_elem = soup.find("a", id="download-link")
    return "https://www.apkmirror.com" + down_elem.get("href"), file_name
