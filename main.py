from src.apkmirror import get_app_url
from src.github import get_git_url
from src.download import download_file
from src.patch import patch


def main():
    app_url, app_name = get_app_url("com.google.android.youtube")
    app_path = download_file(app_url, app_name)

    cli_url, cli_name = get_git_url("revanced-cli")
    cli_path = download_file(cli_url, cli_name)

    patches_url, patches_name = get_git_url("revanced-patches")
    patches_path = download_file(patches_url, patches_name)

    patch(app_path, cli_path, patches_path)


if __name__ == "__main__":
    main()
