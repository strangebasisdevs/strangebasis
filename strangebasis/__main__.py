# This "Strange Basis" is my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy
"""
The strangebasis module.

This is my personal digital toolbox and a module to port all of my
coding standards into my other projects. Cookiecutter perfection.

"""
import argparse


def main() -> None:
    """
    Entry point for the Strange Basis command-line interface (CLI).

    This function sets up the argument parser for the CLI, adding
    a subparser for the "hello" command. If a valid command is
    provided, it calls the corresponding function with the parsed
    arguments.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Strange Basis CLI", prog="strangebasis")
    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser("hello", help="Say hello")
    hello_parser.set_defaults(func=hello)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


def hello(args: argparse.Namespace) -> int:
    """
    Print a hello message.

    This function prints "Hello strange world!" to the console.

    Args:
        args: The command-line arguments passed to the function.

    Returns:
        int: Always returns 0.
    """
    _ = args
    print("Hello strange world!")
    return 0


if __name__ == "__main__":
    main()
