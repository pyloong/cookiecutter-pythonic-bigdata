"""Base Task"""
from abc import ABC, abstractmethod

from {{cookiecutter.project_slug}}.context import Context
from {{cookiecutter.project_slug}}.configs import settings


class AbstractTask(ABC):
    """
    Base class to read a dataset, transform it, and save it to a table.
    """

    # pylint: disable=[too-few-public-methods]

    def __init__(self):
        self.ctx = Context()  # create a context object
        self.settings = settings  # create a settings object
        # loader path
        self.input_path = self.settings.INPUT_PATH
        self.output_path = self.settings.OUTPUT_PATH

    def run(self) -> None:
        """Execute the task module"""
        data = self._extract()  # extract data
        data_transformed = self._transform(data)  # transform data
        self._load(data_transformed)  # load data

    @abstractmethod
    def _extract(self):
        """Extract data from a file, database, or other source."""
        raise NotImplementedError

    @abstractmethod
    def _transform(self, data):
        """Transform incoming data and output the transformed result."""
        raise NotImplementedError

    @abstractmethod
    def _load(self, data) -> None:
        """Load data to a file, database, or other destination."""
        raise NotImplementedError
