"""Context"""

from {{cookiecutter.project_slug}}.constants import ENV_DEVELOPMENT
from {{cookiecutter.project_slug}}.dependencies.config import settings
from {{cookiecutter.project_slug}}.dependencies.logger import LoggerManager
{%- if cookiecutter.use_framework|lower == 'pyspark' %}
from {{cookiecutter.project_slug}}.dependencies.spark import SparkLog4j
from {{cookiecutter.project_slug}}.dependencies.spark import init_spark
{%- endif %}


class Context:
    """
    Context for project, Provide properties and methods
    """
    _instance = None
    environment = ENV_DEVELOPMENT

    def __new__(cls):
        """Singleton mode"""
        if cls._instance is None:
            cls._instance = super(Context, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Context Parameters"""
        self.settings = settings.from_env(self.environment)

    def get_logger(self):
        """Context logger"""
        return LoggerManager(self.settings).get_logger()

{%- if cookiecutter.use_framework | lower == 'pyspark' %}
{%  with %}{% set project_slug_upper = cookiecutter.project_slug|upper() %}
    def get_spark_session(self):
        """Get spark session"""
        return init_spark(self.settings, app_name='{{ project_slug_upper }}')
{% endwith %}

    def get_spark_logger(self) -> SparkLog4j:
        """Get the initialized Spark log object"""
        return SparkLog4j(self.spark_session)
{%- endif %}
