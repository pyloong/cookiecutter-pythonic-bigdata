"""Spark Init and Spark Log4j class"""
from pyspark import SparkConf
from pyspark.sql import SparkSession

from {{cookiecutter.project_slug}}.configs import settings
from {{cookiecutter.project_slug}}.constants import APP_NAME


def init_spark(app_name=APP_NAME, **spark_config):
    # create a SparkSession builder with the given app name and master URL
    spark_builder = (
        SparkSession
        .builder
        .appName(app_name))

    # add other config params to the builder
    for key, val in spark_config.items():
        spark_builder.config(key, val)

    # get or create a SparkSession
    spark_sess = spark_builder.getOrCreate()

    # create a SparkLog4j object to handle logging
    spark_logger = SparkLog4j(spark_sess)

    # if a config file path is provided, load the config file and set the SparkConf
    spark_configs = settings.SPARK_CONFIGS
    if spark_configs:
        SparkConf().setAll(spark_configs.items())
        # log a warning message indicating that the config file was loaded
        spark_logger.warn(f'Loaded config from "{spark_configs}"')
    else:
        # log a warning message indicating that no config file was found
        spark_logger.warn('Not load spark config')

    # return the SparkSession and SparkLog4j objects
    return spark_sess, spark_logger


class SparkLog4j:
    """
    Wrapper class for Log4j JVM object.
    Initializes a logger object with a default log level of "WARN".
    :param spark: SparkSession object.
    """

    def __init__(self, spark: SparkSession):
        # get spark app details with which to prefix all messages
        conf = spark.sparkContext.getConf()
        app_id = conf.get('spark.app.id')
        app_name = conf.get('spark.app.name')
        spark.sparkContext.setLogLevel('info')
        log4j = spark._jvm.org.apache.log4j
        message_prefix = '<' + app_name + ' ' + app_id + '>'
        self.logger = log4j.LogManager.getLogger(message_prefix)

    def error(self, message):
        """Log an error message.
        :param message: Error message to write to log
        :return: None
        """
        self.logger.error(message)

    def warn(self, message):
        """Log a warning message.
        :param message: Warning message to write to log
        :return: None
        """
        self.logger.warn(message)

    def info(self, message):
        """Log an information message.
        :param message: Information message to write to log
        :return: None
        """
        self.logger.info(message)
