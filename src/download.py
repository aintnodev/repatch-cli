import requests
from pathlib import Path
from config import ROOT_DOWNLOAD_DIR, HEADERS


def download_file(download_url, file_name):
    dir_no_ext = "-".join(file_name.split(".")[:-1])
    download_dir = f"{ROOT_DOWNLOAD_DIR}/{dir_no_ext}"
    file_path = f"{download_dir}/{file_name}"

    if not Path(file_path).exists():
        Path(download_dir).mkdir(parents=True, exist_ok=True)

        res = requests.get(download_url, headers=HEADERS, stream=True)
        res.raise_for_status()

        with open(file_path, "wb") as file:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

    return file_path
