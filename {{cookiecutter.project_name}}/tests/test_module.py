# {{cookiecutter.project_name}}
#     Copyright (C) {% now 'utc', '%Y' %}  {{ cookiecutter.author_name }}
"""
Tests for{{cookiecutter.project_name}}.

These tests verify the module can be called from the command line.

Author: {{cookiecutter.author_name}}
"""
import subprocess


def test_module() -> None:
    """
    Test calling the module from the command line.

    Args:
        capsys (pytest.CaptureFixture[str]): Pytest fixture to capture stdout & stderr.

    Returns:
        None
    """
    module_run_result = subprocess.run(
        ["python", "-m", "{{cookiecutter.project_name}}"],
        capture_output=True,
        check=True,
    )

    assert module_run_result.returncode == 0
    assert module_run_result.stdout.decode().strip() == "Hello from {{cookiecutter.project_name}}!"
    assert module_run_result.stderr.decode() == ""
