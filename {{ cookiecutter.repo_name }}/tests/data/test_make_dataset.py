from {{ cookiecutter.package_name }}.data.make_dataset import main


def test_main():
    result = main()
    assert result == True