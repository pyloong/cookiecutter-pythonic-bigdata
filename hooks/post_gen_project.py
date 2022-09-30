"""Post-generate project hooks"""
import os
import shutil
from pathlib import Path


def remove_file(file: Path, *files: Path):
    """
    Remove file
    :param file:
    :param files:
    :return:
    """
    os.remove(file)
    for _f in files:
        os.remove(_f)


def setup_src_layout(flag: str):
    """Setup src layout"""
    if flag != 'y':
        # shutil.move can not pass Path, will raise Exception.
        shutil.move(src=str(Path('src', PROJECT_SLUG)), dst='.')
        shutil.rmtree('src')


def setup_poetry(flag: str):
    """
    Setup poetry.
    If n, use requirements.txt, and require `setup.cfg` file
    else remove `requirements.txt` and `setup.cfg`.
    :param flag:
    :return:
    """
    if flag != 'y':
        remove_file(Path('pyproject.toml'))
    else:
        remove_file(
            Path('requirements.txt'),
            Path('setup.cfg'),
            Path('MANIFEST.in')
        )


def setup_docker(flag: str):
    """
    Setup docker.
    :param flag:
    :return:
    """
    if flag != 'y':
        remove_file(Path('Dockerfile'), Path('.dockerignore'))


def setup_ci_tools(flag: str):
    """
    Setup ci tools
    :param flag:
    :return:
    """
    if flag != 'gitlab':
        remove_file(Path('.gitlab-ci.yml'))
    if flag != 'github':
        shutil.rmtree('.github', ignore_errors=True)


def setup_framework(flag: str):
    """
    Setup ci tools
    :param flag:
    :return:
    """
    if flag != 'pyspark':
        remove_file(Path('src/{{ cookiecutter.project_slug }}/dependencies/spark.py'))


if __name__ == "__main__":
    PROJECT_SLUG = '{{ cookiecutter.project_slug }}'
    SRC_LAYOUT = '{{ cookiecutter.use_src_layout|lower }}'
    USE_POETRY = '{{ cookiecutter.use_poetry|lower }}'
    USE_DOCKER = '{{ cookiecutter.use_docker|lower }}'
    CI_TOOLS = '{{ cookiecutter.ci_tools|lower }}'
    USE_FRAMEWORK = '{{ cookiecutter.use_framework|lower }}'

    setup_src_layout(SRC_LAYOUT)
    setup_poetry(USE_POETRY)
    setup_docker(USE_DOCKER)
    setup_ci_tools(CI_TOOLS)
    setup_framework(USE_FRAMEWORK)
