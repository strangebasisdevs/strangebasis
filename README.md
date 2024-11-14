# strangebasis

This serves as my personal digital toolbox and a module to port all of my coding standards into my other projects.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Pytest Status](https://github.com/strangebasisdevs/strangebasis/actions/workflows/ci.yaml/badge.svg)](https://github.com/strangebasisdevs/strangebasis/actions)
[![Release Status](https://github.com/strangebasisdevs/strangebasis/actions/workflows/release.yaml/badge.svg)](https://github.com/strangebasisdevs/strangebasis/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2813985152cc8c721f8a/maintainability)](https://codeclimate.com/repos/672073070b6110522aa99c3e/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2813985152cc8c721f8a/test_coverage)](https://codeclimate.com/repos/672073070b6110522aa99c3e/test_coverage)
[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/strangebasisdevs/strangebasis)](https://github.com/strangebasisdevs/strangebasis/commits/main)

### Quick Start Guide

To get started quickly with this repository, you have two main options:

1. **Cookiecutting a New Project**:

- If you want to generate a new project based on this repository, follow the instructions in the [Running Cookiecutter](#running-cookiecutter) section.

2. **Contributing to This Repository**:

- If you want to contribute to this repository, follow the guidelines in the [Contributing](#contributing) section.

Both options will help you get up and running with the `strangebasis` project efficiently.

### Running Cookiecutter

To generate a project based on different versions of this repository, you can use the following commands:

1. Make sure you have cookiecutter installed: `pip install cookiecutter`
2. Run cookiecutter with the desired version:

- For the latest version from the main branch: `cookiecutter gh:strangebasisdevs/strangebasis`
- For a specific version or tag: `cookiecutter gh:strangebasisdevs/strangebasis --checkout <tag_or_branch_name>`

Replace `<tag_or_branch_name>` with the specific tag or branch you want to use.

### Contributing

1. **This is a personal repository** for quickly spinning up robust Python projects according to my standards. It utilizes cookiecutter to templatize my work. I welcome contributions in the following manner.
2. Fork it (https://github.com/strangebasisdevs/strangebasis)
3. Create your feature branch (`git checkout -b feature/fooBar`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

### Testing Locally

If you are planning to locally test, you should already be in the poetry shell. If not, read through the quick start guide and/or the contribution guide to make sure this is what you want to do.

1. `poetry install`
1. This installs the module we want to test "strangebasis" with all current changes you made in source.
1. `pytest` to run the current test suite (could also include your changes to the tests)!
