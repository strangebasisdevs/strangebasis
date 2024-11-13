# Contributing to strangebasis

Thank you for your interest in contributing to this project! This document provides guidelines and standards for contributing, from branching and versioning conventions to commit messages and pull request expectations.
For first-time setup, please refer to the [Getting Started](getting_started.md) docs for detailed instructions on setting up your development environment.

## Pre-commit Hooks

This project uses pre-commit for managing pre-commit hooks.
Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks.
It ensures that code meets certain standards before it is committed to the repository.
Refer to getting_started.md for details on first time setup and pre_commit.md for details on each check.

## Automated Versioning and Changelog

Upon merging a release or hotfix branch to `main`, GitHub Actions automatically:

- Bumps the version based on commit types (following [SemVer](https://semver.org/)).
- Generates a `CHANGELOG.md` using Commitizen.
- Pushes the updated version and changelog to `main`. (this extra git push cannot typically trigger other github actions)

## Testing and Coverage

Before submitting code, ensure:

- All tests pass (`pytest` is used for testing).
- Code coverage is sufficient and no new issues are introduced.

## Pre-commit Hooks

This project uses **pre-commit** to ensure code quality and consistency. Before making commits, configure your environment to use the pre-commit hooks defined in `.pre-commit-config.yaml`.
Look at the blah blah blah section in the getting started documentation for detailed instructions on setting up pre-commit in your development environment.

## Submitting a Pull Request

1. **Fork** the repository and create your feature branch as described above.
2. Make commits following the conventional commit standard.
3. Ensure tests pass locally.
4. Push your branch and open a **Pull Request** to `develop`.
5. The Pull Request will trigger GitHub Actions to run tests and update coverage.

## Development Workflow

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

## Commit Conventions

This project uses **[Commitizen](https://github.com/commitizen-tools/commitizen)** to enforce commit message conventions and automate versioning.

> **Note**: Commitizen can be installed along with project dependencies and other development dependencies in the Poetry setup of the [Getting Started](getting_started.md) documentation.

### Writing Conventional Commits

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

### Using Commitizen for Commits

Use Commitizen’s CLI tool for structured commits:

```bash
cz commit
```

Commitizen will prompt you for details and format the commit message correctly.

---

We’re excited to have you collaborate on this project. If you have questions or suggestions, feel free to open an issue.
