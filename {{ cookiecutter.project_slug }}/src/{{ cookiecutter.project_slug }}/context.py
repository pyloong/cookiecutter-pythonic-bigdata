"""Context"""
import logging

{%- if cookiecutter.use_framework|lower == 'pyspark' %}
from pyspark.sql import SparkSession
{%- endif %}

from {{cookiecutter.project_slug}}.constants import APP_NAME
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

    def __init__(self):
        """Context Parameters"""
        self.logger = None
        self.spark_logger = None

    def init_logger(self):
        """
        Initializes the logger for the context object based on the current settings.
        """
        self.logger = logging.getLogger()

{%- if cookiecutter.use_framework|lower == 'pyspark' %}
    def get_spark_session(self, app_name=APP_NAME, **spark_config) -> SparkSession:
        """Get spark session"""
        spark_sess, spark_logger = init_spark(app_name=app_name, **spark_config)
        self.spark_logger = spark_logger
        return spark_sess

    def get_spark_logger(self, spark_session) -> SparkLog4j:
        """Get the initialized Spark log object"""
        if not spark_session:
            self.get_spark_session()
        return SparkLog4j(spark_session)
{%- endif %}
