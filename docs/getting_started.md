# Getting Started with strangebasis

Welcome to the strangebasis project! This guide will help you get started with generating new projects using Cookiecutter, setting up your development environment, testing your changes locally, and contributing to the repository.

## Quick Links

- [Using strangebasis (Users)](#using-strangebasis)
  - Setup Time ~2 minutes
- [Contributing to strangebasis (Developers)](#contributing-to-strangebasis)
  - Setup Time ~10 minutes
- [Advanced Topics](#advanced-topics)

## Table of Contents

[TOC]

## System Requirements

The strangebasis project is tested and supported on the following operating systems:

- Ubuntu
- macOS
- Windows

No minimum specs have been identified, generally if you can run the OS, you can run this.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.12
- pip (Python package installer)
- Git (for development/contribution)

Validate the above prereqs with the following steps:

1. **Verify you are using Python 3.12**:
   Ensure you have Python 3.12 installed (and ideally on your Path) by examining the output of the following:

   ```sh
   python --version
   ```

2. **Verify Python 3.12 can pip**:
   Ensure your Python 3.12 installation has pip by examining the output of the following:

   ```sh
   python -m pip --version
   ```

## Using strangebasis

### Cookiecutter Quick Start

1. Install cookiecutter: `pip install cookiecutter`
2. Generate project: `cookiecutter gh:strangebasisdevs/strangebasis`
3. Follow first-time setup in generated project

### Detailed Cookiecutter Steps

To generate a project based on different versions of this repository, follow these steps:

1. **Install Cookiecutter**:
   Ensure you have Cookiecutter installed:

   ```sh
   python -m pip install cookiecutter
   ```

2. **Generate a Project**:
   Run Cookiecutter with the desired version:

   - For the latest version from the main branch:
     ```sh
     cookiecutter gh:strangebasisdevs/strangebasis
     ```
   - For a specific version or tag:
     ```sh
     cookiecutter gh:strangebasisdevs/strangebasis --checkout <tag_or_branch_name>
     ```
     Replace `<tag_or_branch_name>` with the specific tag or branch you want to use.

3. **Navigate to the Generated Project**:
   Change directory to the newly generated project:

   ```sh
   cd <generated_project_directory>
   ```

4. **Follow First Time Project Setup**:
   Follow the steps outlined in the section "[Cookiecut First Time Setup](./{{cookiecutter.project_name}}/docs/getting_started.md#cookiecut-first-time-setup)" followed by the "[Developer First Time Setup](./{{cookiecutter.project_name}}/docs/getting_started.md#developer-first-time-setup)" in the `docs/getting_started.md` of the generated project to ensure proper configuration of Git, CI, and pre-commit integration.

## Contributing to strangebasis

### Development Quick Start

1. Clone repo: `git clone https://github.com/strangebasisdevs/strangebasis.git`
2. Setup dev environment: `poetry install`
3. Enter dev shell: `poetry shell`
4. Install pre-commit `pre-commit install`
5. Run tests: `pytest`

For detailed steps on setting up your development environment, please refer to the documenation on [Development Environment Setup](contributing.md#development-environment-setup).

### IDE Configuration

Visual Studio Code can automatically detect and use the virtual environment created by Poetry, making it easier to work on your project. This integration should ensure that all terminals started from your IDE already activate the virtual environment.

1. **Install the Python Extension**:

- Open Visual Studio Code.
- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
- Search for "Python" and install the extension provided by Microsoft.

2. **Select the Python Interpreter**:

- Open the Command Palette by pressing `Ctrl+Shift+P`.
- Type `Python: Select Interpreter` and select it.
- Choose the interpreter that corresponds to your virtual environment. If you are using Poetry, it should be listed as something like `.venv/bin/python` or similar.

3. **Activate the Virtual Environment in the Terminal**:

- Open a new terminal in VS Code.
- If you have already activated the Poetry shell, VS Code should automatically use the virtual environment. If not, you can manually activate it by running:

  ```sh
  poetry shell
  ```

By following these steps, Visual Studio Code will recognize and use the Python virtual environment created by Poetry or any other virtual environment tool.

## Advanced Topics

### Best Practices

Following these best practices will help ensure a smooth and efficient development process:

#### Code Quality

- **Write Clean Code**: Follow repo style and linting guidelines for Python code to maintain readability and consistency.
- **Use Type Annotations**: Add type hints to your functions and methods to improve code clarity and facilitate static analysis.
- **Document Your Code**: Use docstrings to document the purpose and usage of your functions, classes, and modules.

#### Version Control

- **Commit Often**: Make small, frequent commits with clear and descriptive messages.
- **Use Branches**: Create feature branches for new features or bug fixes to keep the main branch stable.
- **Rebase and Merge**: Rebase your feature branch before merging to keep the commit history clean.

#### Testing

- **Write Tests**: Ensure that all new features and bug fixes are covered by tests.
- **Run Tests Frequently**: Run the test suite regularly to catch issues early.
- **Use Test Coverage Tools**: Utilize tools like `coverage.py` to monitor and improve test coverage. Integrate with CodeClimate where possible.

#### Collaboration

- **Code Reviews**: Participate in code reviews to share knowledge and improve code quality.
- **Follow Contribution Guidelines**: Adhere to [the project's contribution guidelines](contributing.md) to ensure a smooth review and merge process.
- **Communicate Effectively**: Use clear and concise communication in pull requests, issues, and commit messages.

#### Continuous Integration

- **Automate Testing**: Set up continuous integration (CI) to automatically run tests on each push and pull request.
- **Manage Code Complexity**: Set up CodeClimate to monitor code complexity and keep projects maintainable.
- **Track Code Coverage**: Integrate CodeClimate coverage reporting to make sure new code gets decent exposure/coverage.

By adhering to these best practices, you will contribute to a more maintainable, efficient, and collaborative project environment.

### Local Testing

To test your changes locally, ensure you are in the Poetry Shell and have followed the [Developer First Time Setup](#developer-first-time-setup).

1. **Install Project**:
   Install the project dependencies **AND** the project's python package itself:

```sh
poetry install
```

2. **Run Tests**:
   Run the test suite to verify your changes:

```sh
pytest
```

## Troubleshooting

- **Poetry or pip install fails because Python 3.12 is not installed**: This error typically occurs when the required version of Python is not installed or not correctly set up in your system's PATH. Follow these steps to troubleshoot and verify the prerequisites:

  1. **Check Python Installation**:
     Ensure Python 3.12 is installed by running:

     ```sh
     python --version
     ```

     The output should be `Python 3.12.x`. If not, download and install Python 3.12 from the [official Python website](https://www.python.org/downloads/).

  2. **Verify Python Path**:
     Ensure Python 3.12 is added to your system's PATH. This allows the system to locate the Python executable. You can check this by running:

     ```sh
     echo $PATH
     ```

     Ensure the output includes the path to your Python 3.12 installation directory.

  3. **Check pip Installation**:
     Verify that pip is installed and associated with Python 3.12 by running:

     ```sh
     python -m pip --version
     ```

     If pip is not installed, you can install it using:

     ```sh
     python -m ensurepip --upgrade
     ```

  4. **Reinstall Poetry**:
     If Python 3.12 is correctly installed and in your PATH, but Poetry still fails, try reinstalling Poetry:

     ```sh
     pip install --user poetry
     ```

  5. **Environment Variables**:
     Ensure that your environment variables are correctly set up to use Python 3.12 and pip. This might involve updating your shell configuration files (e.g., `.bashrc`, `.zshrc`, or `.bash_profile`).

  By following these steps, you should be able to resolve issues related to Python 3.12 not being installed or not correctly configured, allowing Poetry and pip to function properly.

- **pytest fails after following these steps**
- **pre-commit fails on initial run**
- **Something is difficult to understand or gives you a headache**

  Open a GitHub issue to report the problem and seek assistance.

## Additional Resources

For more detailed information, refer to the following resources:

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/en/latest/)
- [Commitizen Documentation](https://commitizen-tools.github.io/commitizen/)

Thank you for contributing to strangebasis! If you have any questions or need further assistance, feel free to open an issue on GitHub.

## Support

If you encounter any issues or have questions, feel free to reach out for support:

- **Email**: [strangebasistv@gmail.com](mailto:strangebasistv@gmail.com)
- **GitHub Issues**: [Open an issue](https://github.com/strangebasisdevs/strangebasis/issues)
- **Community Chat**: [Join our Discord](https://discord.gg/dExsuHjN)

We are here to help and appreciate your feedback and contributions!
