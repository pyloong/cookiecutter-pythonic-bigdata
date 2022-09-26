"""Test conf"""
import functools
from pathlib import Path
from sys import version_info

import pytest
from pytest_cookies.plugin import Cookies

current_python_version = f'{version_info.major}.{version_info.minor}'


@pytest.fixture(name='project_root')
def project_root_fixture() -> str:
    """project root fixture"""
    return str(Path(__file__).parent.parent)


@pytest.fixture
def cookies_bake(cookies: Cookies, project_root):
    """cookies bake fixture"""
    return functools.partial(cookies.bake, template=project_root)
