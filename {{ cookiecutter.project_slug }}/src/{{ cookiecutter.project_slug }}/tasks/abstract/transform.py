"""Base Transform"""
from abc import ABC, abstractmethod
from typing import Optional, Union, List

{%- if cookiecutter.use_framework|lower == 'pyspark' %}
from pyspark.sql import SparkSession, DataFrame

{% endif %}
from {{cookiecutter.project_slug}}.context import Context


class AbstractTransform(ABC):
    """
    Base class to define a DataFrame transformation.
    """

    # pylint: disable=[too-few-public-methods]

    def __init__(self):
        self.ctx = Context()  # create a context object
        self.settings = self.ctx.settings  # create settings object
        { %- if cookiecutter.use_framework | lower != 'pyspark' %}
        self.logger = self.ctx.logger
        { %- elif cookiecutter.use_framework | lower == 'pyspark' %}
        self.spark: SparkSession = self.ctx.get_spark_session()  # create spark session
        self.logger = self.ctx.spark_logger
        { % endif %}

    @abstractmethod
    def transform(self, data):
        """
        This method should be implemented to transform the original dataset.

        Args:
            data: The original dataset to be transformed.

        Returns:
            The transformed dataset.
        """
        raise NotImplementedError
    {%- if cookiecutter.use_framework | lower == 'pyspark' %}

    def extra_extractor(
            self,
            file_format,
            path,
            schema=None,
            **options
    ) -> DataFrame:
        """
        Extracts data from a file and returns a DataFrame.

        Args:
            file_format (str): The format of the file to be extracted.
            path (str): The path of the file to be extracted.
            schema (pyspark.sql.types.StructType, optional): The schema of the file to be extracted. Defaults to None.
            **options: Additional options to be passed to the Spark DataFrameReader.

        Returns:
            pyspark.sql.DataFrame: The extracted DataFrame.
        """
        df = (
            self.spark.read.load(
                path=path,
                format=file_format,
                schema=schema,
                **options
            ).repartition(self.default_parallelism)
        )
        if not df or df.isEmpty():
            error_desc = f"Check file, '{path}' file data is empty!"
            self.logger.error(error_desc)
            raise Exception(error_desc)
        return df

    def extra_loader(
            self,
            df: DataFrame,
            path,
            file_format,
            num_partitions=0,
            mode='append',
            partition_by: Optional[Union[str, List[str]]] = None,
            **options
    ) -> None:
        """
        Loads a DataFrame to a file.

        Args:
            df (pyspark.sql.DataFrame): The DataFrame to be loaded.
            path (str): The path of the file to be loaded.
            file_format (str): The format of the file to be loaded.
            num_partitions (int, optional): The number of partitions to be used when writing the file. Defaults to 0.
            mode (str, optional): The mode to be used when writing the file. Defaults to 'append'.
            partition_by (Union[str, List[str]], optional): The column(s) to partition the file by. Defaults to None.
            **options: Additional options to be passed to the Spark DataFrameWriter.

        Raises:
            Exception: If the DataFrame is empty.
        """
        if not df or df.isEmpty():
            error_desc = f"Check file, '{path}' file data is empty!"
            self.logger.error(error_desc)
            raise Exception(error_desc)
        if num_partitions > 0:
            df = df.coalesce(num_partitions)
        df.write.save(
            path=path,
            format=file_format,
            mode=mode,
            partitionBy=partition_by,
            **options
        )
        {% endif %}
