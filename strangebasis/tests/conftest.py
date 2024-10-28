# This "Strange Basis" is my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy
"""
Tests for the strangebasis module using pytest.

This file contains fixture definitions and configuration settings for tests.
The conftest.py file is commonly used in pytest projects to define fixtures
that can be shared across multiple test files, and to configure pytest settings.
"""
import subprocess

import pytest


@pytest.fixture(scope="session", autouse=True)
def ensure_package_installed() -> None:
    """Ensure that the package is installed via Poetry before tests.

    Returns:
        None
    """
    try:
        # Check if the package is installed
        subprocess.check_call(["poetry", "install"])
    except subprocess.CalledProcessError:
        pytest.exit("Poetry install failed. Please check your installation.")
