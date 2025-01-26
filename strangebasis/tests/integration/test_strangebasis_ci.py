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


@pytest.mark.parametrize("args", [["-h", "--help"]])
def test_strangebasis_help(args: list[str]) -> None:
    """
    Test running the `strangebasis` module with the help argument on the command line.

    Args:
        args (list[str]): The arguments to pass to the `strangebasis` command.
    """
    process = subprocess.run(
        ["poetry", "run", sys.executable, "-m", "strangebasis"] + args,
        capture_output=True,
        text=True,
        check=False,
    )
    assert (
        process.stdout.strip()
        == "usage: strangebasis [-h] {hello} ...\n\nStrange Basis CLI\n\npositional arguments:\n  {hello}\n    hello     Say hello\n\noptions:\n  -h, --help  show this help message and exit"
    )
    # a subprocess closing expectedly ALWAYS returns 0 (TODO: test the help function via unit tests to validate other behavior)
    assert process.returncode == 0
    assert process.stderr == ""
