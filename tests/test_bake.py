from pytest_cookies.plugin import Cookies


def test_ci_tools_invokes(cookies: Cookies):
    """Test ci tools"""
    result = cookies.bake(template='..')
    a = result.project_path
    print(a)


def test_bake_project(cookies_bake):
    result = cookies_bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
    assert result.project.basename == "helloworld"
    assert result.project.isdir()
