# strangebasis

This serves as my personal digital toolbox and a module to port all of my coding standards into my other projects.

## License

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

### Testing the Shared Hooks

You should already be in the poetry shell. If not, enter the interactive virtual env with `poetry shell`.

1. `poetry install`
   1. This installs the module we want to test "strangebasis" with all current changes
2. `python -m strangebasis hooks`
   1. This runs all the pre-commit hooks (changes to these hooks must be explicitly installed _first_ using `git add .pre-commit-config.yaml; pre-commit install`)
   2. The importance of testing the hooks in this manner is because mimics how all the other repositories will run the shared hooks.

### Running Cookiecutter

1. Make sure you have cookiecutter installed: `pip install cookiecutter`
2. Run cookiecutter: `cookiecutter .`

### Contributing

1. **This is a personal repository** for quickly spinning up robust Python projects according to my standards. It utilizes cookiecutter to templatize my work. I welcome contributions in the following manner.
2. Fork it (https://github.com/skylardonlevy/strangebasis/)
3. Create your feature branch (`git checkout -b feature/fooBar`)
4. Commit your changes (`git commit -am 'Add some fooBar'`)
5. Push to the branch (`git push origin feature/fooBar`)
6. Create a new Pull Request
