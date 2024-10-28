# This "Strange Basis" is my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy
"""
strangebasis

This is my personal digital toolbox and a module to port all of my
coding standards into my other projects. Cookiecutter perfection.

"""
import argparse

import pre_commit.main


def main() -> None:
    """
    Entry point for the Strange Basis command-line interface (CLI).

    This function sets up the argument parser for the CLI, adding
    a subparser for the "hooks" command. If a valid command is
    provided, it calls the corresponding function with the parsed
    arguments.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Strange Basis CLI")
    subparsers = parser.add_subparsers(dest="command")

    hooks_parser = subparsers.add_parser("hooks", help="Run shared hooks")
    hooks_parser.set_defaults(func=hooks)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


def hooks() -> int:
    """
    Run all pre-commit hooks on the entire repository.

    This function runs all the pre-commit hooks on all files in the
    repository. If any of the hooks fail, the function prints a message
    indicating that some hooks failed and returns the appropriate exit
    status.

    Returns:
        int: The exit status of the pre-commit hook runner. If all hooks
            passed, this is 0; otherwise, it is a non-zero value indicating
            that some hooks failed.
    """
    result: int = pre_commit.main.main(["run", "--all-files"])

    if result == 0:
        print("All pre-commit hooks passed!")
    else:
        print("Some pre-commit hooks failed.")
    return result


if __name__ == "__main__":
    main()
