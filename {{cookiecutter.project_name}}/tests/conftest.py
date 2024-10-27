# {{cookiecutter.project_name}}
#     Copyright (C) {% now 'utc', '%Y' %}  {{ cookiecutter.author_name }}

import subprocess

import pytest


@pytest.fixture(scope="session", autouse=True)
def ensure_package_installed() -> None:
    """Ensure that the package is installed via Poetry before tests."""
    try:
        # Check if the package is installed
        subprocess.check_call(["poetry", "install"])
    except subprocess.CalledProcessError:
        pytest.exit("Poetry install failed. Please check your installation.")
