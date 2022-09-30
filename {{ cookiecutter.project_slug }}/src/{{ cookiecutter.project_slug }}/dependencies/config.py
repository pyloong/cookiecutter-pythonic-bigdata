"""Config Manager"""
from dynaconf import Dynaconf

__settings_files = [
    # All configs file will merge.  # Load default configs.
    'src/automotive_data_etl/configs/global.toml',
    'src/automotive_data_etl/configs/test.toml',
    'src/automotive_data_etl/configs/prod.toml',
    'src/automotive_data_etl/configs/dev.toml'
]

{%  with %}{% set project_slug_upper = cookiecutter.project_slug|upper() %}
settings = Dynaconf(
    # Set env `MYPROGRAM='bar'`，use `configs.FOO` .
    envvar_prefix='{{ project_slug_upper }}',
    settings_files=_settings_files,
    environments=True,  # multi environments
    load_dotenv=True,  # Enable load .env
    lowercase_read=True,
)
{% endwith %}

def update_configs(_settings, key, value):
    """Overwrite env settings config value"""
    if not _settings.exists(key):
        return
    _settings.set(key, value)
