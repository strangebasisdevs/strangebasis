# {{cookiecutter.project_name}}
#     Copyright (C) {% now 'utc', '%Y' %}  {{ cookiecutter.author_name }}
"""
Tests for {{cookiecutter.project_name}}.

These tests verify that the module can be installed via Poetry before other
tests are run. The "session" scope means that this fixture is only run once
before all tests, and "autouse" means that it is automatically applied to all
tests.
"""
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
