"""Test"""
import functools
from pathlib import Path

import pytest
from pytest_cookies.plugin import Cookies


@pytest.fixture(name='project_root')
def project_root_fixture() -> str:
    """project root fixture"""
    return str(Path(__file__).parent.parent)


@pytest.fixture
def cookies_bake(cookies: Cookies, project_root):
    """cookies bake fixture"""
    return functools.partial(cookies.bake, template=project_root)
