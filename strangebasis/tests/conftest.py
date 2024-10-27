# This "Strange Basis" serves as a baseline of productivity across my body of work. It's a system that works best for me; my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy

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
