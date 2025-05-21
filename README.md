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
