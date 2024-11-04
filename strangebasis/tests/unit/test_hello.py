import argparse
import sys
from io import StringIO

import pytest

from strangebasis.__main__ import hello


# This parameterized test will only be needed if the `hello` function is expanded to accept arguments.
@pytest.mark.parametrize("args", [argparse.Namespace(command="hello")])
def test_strangebasis_hello(args: argparse.Namespace) -> None:
    """
    Test running `hello` method individually from the `strangebasis` module.

    Args:
        args (argparse.Namespace): The arguments to pass to the `strangebasis` command.
    """
    # Capture the output
    captured_output = StringIO()
    sys.stdout = captured_output

    result = hello(args)

    # Reset redirect.
    sys.stdout = sys.__stdout__

    # Check the result and the output
    assert result == 0
    assert captured_output.getvalue().strip() == "Hello strange world!"
