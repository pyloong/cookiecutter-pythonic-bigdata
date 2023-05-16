"""Spark Init and Spark Log4j class"""
from pyspark.sql import SparkSession

from {{cookiecutter.project_slug}}.configs import settings
from {{cookiecutter.project_slug}}.constants import APP_NAME


def init_spark(app_name=APP_NAME):
    spark_builder = SparkSession.builder.appName(app_name)
    # Spark settings load
    spark_configs = settings.SPARK_CONFIGS
    if spark_configs:
        for key, val in settings.SPARK_CONFIGS.items():
            spark_builder.config(key, val)
    spark_sess = spark_builder.getOrCreate()
    # Spark s3a
    if settings.USE_S3A:
        init_s3a_conf(spark_sess)
    spark_logger = SparkLog4j(spark_sess)
    return spark_sess, spark_logger

def init_s3a_conf(spark):
    # 设置ceph的信息
    hadoopConf = spark.sparkContext._jsc.hadoopConfiguration()
    hadoopConf.set("fs.s3a.endpoint", settings.END_POINT)
    hadoopConf.set("fs.s3a.access.key", settings.ACCESS_KEY_ID)
    hadoopConf.set("fs.s3a.secret.key", settings.SECRET_ACCESS_KEY)
    hadoopConf.set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
    hadoopConf.set('fs.s3a.ssl.enabled', 'false')
    hadoopConf.set('fs.s3a.path.style.access', 'true')


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
