# {{cookiecutter.project_name}}
#     Copyright (C) {% now 'utc', '%Y' %}  {{ cookiecutter.author_name }}
"""
Tests for{{cookiecutter.project_name}}.

These tests verify the module can be called from the command line.

Author: {{cookiecutter.author_name}}
"""
import subprocess
import sys


def test_module() -> None:
    """
    Test calling the module from the command line.

    Args:
        capsys (pytest.CaptureFixture[str]): Pytest fixture to capture stdout & stderr.

    Returns:
        None
    """
    module_run_result = subprocess.run(
        ["poetry", "run", sys.executable, "-m", "{{cookiecutter.project_name}}"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert module_run_result.returncode == 0
    assert module_run_result.stdout.strip() == "Hello from {{cookiecutter.project_name}}!"
    assert module_run_result.stderr == ""


# def test_main() -> None:
#     """
#     Test calling the main function directly.

#     Args:
#         capsys (pytest.CaptureFixture[str]): Pytest fixture to capture stdout & stderr.

#     Returns:
#         None
#     """
#     from {{cookiecutter.project_name}} import main

#     assert main() == 0
