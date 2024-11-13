# .pre-commit-config.yaml

This configuration file is used by the pre-commit framework to manage and run various code quality and formatting tools before committing changes to the repository.

Each tool listed below is a hook that will be executed by pre-commit.
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

To run all hooks on all files, run: `pre-commit run --all-files`

## Hooks:

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

- **isort**: Sorts and organizes Python imports.

  - Repo: https://github.com/pycqa/isort
  - Rev: 5.13.2
  - Hook ID: isort

- **Prettier**: Formats code for various file types.

  - Repo: https://github.com/pre-commit/mirrors-prettier
  - Rev: v4.0.0-alpha.8
  - Hook ID: prettier

- **blacken-docs**: Formats Python code blocks in documentation.

  - Repo: https://github.com/asottile/blacken-docs
  - Rev: 1.19.1
  - Hook ID: blacken-docs

- **pygrep-hooks**: Various grep-based checks for Python code.

  - Repo: https://github.com/pre-commit/pygrep-hooks
  - Rev: v1.10.0
  - Hook IDs:
    - `python-check-mock-methods`: Checks for common mistakes when using mock methods.
    - `rst-backticks`: Checks for correct usage of backticks in reStructuredText files.

- **pylint**: Lints Python code for style and quality issues.

  - Repo: local
  - Hook ID: pylint

- **bashate**: Lints bash scripts for style and quality issues.

  - Repo: https://github.com/openstack/bashate
  - Rev: 2.1.1
  - Hook ID: bashate

- **shellcheck**: Lints shell scripts for style and quality issues.

  - Repo: https://github.com/shellcheck-py/shellcheck-py
  - Rev: v0.10.0.1
  - Hook ID: shellcheck

- **autoflake**: Removes unused imports and variables from Python code.

  - Repo: https://github.com/myint/autoflake
  - Rev: v2.3.1
  - Hook ID: autoflake

- **bandit**: Security linter for Python code.

  - Repo: https://github.com/PyCQA/bandit
  - Rev: 1.7.10
  - Hook ID: bandit

- **flake8**: Lints Python code for style and quality issues.

  - Repo: https://github.com/PyCQA/flake8
  - Rev: 7.1.1
  - Hook ID: flake8

- **black**: Formats Python code to follow the Black code style.

  - Repo: https://github.com/psf/black-pre-commit-mirror
  - Rev: 24.10.0
  - Hook ID: black

- **mypy**: Static type checker for Python code.
  - Repo: https://github.com/pre-commit/mirrors-mypy
  - Rev: v1.13.0
  - Hook ID: mypy
