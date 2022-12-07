"""
Loads a Task class and calls its `run()` method.
"""
from typing import Callable

from stevedore import ExtensionManager

from {{cookiecutter.project_slug}}.constants import TASK_NAMESPACE
from {{cookiecutter.project_slug}}.context import Context
from {{cookiecutter.project_slug}}.utils.exception import PluginNotFoundError


class Executor:
    """
    Loads a Task class and calls its `run()` method.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, ctx: Context, task: str):
        self.task = task
        self.ctx = ctx
        self.logger = ctx.logger

    def run(self) -> None:
        """calls its `run()` method in the task class"""
        task_class = self._load_task(TASK_NAMESPACE, self.task)
        self.logger.info(f"Running task: {task_class}")
        task_class().run()

    def _load_task(self, namespace: str, name: str) -> Callable:
        """Get extension by name from namespace, return task obj"""
        extension_manager = ExtensionManager(namespace=namespace, invoke_on_load=False)
        for ext in extension_manager.extensions:
            if ext.name == name:
                return ext.plugin
            self.logger.warning(f'Load plugin: {ext.plugin} in namespace "{namespace}"')
        raise PluginNotFoundError(namespace=namespace, name=name)
