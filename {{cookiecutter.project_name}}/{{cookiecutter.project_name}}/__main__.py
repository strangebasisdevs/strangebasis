# {{cookiecutter.project_name}}
#     Copyright (C) {% now 'utc', '%Y' %}  {{ cookiecutter.author_name }}


def main() -> int:
    print("Hello from {{ cookiecutter.project_name }}!")

    return 0


if __name__ == "__main__":
    main()
