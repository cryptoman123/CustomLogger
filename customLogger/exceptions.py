from logging import NOTSET


class LogLevelMissMatch(Exception):
    """Exception raised for errors in the Logger Level."""
    def __init__(self, message="Log level miss match", level=NOTSET):
        super().__init__(f"Your log level is {level}, {message}")
        

class IllegalAssignment(Exception):
    """Exception raised when logging.Logger is changed via assignment opperator."""
    def __init__(self, message="Changing logging.Logger via assignment opperator not allowed."):
        super().__init__(f"Illegal Assignment, {message}")
