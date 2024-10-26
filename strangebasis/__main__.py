import argparse

import pre_commit.main


def main():
    parser = argparse.ArgumentParser(description="Strange Basis CLI")
    subparsers = parser.add_subparsers(dest="command")

    hooks_parser = subparsers.add_parser("hooks", help="Run shared hooks")
    hooks_parser.set_defaults(func=hooks)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


def hooks(args):
    # parser = argparse.ArgumentParser(description="Run shared hooks")

    result = pre_commit.main.main(["run", "--all-files"])

    if result == 0:
        print("All pre-commit hooks passed!")
    else:
        print("Some pre-commit hooks failed.")
    return result


if __name__ == "__main__":
    main()
