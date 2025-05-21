import subprocess
from pathlib import Path
from config import ROOT_DOWNLOAD_DIR, ROOT_OUTPUT_DIR


def patch(app_path, cli_path, patches_path):
    out_path = app_path.replace(ROOT_DOWNLOAD_DIR, ROOT_OUTPUT_DIR)
    command = [
        "java",
        "-jar",
        cli_path,
        "patch",
        "-p",
        patches_path,
        "-o",
        out_path,
        app_path,
    ]

    out_path = "/".join(out_path.split("/")[:-1])
    if not Path(out_path).exists():
        Path(out_path).mkdir(parents=True, exist_ok=True)

    if (
        Path(cli_path).exists()
        and Path(patches_path).exists()
        and Path(app_path).exists()
    ):
        subprocess.run(command, capture_output=True, text=True, check=True)
