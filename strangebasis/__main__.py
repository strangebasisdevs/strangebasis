# This "Strange Basis" serves as a baseline of productivity across my body of work. It's a system that works best for me; my digital toolbox. Use at your own risk.
#     Copyright (C) 2024  Skylar DonLevy

import argparse

import pre_commit.main


def main() -> None:
    parser = argparse.ArgumentParser(description="Strange Basis CLI")
    subparsers = parser.add_subparsers(dest="command")

    hooks_parser = subparsers.add_parser("hooks", help="Run shared hooks")
    hooks_parser.set_defaults(func=hooks)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


def hooks(args: argparse.Namespace) -> int:
    # parser = argparse.ArgumentParser(description="Run shared hooks")

    result: int = pre_commit.main.main(["run", "--all-files"])

    if result == 0:
        print("All pre-commit hooks passed!")
    else:
        print("Some pre-commit hooks failed.")
    return result


if __name__ == "__main__":
    main()
