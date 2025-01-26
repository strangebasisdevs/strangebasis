## v0.5.0 (2025-01-26)

### Feat

- **too-much-stuff**: fix, clean, update, brand

## v0.4.0 (2025-01-24)

### Feat

- **cookiecutter**: trickle down tehcnical benefits

## v0.3.0 (2025-01-23)

### Feat

- **nitpick/style.toml**: modularize mypy config management
- **nitpick/style.toml**: modularize flake8 config management
- **nitpick/core.toml**: add shellcheck to the core config management
- **nitpick/style.toml**: modularize pylint config management
- **nitpick/style.toml**: modularize prettier config management
- **nitpick/style.toml**: enforce pyproject isort settings with nitpick
- **nitpick/style.toml**: modularize isort config management
- **nitpick**: truly modularize nitpick core config
- **nitpick/core.toml**: add editorconfig to core.toml
- **nitpick/core.toml**: add nitpick config to core.toml

### Fix

- **vulnerability**: update jinja2 sandbox breakout vuln
- **pyproject.toml**: remove nitpick builtin style for bashate

### Refactor

- **pyproject.toml**: remove comments and prepare for cookiecut inheritance
- refactor nitpick python version check
- **readthedocs**: remove readthedocs integration for now
- **nitpick/core.toml**: modularize bandit config management and remove duplicate bandit hook
- **nitpick/style.toml**: modularize autflake config management
- **nitpick/style.toml**: cleanup pyproject.toml and use builtin for blackendocs
- **nitpick/core.toml**: migrate pypackage gitlegal toml into core.toml
- migrate CodeClimate nitpick into core.toml
- **nitpick/core.toml**: draft core.toml for config as code approach

## v0.2.7 (2024-11-18)

### Fix

- **.codeclimate.yml**: disable markdownlint

## v0.2.6 (2024-11-18)

### Fix

- implement editorconfig pre-commit and update config
- update codeclimate config

### Refactor

- **config**: consolidate more configuration
- **config**: consolidate some configs into pyproject.toml
- **housekeeping**: delete firsttimesetup.note and fix newline chars in repo

## v0.2.5 (2024-11-14)

### Fix

- reference org repo in cookiecutter nitpick config

## v0.2.4 (2024-11-13)

### Fix

- **release.yaml**: try excplicity pushing tag [skip_ci]

## v0.2.3 (2024-11-13)

### Fix

- **release.yaml**: add debug output [skip_ci]

## v0.2.2 (2024-11-13)

### Fix

- **release.yaml**: try suggested fix for tag [skip_ci]

## v0.2.1 (2024-11-13)

### Fix

- debug by pushing local tags to remote
- **release.yaml**: configure git to fetch tags
- **releast.yaml**: add changelog generation and hopefully tagging

## v0.2.0 (2024-11-12)

### Feat

- **coverage**: configure coverage and cookiecut
- **pre-commit**: implement nitpick pre-commit check
- nitpick aha moment and passing pytests
- **integration**: integrate prettier and nitpick
- **nitpick**: created my own nitpick style from built-ins
- **hooks**: implement pylint flake8 and bandit
- **cookiecutting**: 18th times the charm

### Fix

- **release.yaml**: revert key configuration and add permission config
- **release.yaml**: try another way of configuring github_token
- **release.yaml**: add git configuration step for bump

### Refactor

- update pre-commit and nitpick source for cookiecutter test
- **.pre-commit-config.yaml**: remove extraneous comment
- **nitpick**: nitpick for nitpick
- **cookiecutter**: restructure project and add pytests
- record work. change approach

## v0.1.3 (2024-10-25)

### Fix

- **.pre-commit-hooks.yaml**: fix entry command

## v0.1.2 (2024-10-25)

### Feat

- **strangebasis**: setup main python module

## v0.1.1 (2024-10-25)

## v0.1.0 (2024-10-24)

### Feat

- **.pre-commit-config.yaml**: autoupdate hooks
- **packaging**: implement initial python package structure
- **LICENSE**: add AGPL v3 License
