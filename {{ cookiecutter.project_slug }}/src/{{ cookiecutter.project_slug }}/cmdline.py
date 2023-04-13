"""Project executor"""
import argparse
from logging import Logger

from stevedore import ExtensionManager

from {{cookiecutter.project_slug}}.constants import TASK_NAMESPACE
from {{cookiecutter.project_slug}}.context import Context
from {{cookiecutter.project_slug}}.executor import Executor
from {{cookiecutter.project_slug}}.dependencies.config import update_configs
from {{cookiecutter.project_slug}}.dependencies.logger import init_log


def _parse_args() -> argparse.Namespace:
    """Parameter parsing"""
    parser = argparse.ArgumentParser(allow_abbrev=False)
    # parser add arguments
    parser.add_argument(
        "--task",
        required=True,
        choices=_get_task_list()
    )
    parser.add_argument(
        "--input",
        required=False,
        help='Update extract data input path'
    )
    parser.add_argument(
        "--output",
        required=False,
        help='Update extract data output path'
    )
    parser.add_argument(
        "--config_path",
        required=False,
        help='Spark config path, file format is json'
    )
    return parser.parse_args()


def _get_task_list():
    """Get task list by namespace"""
    extension_manager = ExtensionManager(namespace=TASK_NAMESPACE, invoke_on_load=False)
    return extension_manager.entry_points_names()


def _update_path(input_path=None, output_path=None, spark_config_path=None):
    """Get task list by namespace"""
    if input_path:
        update_configs('input_path', input_path)
    if output_path:
        update_configs('output_path', output_path)
    if spark_config_path:
        update_configs('spark_config_path', spark_config_path)


def main() -> None:
    """
    Parse args, init Context, init logger and executor task run.
    """
    args = _parse_args()

    init_log()
    # Init Context object
    ctx = Context()
    ctx.init_logger()
    logger: Logger = ctx.logger
    # Update Settings Use Args
    _update_path(input_path=args.input, output_path=args.output, spark_config_path=args.config_path)
    # logger = logging.getLogger()
    logger.info('ETL project init success.')
    # Executor scheduling task
    Executor(ctx, args.task).run()


if __name__ == "__main__":
    main()
