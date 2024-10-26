# strangebasis
This serves as my personal digital toolbox and a module to port all of my coding standards into my other projects.


## License

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)


### Testing the Shared Hooks
You should already be in the poetry shell. If not, enter the interactive virtual env with `poetry shell`.
1. `poetry install`
   1. This installs the module we want to test "strangebasis" with all current changes
2. `python -m strangebasis hooks`
   1. This runs all the pre-commit hooks (changes to these hooks must be explicitly installed *first* using `git add .pre-commit-config.yaml; pre-commit install`)
   2. The importance of testing the hooks in this manner is because mimics how all the other repositories will run the shared hooks.
