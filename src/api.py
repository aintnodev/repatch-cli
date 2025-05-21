import requests


def app_version(pkg_name):
    res = requests.get("https://api.revanced.app/v4/patches/list")
    res.raise_for_status()
    patches = res.json()

    for patch in patches:
        compatible = patch.get("compatiblePackages")
        if isinstance(compatible, dict):
            versions = compatible.get(pkg_name)
            if versions:
                return versions[-1]
