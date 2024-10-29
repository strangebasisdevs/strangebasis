# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Author: {{ cookiecutter.author_name }}

## Installation and Setup

### Prerequisites

- Python 3.12
- pip

### First Time Project Setup (Future NIX? or Ansible?)

These steps are intended to follow the "cookiecut" of the strangebasis standards. Some are pre-requisite and can be verified quickly, especially if you've cookiecut strangebasis on this machine already.

Details below, fast track here:

```
poetry install; poetry shell
git init; git add -A; pre-commit install; pre-commit run --all-files; pytest; git add -A; cz c
```

#### Prerequisites

1. Install the required version of Python (e.g., 3.12).

   This is the Python environment that will run your project. Verify the Python installation by running `python --version`.

2. Initialize a new Poetry project with desired parameters.

   Install poetry with python version 3.12:
   `python -m pip install poetry`

   This package is a robust python packaging and dependency management solution. Pythonic, well documented, and widely supported! After the "cookiecut"

#### Dev Project Setup!

1. Install project dependencies.

   With Poetry initialized, you can install the project dependencies using `poetry install`. This will install all the packages listed in your `poetry.toml` file, including Poetry itself.

2. Activate the virtual environment.

   Without specifically adjusting this, Poetry will create a virtual environment for you when you run the install command in the previous step (thank you poetry). To activate the virtual environment, run `poetry shell`. This will make sure you have access to the dependencies listed in your `poetry.toml` file in your interactive shell session. I loaded up the development tools and I plan to expand them; I like having a solid toolbox and I recommend you practice using one too. Check out the pyproject.toml for the dev-dependencies to get some ideas. Many of these are configured in the pre-commit hooks, but being able to run them manually, when you need them, rocks.

   The AI tools say this:

   Poetry automatically creates a virtual environment for your project. Activate it by running `poetry shell`. This ensures access to dependencies specified in `pyproject.toml`. A well-equipped development environment is crucial; explore the dev-dependencies section in `pyproject.toml` for tools to enhance your workflow. Many are set up in pre-commit hooks (and are run automatically when you use my pre-commit hooks) but can also be executed manually when needed.

3. Initialize the Git repository.

   Run `git init` to create a new Git repository in the project directory. This will allow you to track changes to your project over time. Since everything is new, makes sense to follow this up with `git add -A`

4. Set up pre-commit hooks.

   Pre-commit hooks are a way to enforce coding standards and prevent common errors before committing your code. To set up pre-commit hooks, run `pre-commit install`. TODO: verify with CI, must pass these to approve pr

5. Use Commitizen for conventional commits.

   Commitizen is a tool to help you write conventional commit messages. To use Commitizen, run `cz c`. TODO: verify with CI, must commit with conventional commit format

### Working with Poetry

When developing a Poetry project like this one, it is recommended to use the Poetry shell exclusively. This allows Poetry to manage the Python environment and dependencies for you. To activate the Poetry shell, run `poetry shell` (many IDEs will integrate your developer console with the virtual environment but it's good to be sure for consistency). From then on, you can use the `poetry` command to manage dependencies and run your project. The Poetry shell is a virtual environment that is separate from the system Python environment, allowing you to isolate your project's dependencies. It replaces the built-in package manager pip in the context of this project. It is similar to npm for JavaScript and pipenv for Python.

To declare a dependency in your project, you can use the `poetry add` command. E.g., to declare a dependency on the requests library, you can run `poetry add requests`. Poetry will then install the dependency and add it to the list of dependencies in the pyproject.toml file.

To install all declared dependencies, you can run `poetry install`. Poetry will then install all declared dependencies and their dependencies.

You can also use the `poetry remove` command to remove a dependency from your project. E.g., to remove the requests library, you can run `poetry remove requests`.

## Usage

Please answer the following questions to help define the usage of your project:

- What is the main purpose of your project?
- What are the main features of your project?
- How should users run your project?
- What are the expected inputs and outputs of your project?
- Are there any specific command line arguments or options?
- Are there any specific environment variables to be set?
- Are there any specific dependencies to be installed?

### Getting Started

1. Run the project: `poetry install; python -m <project_name>`
   - What are the common uses? Anything more than running main?

### Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request.

## License and Copyright

- License: GNU AFFERO GENERAL PUBLIC LICENSE
- Copyright: {% now 'utc', '%Y' %}, {{ cookiecutter.author_name }}

## Contact

- Author: [Author Name](mailto:skylar.donlevy.dev@gmail.com)
