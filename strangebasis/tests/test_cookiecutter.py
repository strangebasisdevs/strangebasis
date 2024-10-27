# This "Strange Basis" serves as a baseline of productivity across my body of work. It's a system that works best for me; my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy

import os
import subprocess

import pytest


@pytest.mark.parametrize("output_dir", ["generated_project"])
def test_cookiecutter_project_creation(output_dir: str) -> None:
    """
    Test running cookiecutter on the local directory structure.

    Args:
        output_dir (str): The name of the directory to be generated by cookiecutter.
    """
    try:
        # Run cookiecutter on the current directory
        subprocess.run(["cookiecutter", "."], check=True)

        # Verify that the project directory was created
        assert os.path.isdir(output_dir)

        # Optionally, check for existence of expected files
        expected_files = ["README.md", "pyproject.toml"]
        for file in expected_files:
            assert os.path.isfile(os.path.join(output_dir, file))

    finally:
        # Clean up by removing the generated directory
        # Temporarily comment out the removal of the generated directory
        # if os.path.isdir(output_dir):
        #     subprocess.run(["rm", "-rf", output_dir])

        # Print instructions for manually testing the generated project
        print(
            f"To manually test the generated project, navigate to '{output_dir}' and run your desired test commands."
        )
