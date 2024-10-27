# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Author: {{ cookiecutter.author_name }}

## Installation and Setup

### Prerequisites

* Python 3.12
* pip

### First Time Project Setup (Future NIX? or Ansible?)

1. Install the required version of Python (e.g., 3.12).

   This is the Python environment that will run your project. Verify the Python installation by running `python --version`.

2. Initialize a new Poetry project with desired parameters.

   Poetry is my/our package manager for Python. It will create a `poetry.lock` file for you. This is a virtual environment that will contain all the dependencies required by your project. To initialize a new Poetry project, run a command like `poetry init --name={{ cookiecutter.project_name }} --description="{{ cookiecutter.description }}" --author="{{ cookiecutter.author_name }}" --license="AGPL-3.0" --python="{{ cookiecutter.python_version }}" --dependency=black@{{ cookiecutter.black_version }} --no-interaction`. This will create a `poetry.toml` file for you.

3. Install project dependencies.

   With Poetry initialized, you can install the project dependencies using `poetry install`. This will install all the packages listed in your `poetry.toml` file, including Poetry itself.

4. Activate the virtual environment.

   After installing the project dependencies, Poetry will create a virtual environment for you. To activate the virtual environment, run `poetry shell`. This will install Poetry, pre-commit, and any other dependencies listed in your `poetry.toml` file.

5. Set up pre-commit hooks.

   Pre-commit hooks are a way to enforce coding standards and prevent common errors before committing your code. To set up pre-commit hooks, run `pre-commit install`.

6. Use Commitizen for conventional commits.

   Commitizen is a tool to help you write conventional commit messages. To use Commitizen, run `cz c`.

### Working with Poetry

When developing a Poetry project like this one, it is recommended to use the Poetry shell exclusively. This allows Poetry to manage the Python environment and dependencies for you. To activate the Poetry shell, run `poetry shell` (many IDEs will integrate your developer console with the virtual environment but it's good to be sure for consistency). From then on, you can use the `poetry` command to manage dependencies and run your project. The Poetry shell is a virtual environment that is separate from the system Python environment, allowing you to isolate your project's dependencies. It replaces the built-in package manager pip in the context of this project. It is similar to npm for JavaScript and pipenv for Python.

To declare a dependency in your project, you can use the `poetry add` command. E.g., to declare a dependency on the requests library, you can run `poetry add requests`. Poetry will then install the dependency and add it to the list of dependencies in the pyproject.toml file.

To install all declared dependencies, you can run `poetry install`. Poetry will then install all declared dependencies and their dependencies.

You can also use the `poetry remove` command to remove a dependency from your project. E.g., to remove the requests library, you can run `poetry remove requests`.

## Usage

Please answer the following questions to help define the usage of your project:

* What is the main purpose of your project?
* What are the main features of your project?
* How should users run your project?
* What are the expected inputs and outputs of your project?
* Are there any specific command line arguments or options?
* Are there any specific environment variables to be set?
* Are there any specific dependencies to be installed?

### Getting Started

1. Run the project: `poetry install; python -m <project_name>`
   * What are the common uses? Anything more than running main?

### Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request.

## License and Copyright

* License: GNU AFFERO GENERAL PUBLIC LICENSE
* Copyright: {{ cookiecutter.year }}, Skylar DonLevy

## Contact

* Author: [Author Name](mailto:skylar.donlevy.dev@gmail.com)
