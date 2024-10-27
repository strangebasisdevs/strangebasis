# {{cookiecutter.project_name}}
#     Copyright (C) {{ cookiecutter.year }}  Skylar DonLevy

def test_main(capsys):
    import {{cookiecutter.project_name}}
    {{cookiecutter.project_name}}.main()
    out, err = capsys.readouterr()
    assert out == "0\n"
    assert err == ""
