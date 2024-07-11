# Python Template

[![Build, test with Tox and deploy](https://github.com/proafxin/python-template/actions/workflows/test_release.yaml/badge.svg)](https://github.com/proafxin/python-template/actions/workflows/test_release.yaml)
[![codecov](https://codecov.io/gh/proafxin/python-template/graph/badge.svg?token=w6t9xzSY45)](https://codecov.io/gh/proafxin/python-template)
[![Documentation Status](https://readthedocs.org/projects/python-template-for-packaging/badge/?version=latest)](https://python-template-for-packaging.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/proafxin/statracking/develop.svg)](https://results.pre-commit.ci/latest/github/proafxin/statracking/develop)

A template for building python packages with CI/CD for code quality check and publishing to PyPi. The main purpose is to provide some default settings and configurations for development which I personally use for every project. For example, using `tox` to automate my tasks before pushing changes I made, using `trunk` to check code quality issues, using Github actions as CI, using `codecov` to upload coverage data.

## Development

You need [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) and [Tox](https://tox.wiki/en/latest/installation.html#via-pip) preinstalled.

### Usage

Rename the directory `pytemplate` to your package name. Similarly, change the `name` variable under `tool.poetry` section in `pyproject.toml` file. Remove the files `tests/test_something.py` and `pytemplate/something.py` before any development.

Before you push your code, run `tox` first. You should see all environments pass and you get the message `congratulations :)`.

## Publishing to Pypi

First, you should always update your version using [semantic versioning](https://packaging.python.org/en/latest/discussions/versioning/#semantic-versioning) as PyPi does not allow overwriting existing packages. Run one of the following based on your changes

- `poetry version major`
- `poetry version minor`
- `poetry version patch`

## Environment setup

This template uses Github Actions for publishing to PyPi. So, you also need `PYPI_TOKEN` available as a respository secret. Moreover, import your project in [codecov](https://about.codecov.io/) (get the `CODECOV_TOKEN` from the settings page and add it as a repository secret) and [Read the docs](https://about.readthedocs.com/).
