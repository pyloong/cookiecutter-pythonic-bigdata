"""Logger"""
import os
import logging
from logging.config import dictConfig

from dynaconf.base import Settings

from {{cookiecutter.project_slug}}.constants import DEFAULT_ENCODING


class LoggerManager:
    """
    This is Logger config class, you can init logger config for logging.
    param ctx_settings: Context() settings
    """

    def __init__(self, ctx_settings: Settings):
        self.settings = ctx_settings
        self.log_path = self.get_log_path()

    def get_logger(self):
        """Return Logger object."""
        self.init_log()
        logger = logging.getLogger()
        print(f'Log file path: "{self.get_log_path()}"')
        return logger

    def get_log_path(self):
        """
        Get or Create default log path
        Default log path: "tmp/log/all.log"
        """
        log_path = self.settings.LOGPATH
        os.makedirs(log_path, exist_ok=True)
        return log_path

    @staticmethod
    def verbose_formatter(verbose: bool) -> str:
        """formatter factory"""
        if verbose is True:
            return 'verbose'
        return 'simple'

    def update_log_level(self, debug: bool, level: str) -> str:
        """update log level"""
        if debug is True:
            level_num = logging.DEBUG
        else:
            level_num = logging.getLevelName(level)
        self.settings.set('LOGLEVEL', logging.getLevelName(level_num))
        return self.settings.LOGLEVEL

    def init_log(self) -> None:
        """Init log config."""
        log_level = self.update_log_level(self.settings.DEBUG, str(self.settings.LOGLEVEL).upper())

        verbose_format = '%(asctime)s %(levelname)s %(name)s %(process)d %(thread)d %(message)s'
        simple_format = '%(asctime)s %(levelname)s %(name)s %(message)s'

        log_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                'verbose': {
                    'format': verbose_format,
                },
                'simple': {
                    'format': simple_format,
                },
            },
            "handlers": {
                "console": {
                    "formatter": self.verbose_formatter(self.settings.VERBOSE),
                    'level': 'DEBUG',
                    "class": "logging.StreamHandler",
                },
                'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'DEBUG',
                    'formatter': self.verbose_formatter(self.settings.VERBOSE),
                    'filename': os.path.join(self.log_path, 'all.log'),
                    'maxBytes': 1024 * 1024 * 1024 * 200,  # 200M
                    'backupCount': '5',
                    'encoding': DEFAULT_ENCODING
                },
            },
            "loggers": {
                '': {'level': log_level, 'handlers': ['console']},
            }
        }

        dictConfig(log_config)
