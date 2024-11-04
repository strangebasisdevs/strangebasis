import subprocess
import sys

import pytest


@pytest.mark.parametrize("args", [["hello"]])
def test_strangebasis_hello(args: list[str]) -> None:
    """
    Test running the `strangebasis` module on the command line.

    Args:
        args (list[str]): The arguments to pass to the `strangebasis` command.
    """
    process = subprocess.run(
        ["poetry", "run", sys.executable, "-m", "strangebasis"] + args,
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.stdout == "Hello strange world!\n"
    assert process.returncode == 0
    assert process.stderr == ""
