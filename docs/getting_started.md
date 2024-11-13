# Getting Started with strangebasis

Welcome to the strangebasis project! This guide will help you get started with generating new projects using Cookiecutter, setting up your development environment, testing your changes locally, and contributing to the repository.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.12
- pip (Python package installer)

### Running Cookiecutter

To generate a project based on different versions of this repository, follow these steps:

1. **Install Cookiecutter**:
   Ensure you have Cookiecutter installed:

   ```sh
   pip install cookiecutter
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

### Contribution/Development Prep

The following section outlines the

## Installation and Setup

### First Time Project Setup

These steps will guide you through the initial setup of the strangebasis project.

## Setting Up Your Development Environment

1. Clone the repository and create a virtual environment.
2. Install dependencies:

   ```bash
   pip install poetry
   ```

3. Install Commitizen and other development dependencies:

   ```bash
   poetry install
   ```

4. Run tests locally to verify everything is set up correctly:
   ```bash
   poetry run pytest
   ```

### Configuring Pre-commit Hooks

To ensure code quality and consistency, we use pre-commit hooks. Follow these steps to set them up:

1. Install `pre-commit`:

```bash
pip install pre-commit
```

2. Install the pre-commit hooks defined in the repository:

```bash
pre-commit install
```

3. [Optional] Run the hooks against all files to check for any existing issues (likely an extraneous step on clean clone):

```bash
pre-commit run --all-files
```

Pre-commit hooks will now run automatically on each commit, helping to maintain code quality and consistency.

1. **Install Python 3.12**:
   Ensure you have Python 3.12 installed. Verify the installation by running:

   ```sh
   python --version
   ```

2. **Install Poetry**:
   Poetry is used for dependency management. Install Poetry using pip if you have not installed it before:

   ```sh
   python -m pip install poetry
   ```

3. **Initialize the Project**:
   Install the project dependencies and activate the virtual environment:

   ```sh
   poetry install
   poetry shell
   ```

4. **Initialize Git Repository**:
   Initialize a new Git repository and add all files:

   ```sh
   git init
   git add -A
   ```

5. **Set Up Pre-commit Hooks**:
   Pre-commit hooks help enforce coding standards. Install the pre-commit hooks:

   ```sh
   pre-commit install
   pre-commit run --all-files
   ```

6. **Run Tests**:
   Run the test suite to ensure everything is set up correctly:

   ```sh
   pytest
   ```

7. **Make Your First Commit**:
   Use Commitizen to make your first commit:
   ```sh
   cz c
   ```

## Contributing

We welcome contributions to the strangebasis project. Follow these steps to contribute:

1. **Fork the Repository**:
   Fork the repository on GitHub: [strangebasisdevs/strangebasis](https://github.com/strangebasisdevs/strangebasis)

2. **Create a Feature Branch**:
   Create a new branch for your feature or fix:

   ```sh
   git checkout -b feature/fooBar
   ```

3. **Make Changes**:
   Make your changes and commit them using conventional commit messages.

4. **Push to the Branch**:
   Push your changes to your forked repository:

   ```sh
   git push origin feature/fooBar
   ```

5. **Create a Pull Request**:
   Open a pull request to merge your changes back into the main repository.

## Testing Locally

To test your changes locally, ensure you are in the Poetry shell. If not, activate it by running:

```sh
poetry shell
```

1. **Install Dependencies**:
   Install the project dependencies:

   ```sh
   poetry install
   ```

2. **Run Tests**:
   Run the test suite to verify your changes:
   ```sh
   pytest
   ```

## Additional Resources

For more detailed information, refer to the following resources:

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/en/latest/)
- [Commitizen Documentation](https://commitizen-tools.github.io/commitizen/)

Thank you for contributing to strangebasis! If you have any questions or need further assistance, feel free to open an issue on GitHub.
