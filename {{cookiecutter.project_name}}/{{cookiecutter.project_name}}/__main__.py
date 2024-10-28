# {{cookiecutter.project_name}}
#     Copyright (C) {% now 'utc', '%Y' %}  {{ cookiecutter.author_name }}
"""
{{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Author: {{ cookiecutter.author_name }}
"""


def main() -> int:
    """
    Main entry point for the {{ cookiecutter.project_name }} module.

    This function prints a greeting message and returns an integer
    indicating successful execution.

    Returns:
        int: The exit status of the execution, where 0 indicates success.
    """
    print("Hello from {{ cookiecutter.project_name }}!")

    return 0


if __name__ == "__main__":
    main()
