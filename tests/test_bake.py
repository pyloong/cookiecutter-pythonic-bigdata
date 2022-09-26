"""Test"""


def test_bake_project(cookies):
    """Generate a new project"""
    result = cookies.bake(extra_context={"repo_name": "helloworld"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
    assert result.project.basename == "helloworld"
    assert result.project.isdir()
