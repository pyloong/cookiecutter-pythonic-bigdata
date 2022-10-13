"""Project executor"""
import argparse

from stevedore import ExtensionManager

from {{cookiecutter.project_slug}}.constants import ENV_DEVELOPMENT
from {{cookiecutter.project_slug}}.constants import TASK_NAMESPACE
from {{cookiecutter.project_slug}}.context import Context
from {{cookiecutter.project_slug}}.dependencies.config import update_configs
from {{cookiecutter.project_slug}}.executor import Executor


def _parse_args() -> argparse.Namespace:
    """Parameter parsing"""
    parser = argparse.ArgumentParser(allow_abbrev=False)
    # parser add arguments
    parser.add_argument(
        "--env",
        required=False,
        choices=['development', 'testing', 'production'],
        default=ENV_DEVELOPMENT
    )
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
    return parser.parse_args()


def _get_task_list():
    """Get task list by namespace"""
    extension_manager = ExtensionManager(namespace=TASK_NAMESPACE, invoke_on_load=False)
    return extension_manager.entry_points_names()


def _update_path(settings, input_path, output_path):
    """Get task list by namespace"""
    if input_path:
        update_configs(settings, 'input_path', input_path)
    if output_path:
        update_configs(settings, 'output_path', output_path)


def main() -> None:
    """
    Parse args, init Context, init logger and executor task run.
    """
    args = _parse_args()
    Context().environment = args.env
    ctx = Context()
    _update_path(ctx.settings, args.input, args.output)
    logger = ctx.logger
    logger.info('Etl project init success.')
    logger.info("Env configs options: %s", ctx.settings.message)
    Executor(ctx, args.task).run()


if __name__ == "__main__":
    main()
