# Python Starter

A minimalist template for starting a new [Python](https://www.python.org/) project.

This template provides a basic Python project containing an example package with built-in support for formatting, linting, testing, and continuous integration.

## Key Features

* Uses [uv](https://docs.astral.sh/uv/) as the package manager.
* Supports formatting and linting with [Ruff](https://github.com/astral-sh/ruff), and testing with [Pytest](https://docs.pytest.org/en/stable/).
* Fixes formatting and linting during pre-commit hooks using [Lefthook](https://lefthook.dev/).
* Preconfigured workflows for [Dependabot](https://docs.github.com/en/code-security/dependabot) and [GitHub Actions](https://github.com/features/actions).

## Usage

This guide explains how to use this template to start a new Python project, from creation to release.

### Create a New Project

Follow [this link](https://github.com/new?template_name=python-starter&template_owner=threeal) to create a new project based on this template. For more information about creating a repository from a template on GitHub, refer to [this documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

Alternatively, you can clone this repository locally to begin using this template.

### Set Up Tools

#### Set Up Package Manager

This template uses [uv](https://docs.astral.sh/uv/) as the package manager. If uv is not installed, follow [this guide](https://docs.astral.sh/uv/getting-started/installation/) to install it. Then, synchronize the project dependencies with:

```sh
uv sync
```

For more information on uv, including adding dependencies or running tools, refer to [this documentation](https://docs.astral.sh/uv/guides/).

#### Set Up Git Hooks

This template uses [Lefthook](https://lefthook.dev/) to manage Git hooks, especially for the pre-commit hook. Lefthook will be installed as a development dependency by the package manager, and the pre-commit hook can be installed with:

```sh
uv run lefthook install
```

After that, each commit to the project will trigger a hook that checks for formatting and linting. This ensures that committed files follow the specified rules.

For more information on Lefthook and how it manages hooks, refer to [this documentation](https://lefthook.dev/usage/index.html).

### Developing the Project

#### Choose a License

By default, this template is [unlicensed](https://unlicense.org/). Before modifying this template, it is recommended to replace the [`LICENSE`](./LICENSE) file with the license that will be used by the new project. For more information about licensing a repository, refer to [this documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

Alternatively, you can remove the `LICENSE` file or leave it as is to keep the new project unlicensed.

#### Writing the Package

Modify the source files under the [`src`](./src) directory to start writing the package. If you're new to Python, refer to [this documentation](https://wiki.python.org/moin/BeginnersGuide) for guidance.

You can replace the [`src/bonacci`](./src/bonacci) directory with your package name. You can also add as many packages as you want to the `src` directory. Just make sure to update the contents of the [`pyproject.toml`](./pyproject.toml) file according to your package information.

#### Testing the Package

Test files in this template are named `test_*.py` and located in the [`tests`](./tests) directory. Write the necessary tests for your package and run them with:

```sh
uv run pytest -v --cov
```

This template uses [Pytest](https://docs.pytest.org/en/stable/) as the testing framework. For more information on testing with Pytest, refer to [this documentation](https://docs.pytest.org/en/stable/getting-started.html).

#### Push the Changes

After writing and testing the package, commit the changes and push them to GitHub. Each push to the `main` branch will trigger a GitHub Actions workflow for continuous integration. For more details on GitHub Actions workflows, refer to [this documentation](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions).

Instead of pushing directly to the `main` branch, it is recommended to push to a separate branch and then create a pull request to merge into `main`. This allows changes to be reviewed and checked by GitHub Actions before merging. For more details on pull requests, refer to [this documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

### Releasing the Project

#### Specify Version Number

Update the version number of the package in the [`pyproject.toml`](./pyproject.toml) file to match the version you plan to release. The version number usually follows the semantic versioning system. Refer to [this documentation](https://packaging.python.org/en/latest/discussions/versioning/) for more information on versioning in Python projects.

#### Build the Package

Before releasing, check if the package can be built with:

```sh
uv build
```

This will create a source tarball and wheel distribution of the package under the `dist` directory. You can verify the contents of the package or install it locally to ensure that it is built correctly. For more information on building the package, refer to [this documentation](https://docs.astral.sh/uv/guides/package/#building-your-package).

#### Release on GitHub

Create a new tag in the `main` branch corresponding to the version number of the release, and then draft a new release using that tag. You can also include the source tarball and wheel distribution as assets in the release. Refer to [this documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) for more information on managing releases on GitHub.

#### Publish on PyPI

Run the following command to publish the package to [PyPI](https://pypi.org/):

```sh
uv publish
```

The command will prompt you to enter your username or token for publishing on PyPI. After publishing, wait a few minutes for the package to become available on PyPI. For more information on publishing to PyPI, refer to [this documentation](https://docs.astral.sh/uv/guides/package/#publishing-your-package).
