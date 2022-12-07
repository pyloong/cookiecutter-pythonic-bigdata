"""Context"""
{%- if cookiecutter.use_framework|lower == 'pyspark' %}
from pyspark.sql import SparkSession
{%- endif %}

from {{cookiecutter.project_slug}}.constants import ENV_DEVELOPMENT
from {{cookiecutter.project_slug}}.dependencies.config import config_manager
from {{cookiecutter.project_slug}}.dependencies.logger import LoggerManager
from {{cookiecutter.project_slug}}.utils.singleton import singleton
{%- if cookiecutter.use_framework|lower == 'pyspark' %}
from {{cookiecutter.project_slug}}.dependencies.spark import SparkLog4j
from {{cookiecutter.project_slug}}.dependencies.spark import init_spark
{%- endif %}


@singleton
class Context:
    """
    Context for project, Provide properties and methods
    """
    environment = ENV_DEVELOPMENT

    def __init__(self):
        """Context Parameters"""
        self.settings = config_manager.from_env(self.environment)
        self.logger = LoggerManager(self.settings).get_logger()

{%- if cookiecutter.use_framework | lower == 'pyspark' %}
{%  with %}{% set project_slug_upper = cookiecutter.project_slug|upper() %}
    def get_spark_session(self) -> SparkSession:
        """Get spark session"""
        return init_spark(self.settings, app_name='BUSINESS_DATA_ETL')
{% endwith %}
    def get_spark_logger(self, spark_session) -> SparkLog4j:
        """Get the initialized Spark log object"""
        if not spark_session:
            self.get_spark_session()
        return SparkLog4j(spark_session)
{%- endif %}
