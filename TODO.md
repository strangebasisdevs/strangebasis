### Categorization of Hooks

#### Core Hooks:

- ~~**commitizen**: Ensures commit message standards.~~
- ~~**trailing-whitespace**: Removes trailing whitespace.~~
- ~~**end-of-file-fixer**: Ensures files end with a newline.~~
- ~~**check-yaml**: Validates YAML files.~~
- ~~**check-added-large-files**: Prevents large files from being added.~~
- ~~**check-case-conflict**: Checks for case conflicts in filenames.~~
- ~~**check-json**: Validates JSON files.~~
- ~~**check-merge-conflict**: Detects merge conflict markers.~~
- ~~**check-toml**: Validates TOML files.~~
- ~~**debug-statements**: Detects debug statements.~~
- **python-check-mock-methods**: Checks for mock method usage.
- **rst-backticks**: Ensures correct usage of backticks in reStructuredText files.
- ~~**bashate**: Lints bash scripts.~~

#### Style Hooks:

- **isort**: Sorts imports.
- **prettier**: Formats code according to Prettier standards.
- **blacken-docs**: Formats Python code in documentation.
- **pylint**: Lints Python code (with specific settings).

#### Strangebasis (Repo Specific) Hooks:

- **pylint**: Custom entry and settings specific to this repository.

### Draft Nitpick Syntax to Enforce Hooks

#### `nitpick/core-pre-commit.toml`

```toml
[nitpick.meta]
name = "core-pre-commit"
url = "https://github.com/your-repo/nitpick/core-pre-commit.toml"

[".pre-commit-config.yaml".repos]
repo = "https://github.com/commitizen-tools/commitizen"
rev = "v3.30.1"
hooks = [{id = "commitizen", stages = ["commit-msg"]}]

[".pre-commit-config.yaml".repos]
repo = "https://github.com/pre-commit/pre-commit-hooks"
rev = "v5.0.0"
hooks = [
    {id = "trailing-whitespace"},
    {id = "end-of-file-fixer"},
    {id = "check-yaml"},
    {id = "check-added-large-files"},
    {id = "check-case-conflict"},
    {id = "check-json"},
    {id = "check-merge-conflict"},
    {id = "check-toml"},
    {id = "debug-statements"}
]

[".pre-commit-config.yaml".repos]
repo = "https://github.com/pre-commit/pygrep-hooks"
rev = "v1.10.0"
hooks = [
    {id = "python-check-mock-methods"},
    {id = "rst-backticks"}
]

[".pre-commit-config.yaml".repos]
repo = "https://github.com/openstack/bashate"
rev = "2.1.1"
hooks = [{id = "bashate", args = ["-i", "E006"]}]
```

#### `nitpick/style-pre-commit.toml`

```toml
[nitpick.meta]
name = "style-pre-commit"
url = "https://github.com/your-repo/nitpick/style-pre-commit.toml"

[".pre-commit-config.yaml".repos]
repo = "https://github.com/pycqa/isort"
rev = "5.13.2"
hooks = [{id = "isort"}]

[".pre-commit-config.yaml".repos]
repo = "https://github.com/pre-commit/mirrors-prettier"
rev = "v4.0.0-alpha.8"
hooks = [{id = "prettier", stages = ["pre-commit"]}]

[".pre-

commit

-config.yaml".repos]
repo = "https://github.com/asottile/blacken-docs"
rev = "1.19.1"
hooks = [{id = "blacken-docs", additional_dependencies = ["black==23.7.0"]}]
```

####

strangebasis-pre-commit.toml

```toml
[nitpick.meta]
name = "strangebasis-pre-commit"
url = "https://github.com/your-repo/nitpick/strangebasis-pre-commit.toml"

[".pre-commit-config.yaml".repos]
repo = "local"
hooks = [
    {
        id = "pylint",
        name = "pylint",
        entry = "poetry run pylint --disable=C0103",
        language = "system",
        exclude = "tests/",
        types = ["python"]
    }
]
```

### Update `core.toml`, `style.toml`, and `strangebasis.toml`

#### `core.toml`

```toml
[nitpick.meta]
name = "core"
url = "https://github.com/your-repo/nitpick/core.toml"

[".pre-commit-config.yaml".include]
files = ["nitpick/core-pre-commit.toml"]
```

#### `style.toml`

```toml
[nitpick.meta]
name = "style"
url = "https://github.com/your-repo/nitpick/style.toml"

[".pre-commit-config.yaml".include]
files = ["nitpick/style-pre-commit.toml"]
```

#### `strangebasis.toml`

```toml
[nitpick.meta]
name = "strangebasis"
url = "https://github.com/your-repo/nitpick/strangebasis.toml"

[".pre-commit-config.yaml".include]
files = ["nitpick/strangebasis-pre-commit.toml"]
```

This approach ensures that core, style, and project-specific pre-commit hooks are properly categorized and enforced using Nitpick.
