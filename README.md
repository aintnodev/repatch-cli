# RePatch CLI

Download and patch any compatible app with [ReVanced CLI](https://github.com/ReVanced/revanced-cli)

> [!WARNING]
> This project is currently under active development and is **highly experimental**. Its structure, purpose, and behavior may change significantly over time. It is not production-ready, and no guarantees are made about stability or long-term support. Use with caution.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aintnodev/repatch-cli.git
cd repatch
```

### 2. Install dependencies with `uv`

Install `uv` if not already, then from project `$root`

```bash
uv sync
```

### 3. Make configuration file

Create `config.py` similar to `config.example.py` and populate it with your desired configuration

## Usage

Modify `pkg_name` in `main.py` to desired package name, then run

```bash
uv run main.py
```

> [!CAUTION]
> This tool does not include or distribute any proprietary or third-party binaries. It is designed solely to automate the patching process using official ReVanced tools and publicly available APKs.
> Use at your own discretion. The author is not responsible for misuse, redistribution, or violation of third-party licenses or terms of service.

## Credits

This project wouldn’t exist without the incredible work of the [ReVanced team](https://revanced.app/). All ReVanced components are licensed under the [GPLv3](https://github.com/ReVanced/revanced-cli/blob/main/LICENSE). This script does not modify or include their code, it only downloads and uses them as external tools.

Full credit to the ReVanced developers. This project is not affiliated with or endorsed by the ReVanced project.
