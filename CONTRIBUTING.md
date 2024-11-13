# Contributing to strangebasis

Thank you for your interest in contributing to this project! This document provides guidelines and standards for contributing, from branching and versioning conventions to commit messages and pull request expectations.

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

## Automated Versioning and Changelog

Upon merging a release or hotfix branch to `main`, GitHub Actions automatically:

- Bumps the version based on commit types (following [SemVer](https://semver.org/)).
- Generates a `CHANGELOG.md` using Commitizen.
- Pushes the updated version and changelog to `main`.

## Testing and Coverage

Before submitting code, ensure:

- All tests pass (`pytest` is used for testing).
- Code coverage is sufficient and no new issues are introduced.
- Coverage reports are uploaded to CodeClimate via GitHub Actions.

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

3. [Optional] Run the hooks against all files to check for any existing issues (likely an extra step on clean clone):

```bash
pre-commit run --all-files
```

Pre-commit hooks will now run automatically on each commit, helping to maintain code quality and consistency.

## Submitting a Pull Request

1. **Fork** the repository and create your feature branch as described above.
2. Make commits following the conventional commit standard.
3. Ensure tests pass locally.
4. Push your branch and open a **Pull Request** to `develop`.
5. The Pull Request will trigger GitHub Actions to run tests and update coverage.

Thank you for contributing! We’re excited to have you collaborate on this project. If you have questions or suggestions, feel free to open an issue.
