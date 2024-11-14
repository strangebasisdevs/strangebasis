# Contributing to Strangebasis

Thank you for your interest in contributing to Strangebasis! Follow these steps to ensure your contributions are well-prepared and align with the project's standards.

## Quick Links

- [Getting Started](#getting-started): Essential for setting up your local development environment.
- [Development Environment Setup](#development-environment-setup): Detailed steps to configure your tools and dependencies.
- [Contribution Workflow](#contribution-workflow): Guidelines for creating branches, making changes, and ensuring code quality.
- [Creating a Pull Request](#creating-a-pull-request): Instructions for submitting your changes for review.
- [Pre-commit Hooks](#pre-commit-hooks): Ensures code quality and consistency before committing changes.

## Table of Contents

[TOC]

## First Time Setup

### Getting Started

1. **Fork the Repository**: Fork the repository on GitHub to your account.

2. **Clone the Repository**: Clone your forked repository to your local machine:
   ```sh
   git clone https://github.com/<your-username>/strangebasis.git
   cd strangebasis
   ```

### Development Environment Setup

1. **Install Poetry**: If not already installed, install Poetry:

   ```sh
   pip install poetry
   ```

2. **Install Dependencies**: Install the project dependencies and development tools:

   ```sh
   poetry install
   ```

3. **Activate the Poetry Shell**: To ensure all following commands use the virtual environment managed by Poetry, activate the Poetry shell:

   ```sh
   poetry shell
   ```

4. **Install Pre-commit Hooks**: Using pre-commit hooks helps us maintain a high standard of code quality and consistency across the project:

   ```sh
   pre-commit install
   ```

5. **[Optional] Run Pre-commit Hooks**: Run pre-commit hooks against all files to check for any existing issues:

   ```sh
   pre-commit run --all-files
   ```

6. **Run Tests**: Run tests locally to verify everything is set up correctly:
   ```sh
   pytest
   ```

## Contribution Workflow

1. **Create a Branch**: Create a new branch for your feature or bugfix:

   ```sh
   git checkout -b <branch-name>
   ```

2. **Make Changes**: Make your changes to the codebase.

3. **Run Pre-commit Hooks**: Ensure your changes pass pre-commit hooks:
   ```sh
   pre-commit run --all-files
   ```

### Writing and Running Tests

1. **Write Tests**: Ensure your changes are covered by tests. Add new tests if necessary.

2. **Run Tests**: Run the test suite to verify that all tests pass:
   ```sh
   pytest
   ```

### Committing and Pushing Changes

1. **Commit Your Changes**: Use Commitizen to ensure your commit messages follow the conventional commit format:

   ```sh
   git add .
   cz commit
   ```

2. **Push to Your Fork**: Push your branch to your forked repository:
   ```sh
   git push origin <branch-name>
   ```

### Creating a Pull Request

1. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request from your branch.

### Responding to Feedback

1. **Be Responsive**: Be responsive to any feedback or requests for changes from the project maintainers.

By following this checklist, you can ensure that your contributions are well-prepared and align with the project's standards. Thank you for contributing to Strangebasis!

## Development Paradigms and Tools

This project follows the **Git Flow** branching strategy:

- **`main`**: The production-ready branch, containing stable releases.
- **`develop`**: The integration branch for the next release.
- **Feature branches** (`feature/<feature-name>`): Branches off `develop` for new features or updates.
- **Release branches** (`release/<version>`): Used to prepare for an upcoming release. Once stable, it’s merged into `main`.
- **Hotfix branches** (`hotfix/<version>`): For urgent fixes applied to `main`.

### Branching and Merging Process

1. **Creating Feature Branches**: When working on a new feature or fix:

- Branch from `develop` with the naming convention: `feature/<feature-name>` or `fix/<issue-description>`.
- Make sure each branch addresses a single feature or issue for clear, isolated changes.

2. **Pull Requests**:

- Open pull requests (PRs) to merge changes back into `develop`.
- Ensure PRs are descriptive, referencing any related issue numbers.
- Each PR should include relevant test cases, and all tests should pass.
- Once code on `develop` is stable and ready for a new release, a release branch (`release/<version>`) will be created.

3. **Releases and Hotfixes**:

- To start a release, create a `release/<version>` branch from `develop`.
- For urgent fixes, create a `hotfix/<version>` branch from `main`.
- Releases and hotfixes will be merged back to both `main` and `develop` to ensure consistency.

### Submitting a Pull Request

1. **Fork** the repository and create your feature branch as described above.
2. Make commits following the conventional commit standard.
3. Ensure tests pass locally.
4. Push your branch and open a **Pull Request** to `develop`.
5. The Pull Request will trigger GitHub Actions to run tests and update coverage.

### Pre-commit Hooks

This project uses **pre-commit** to ensure code quality and consistency. Before making commits, configure your environment to use the pre-commit hooks defined in [`.pre-commit-config.yaml`](../.pre-commit-config.yaml).
Refer to [getting_started.md](getting_started.md) for details on first time setup and [pre-commit.md](pre-commit.md) for details on each check.

### Testing and Coverage

Before submitting code, ensure:

- All tests pass (`pytest` is used for testing).
- Code coverage is sufficient and no new issues are introduced.

### Automated Versioning and Changelog

Upon merging a release or hotfix branch to `main`, GitHub Actions automatically:

- Bumps the version based on commit types (following [SemVer](https://semver.org/)).
- Generates a `CHANGELOG.md` using Commitizen.
- Pushes the updated version and changelog to `main`. (this extra git push cannot typically trigger other github actions)

### Commit Conventions

This project uses **[Commitizen](https://github.com/commitizen-tools/commitizen)** to enforce commit message conventions and automate versioning.

> **Note**: Commitizen can be installed along with project dependencies and other development dependencies in the Poetry setup of the [Getting Started](getting_started.md) documentation.

#### Writing Conventional Commits

Follow the structure: `<type>(scope): <message>`. Common types include:

- **feat**: New features
- **fix**: Bug fixes
- **chore**: Maintenance or non-functional updates
- **docs**: Documentation-only changes
- **test**: Adding or modifying tests

Example commits:

```plaintext
feat(auth): add user authentication via OAuth
fix(api): resolve response timeout issue
chore(deps): update dependencies
```

#### Using Commitizen for Commits

Use Commitizen’s CLI tool for structured commits:

```bash
cz commit
```

Commitizen will prompt you for details and format the commit message correctly.

---

We’re excited to have you collaborate on this project. If you have questions or suggestions, feel free to [open an issue](https://github.com/strangebasis/strangebasis/issues).
