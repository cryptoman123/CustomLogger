from logging import NOTSET


class LogLevelMissMatch(Exception):
    """Exception raised for errors in the Logger Level."""
    def __init__(self, message="Log level miss match", level=NOTSET):
        super().__init__(f"Your log level is {level}, {message}")
        