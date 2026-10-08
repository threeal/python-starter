# Python Starter

A minimal template for building a [Python](https://www.python.org/) library with an optional CLI. Ships pre-configured with formatting, linting, 100% test coverage enforcement, pre-commit hooks, and CI.

## Getting Started

Create a new repository from this template on GitHub using [this link](https://github.com/new?template_name=python-starter&template_owner=threeal), or clone it locally and point it at your own remote.

## Setup

Install [uv](https://docs.astral.sh/uv/), then install the Python version pinned in `.python-version` along with the dependencies:

```sh
uv sync
```

Install [Lefthook](https://lefthook.dev/) and [dprint](https://dprint.dev/), then register the pre-commit hook:

```sh
lefthook install
```

## Customizing

Replace or extend the template files to fit your project:

- **`src/bonacci/`** — Rename to your package name, matching the package name in `pyproject.toml`.
- **`src/bonacci/__init__.py`** — Update the public API exports to match your library.
- **`src/bonacci/__main__.py`** — Replace or remove the placeholder CLI. Remove this file and the `[project.scripts]` entry in `pyproject.toml` if your project doesn't need a CLI.
- **`src/bonacci/fibonacci.py`** — Replace with your own library logic, along with its tests in `tests/test_fibonacci.py`.
- **`CLAUDE.md`** — Replace with guidance specific to your project.
- **`LICENSE`** — Replace with your preferred license, or keep the [Unlicense](https://unlicense.org/).
- **`pyproject.toml`** — Update the package name, description, version, authors, and other metadata.
- **`README.md`** — Replace with a description of your project.

## Development

Write code in `src/`. Test files live in `tests/` as `test_*.py`. Run the test suite with:

```sh
uv run pytest --cov
```

The project enforces 100% code coverage on every run.

Each `git commit` runs the pre-commit hook registered during setup, which checks your changes and fixes what it can in place. If it fails, fix any reported issues, re-stage the changed files, and commit again.

After committing, push to `main` or open a pull request from another branch — CI will run the same checks across all files, plus additional checks of its own.

## Releasing

Update the version in `pyproject.toml` and in the CLI's `--version` in `src/bonacci/__main__.py`, push a version tag, and create a GitHub Release. To publish to [PyPI](https://pypi.org/), run:

```sh
uv build --clear
uv publish
```
