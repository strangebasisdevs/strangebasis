# This "Strange Basis" serves as a baseline of productivity across my body of work. It's a system that works best for me; my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy

import subprocess
import sys

import pytest


@pytest.mark.parametrize("args", [["hooks"]])
def test_strangebasis_hooks(args: list[str]) -> None:
    """
    Test running the `strangebasis` command with the `hooks` argument. This is
    redundant since `pre-commit` hooks should be run automatically.

    Args:
        args (list[str]): The arguments to pass to the `strangebasis` command.
    """
    process = subprocess.run(
        [sys.executable, "-m", "strangebasis"] + args,
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode == 0
    assert "failed" not in process.stdout.lower()
    assert process.stderr == ""
