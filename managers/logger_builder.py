"""This unit provides a LoggerBuilder class to create loggers in a handy way"""
import logging
# --------------------------------------------------------------------------


class LoggerBuilder:
    """LoggerBuilder class contains a handy interface to create loggers"""

    def __init__(self):
        """Initialization of LoggerBuilder class. There is a dict with
        logger's levels in the levels field"""
        self.levels = {'info': logging.INFO,
                       'debug': logging.DEBUG,
                       'warning': logging.WARNING,
                       'error': logging.ERROR,
                       'critical': logging.CRITICAL
                       }

    def get_new(self, filename: str, logger_name: str, format_str: str,
                level: str = 'info'):
        """Creation of a new logger

        :param filename: A name of a file to write logs into
        :param logger_name: A name of a new logger
        :param format_str: A template to format logger recordings
        :param level: A level of logger ('info' by default)
        Returns
            new_logger - an instance of the Logger class
        """
        new_logger = logging.getLogger(logger_name)
        logger_handler = logging.FileHandler(filename)
        log_formatter = logging.Formatter(format_str)

        logger_handler.setFormatter(log_formatter)
        new_logger.addHandler(logger_handler)
        new_logger.setLevel(self.levels.get(level, 'info'))

        return new_logger

