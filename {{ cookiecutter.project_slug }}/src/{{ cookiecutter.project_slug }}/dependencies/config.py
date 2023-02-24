"""Config Manager"""
from pathlib import Path

from dynaconf import Dynaconf

__BASE_DIR = Path(__file__).parent.parent

__settings_files = [
    # All configs file will merge.  # Load default configs.
    __BASE_DIR / 'configs' / 'dev.toml',
    __BASE_DIR / 'configs' / 'prod.toml',
    __BASE_DIR / 'configs' / 'test.toml',
    __BASE_DIR / 'configs' / 'global.toml',
]
{%  with %}{% set project_slug_upper = cookiecutter.project_slug|upper() %}
config_manager = Dynaconf(
    # Set env `MYPROGRAM='bar'`，use `configs.FOO` .
    envvar_prefix='{{ project_slug_upper }}',
    settings_files=__settings_files,
    environments=True,  # multi environments
    load_dotenv=True,  # Enable load .env
    lowercase_read=True,
    base_dir=__BASE_DIR,
)
{% endwith %}

def update_configs(_settings, key, value):
    """Overwrite env settings config value"""
    if not _settings.exists(key):
        return
    _settings.set(key, value)
