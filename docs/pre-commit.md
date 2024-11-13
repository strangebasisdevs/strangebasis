# .pre-commit-config.yaml

This configuration file is used by the pre-commit framework to manage and run various code quality and formatting tools before committing changes to the repository.

## Table of Contents

[TOC]

## Setup

If you've followed the developer setup in [getting_started.md](getting_started.md), pre-commit should already be available and configured in your virtual environment managed by poetry. You can verify this by running the following:

1. Verify if you are in the poetry shell by running:

```sh
poetry shell
```

If you are not already in the shell, this command will activate it.

2. Ensure the pre-commit hooks are installed by running:

```sh
pre-commit install
```

This will configure the pre-commit hooks as defined in the `.pre-commit-config.yaml` file in this project.

## Running Hooks

To run all hooks on all files, run:

```sh
pre-commit run --all-files
```

## Hooks:

Individual hook usage: `pre-commit run <hook-id>`

| Hook Use Case   | Hook ID                   |
| --------------- | ------------------------- |
| Code Formatting | isort                     |
| Code Formatting | prettier                  |
| Code Formatting | black                     |
| Code Formatting | blacken-docs              |
| Code Quality    | pylint                    |
| Code Quality    | flake8                    |
| Code Quality    | mypy                      |
| Security        | bandit                    |
| Utility         | commitizen                |
| Utility         | trailing-whitespace       |
| Utility         | end-of-file-fixer         |
| Utility         | check-yaml                |
| Utility         | check-added-large-files   |
| Utility         | check-case-conflict       |
| Utility         | check-json                |
| Utility         | check-merge-conflict      |
| Utility         | check-toml                |
| Utility         | debug-statements          |
| Utility         | python-check-mock-methods |
| Utility         | rst-backticks             |
| Utility         | bashate                   |
| Utility         | shellcheck                |
| Utility         | autoflake                 |

In most cases, the underlying tools used in the above hooks should be installed as development dependencies within the Poetry virtual environment. This allows most hooks to be run locally. However, be aware that this might not fully replicate the "pre-commit" environment, which is designed to be portable and consistent. Therefore, it is recommended to use the methods outlined above to run the pre-commit checks and/or autoformatting.

### Code Formatting

- **isort**: Sorts and organizes Python imports.

  - Repo: https://github.com/pycqa/isort
  - Rev: 5.13.2
  - Hook ID: isort

- **Prettier**: Formats code for various file types.

  - Repo: https://github.com/prettier/prettier
  - Rev: v4.0.0-alpha.8
  - Hook ID: prettier

- **black**: The uncompromising Python code formatter.

  - Repo: https://github.com/psf/black
  - Rev: 24.10.0
  - Hook ID: black

- **blacken-docs**: Formats Python code blocks in documentation files.
  - Repo: https://github.com/asottile/blacken-docs
  - Rev: 1.19.1
  - Hook ID: blacken-docs

### Code Quality

- **pylint**: A Python static code analysis tool.

  - Repo: https://github.com/PyCQA/pylint
  - Rev: Depends on locally installed dev tool. Run `poetry show pylint` to get current version or `poetry update pylint` to update pylint.
  - Hook ID: pylint

- **flake8**: A tool for style guide enforcement.

  - Repo: https://github.com/PyCQA/flake8
  - Rev: 7.1.1
  - Hook ID: flake8

- **mypy**: A static type checker for Python.
  - Repo: https://github.com/python/mypy
  - Rev: v1.13.0
  - Hook ID: mypy

### Security

- **bandit**: A tool to find common security issues in Python code.
  - Repo: https://github.com/PyCQA/bandit
  - Rev: 1.7.10
  - Hook ID: bandit

### Utility Hooks

- **Commitizen**: Ensures commit messages follow a specified convention.

  - Repo: https://github.com/commitizen-tools/commitizen
  - Rev: v3.30.1
  - Hook ID: commitizen

- **Pre-commit Hooks**: Various utility hooks.

  - Repo: https://github.com/pre-commit/pre-commit-hooks
  - Rev: v5.0.0
  - Hook IDs:
    - `trailing-whitespace`: Removes trailing whitespace from files.
    - `end-of-file-fixer`: Ensures that files end with a newline.
    - `check-yaml`: Checks YAML files for syntax errors.
    - `check-added-large-files`: Prevents adding large files to the repository.
    - `check-case-conflict`: Checks for files with names that would conflict on a case-insensitive filesystem.
    - `check-json`: Checks JSON files for syntax errors.
    - `check-merge-conflict`: Checks for files that contain merge conflict strings.
    - `check-toml`: Checks TOML files for syntax errors.
    - `debug-statements`: Checks for debug statements (e.g., print, pdb) in Python files.

- **pygrep-hooks**: Various grep-based checks.

  - Repo: https://github.com/pre-commit/pygrep-hooks
  - Rev: v1.10.0
  - Hook IDs:
    - `python-check-mock-methods`: Checks for common mistakes in mock method calls.
    - `rst-backticks`: Ensures correct usage of backticks in reStructuredText files.

- **bashate**: A bash script linter.

  - Repo: https://github.com/openstack/bashate
  - Rev: 2.1.1
  - Hook ID: bashate

- **shellcheck**: A shell script static analysis tool.

  - Repo: https://github.com/koalaman/shellcheck
  - Rev: v0.10.0.1
  - Hook ID: shellcheck

- **autoflake**: Removes unused imports and variables.
  - Repo: https://github.com/myint/autoflake
  - Rev: v2.3.1
  - Hook ID: autoflake
