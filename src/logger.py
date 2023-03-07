import logging

from abc import ABC
from abc import abstractmethod


class LogLevelMissMAtch(Exception):
    """Exception raised for errors in the Logger Level."""
    def __init__(self, message="Log level miss match", level=logging.NOTSET):
        super().__init__(f"Your log level is {level}, {message}")


class LoggerInteface(ABC):

    @abstractmethod
    def debug(self, message: str):
        """Abstrat method to be implemented"""
        ...

    @abstractmethod
    def info(self, message: str):
        """Abstrat method to be implemented"""
        ...

    @abstractmethod
    def warning(self, message: str):
        """Abstrat method to be implemented"""
        ...

    @abstractmethod
    def error(self, message: str):
        """Abstrat method to be implemented"""
        ...

    @abstractmethod
    def critical(self, message: str):
        """Abstrat method to be implemented"""
        ...


class Logger(LoggerInteface):

    def __new__(cls, 
                name: str = __name__,
                level: int = logging.DEBUG,
                filename: str = f"default_{__name__}.log",
                filemode: str = "a",
                format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%d-%b-%y %H:%M:%S') -> logging.Logger:

        return cls._return_logger(name, level, filename, format, datefmt)
    
    def __init__(self,
                 name: str = __name__,
                 level: int = logging.DEBUG,
                 filename: str = f"default_{__name__}.log",
                 filemode: str = "a",
                 format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                 datefmt='%d-%b-%y %H:%M:%S') -> None:
        super().__init__()
        self._name: str = name
        self._level: int = level
        self._filename: str = filename
        self._filemode: str = filemode
        self._format: str = format
        self._datefmt: str = datefmt
        self._logger: logging.Logger = logging.getLogger(name)

    @property
    def name(self) -> str:
        """Get Name of the logger

            To get the name of the logging.Logger which is refered by logging.getLogger(__name__)
        
            :param self:
            :type self: Logger
            :return: name of the logger
            :rtype: str
        """
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Set Name of the logger

        To set the name of the logging.Logger which is refered by logging.getLogger(__name__)
    
        :param self:
        :type self: Logger
        :param value: The name you want the logger to be.
        :type value: str
        :return: None
        :rtype: None
        """
        self._name = value

    @property
    def level(self) -> str:
        """Get Level of the logger

        The numeric values of logging levels are given in the following table.
        These are primarily of interest if you want to define your own levels,
        and need them to have specific values relative to the predefined levels.
        If you define a level with the same numeric value,
        it overwrites the predefined value; the predefined name is lost.

        .. list-table:: Logging Levels
           :widths: 25 25
           :header-rows: 1

           * - Level
             - Numeric value
           * - CRITICAL
             - 50
           * - ERROR
             - 40
           * - WARNING
             - 30
           * - INFO
             - 20
           * DEBUG
             - 10
           * NOTSET
             - 0

        :param self:
        :type self: Logger
        :return: level of the logger
        :rtype: str
        """
        return self._level
    
    @level.setter
    def level(self, value: int):
        """Set Level of the logger

        The numeric values of logging levels are given in the following table.
        These are primarily of interest if you want to define your own levels,
        and need them to have specific values relative to the predefined levels.
        If you define a level with the same numeric value,
        it overwrites the predefined value; the predefined name is lost.

        .. list-table:: Logging Levels
           :widths: 25 25
           :header-rows: 1

           * - Level
             - Numeric value
           * - CRITICAL
             - 50
           * - ERROR
             - 40
           * - WARNING
             - 30
           * - INFO
             - 20
           * DEBUG
             - 10
           * NOTSET
             - 0

        :param self:
        :type self: Logger
        :param value: any of the logging values found in the above logging level table
        :type value: int
        :return: None
        :rtype: None
        """
        self._level = value

    @property
    def filename(self) -> str:
        """Get name of the file where the logger is writing logs in.
        
        :param self:
        :type self: Logger
        :return: level of the logger
        :rtype: str
        """
        return self._filename
    
    @filename.setter
    def filename(self, value: str):
        """Set the name of file where the logger is writing logs in.
        
        :param self:
        :type self: Logger
        :param value: The name you want the logger to be.
        :type value: str
        :return: None
        :rtype: None
        """
        self._filename = value

    @property
    def filemode(self) -> str:
        """Get the filemode of the logging.Logger reference.

        In Python there are a few filemodes which you might choose to use.
        Following are a a few of them:

        .. list-table:: Logging Levels
           :widths: 25 25
           :header-rows: 1

           * - Mode
             - Description
           * - r	
             - Open a file for reading. (default)
           * - w
             - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
           * - x
             - Open a file for exclusive creation. If the file already exists, the operation fails.
           * - a
             - Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
           * - t
             - Open in text mode. (default)
           * - b
             - Open in binary mode.
           * - +
             - Open a file for updating (reading and writing)

        :param self:
        :type self: Logger
        :return: filemode of the file handler in the logging.Logger reference
        :rtype: str
        """
        return self._filemode
    
    @filemode.setter
    def filemode(self, value: str):
        """Set the filemode of the logging.Logger reference.

        In Python there are a few filemodes which you might choose to use.
        Following are a a few of them:

        .. list-table:: Logging Levels
           :widths: 25 25
           :header-rows: 1

           * - Mode
             - Description
           * - r	
             - Open a file for reading. (default)
           * - w
             - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
           * - x
             - Open a file for exclusive creation. If the file already exists, the operation fails.
           * - a
             - Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
           * - t
             - Open in text mode. (default)
           * - b
             - Open in binary mode.
           * - +
             - Open a file for updating (reading and writing)

        :param self:
        :type self: Logger
        :param value: The mode you want the logger to write in a file.
        :type value: str
        :return: None
        :rtype: None
        """
        self._filemode = value

    @property
    def format(self) -> str:
        """Get the format of display messages or log record.

        To see how you can format your messages, see `LogRecord Attributes <https://docs.python.org/3/library/logging.html#logrecord-attributes>`_
        
        :param self:
        :type self: Logger
        :return: The format of the message you will log
        :rtype: str
        """
        return self._format
    
    @format.setter
    def format(self, value: str):
        """Set the format of display messages or log record.

        To see how you can format your messages, see `LogRecord Attributes <https://docs.python.org/3/library/logging.html#logrecord-attributes>`_
        
        :param self:
        :type self: Logger
        :param value: Format of Log Record
        :type value: str
        :return: The format of the message you will log
        :rtype: str
        """
        self._format = value

    @property
    def datefmt(self) -> str:
        """"Get the format of date which is logged into the message
        
        For checking out how to format the date, see `datefmt <https://docs.python.org/3/library/time.html#time.strftime>`_

        :param self:
        :type self: Logger
        :return: The format of the date
        :rtype: str
        """
        return self._datefmt
    
    @datefmt.setter
    def datefmt(self, value: str):
        """Set the format of date which is logged into the message

        For checking out how to format the date, see `datefmt <https://docs.python.org/3/library/time.html#time.strftime>`_

        :param self:
        :type self: Logger
        :param value: The format of the date
        :type: str
        :return: None
        :rtype: None
        """
        self._datefmt = value

    def getConsoleHandler(
            self,
            level: int = logging.DEBUG,
            format: str = '%(name)s - %(levelname)s - %(message)s') -> logging.StreamHandler:
        """To create a console handler
        
        To output log records onto the console

        :param level: logging level you want StreamHandler to be
        :type level: int
        :return: stream handler
        :rtype: logging.StreamHandler
        """
        c_handler = logging.StreamHandler()
        c_handler.setLevel(level)
        c_format = logging.Formatter(format)
        c_handler.setFormatter(c_format)
        return c_handler

    def getFileHandler(
            self,
            filename: str = f"{__name__}.log",
            filemode: str = "a",
            level: int = logging.DEBUG,
            format: str = '%(name)s - %(levelname)s - %(message)s') -> logging.FileHandler:
        """To create a File handler
        
        To output log records onto the File

        :param level: logging level you want FileHandler to be
        :type level: int
        :return: file handler
        :rtype: logging.FileHandler
        """
        f_handler = logging.FileHandler(filename=filename, filemode=filemode, encoding="UTF-8")
        f_handler.setLevel(level)
        f_format = logging.Formatter(format)
        f_handler.setFormatter(f_format)
        return f_handler

    def _return_logger(self,
                       name: str = __name__,
                      level: int = logging.DEBUG,
                      file: bool = False,
                      console: bool = True,
                      filename: str = f"{__name__}.log",
                      filemode: str = "a",
                      format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      datefmt='%d-%b-%y %H:%M:%S') -> logging.Logger:
        """Get the logging.Logger(__name__)

        :param self:
        :type self: Logger
        :param name: name of the logger
        :type str:
        :param level: one of the log levels, you can refer to it in the level setter function
        :type int:
        :param file: to write log records in a file
        :type bool:
        :param console: to write log records into the console
        :type bool:
        :param filename: path of the file where you want to write log records
        :type str:
        :param filemode: mode of the file where you want to write log records
        :type str:
        :param format: format of the log record
        :type str:
        :param datefmt: format of the date and time in log record
        :type str:
        :return: Logger
        :rtype logging.Logger:
        """
        self._logger.setLevel(logging.DEBUG)  # Root logger

        if file:
            # Add a file handler
            f_handler = self.getFileHandler(filename=filename, filemode=filemode, level=level, format=format)
            self._logger.addHandler(f_handler)


        if console:
            # Add a Stream Handler
            c_handler = self.getConsoleHandler(level=level, format=format)
            self._logger.addHandler(c_handler)

        return self._logger

    def debug(self, message: str):
        """Write DEBUG level Log Record"""
        if self._level >= logging.DEBUG:
            self._logger.debug(message)
        else:
            raise LogLevelMissMAtch("You tried to create a Log Record of DEBUG", self._level)

    def info(self, message: str):
        """Write INFO level Log Record"""
        if self._level >= logging.INFO:
            self._logger.info(message)
        else:
            raise LogLevelMissMAtch("You tried to create a Log Record of INFO", self._level)

    def warning(self, message: str):
        """Write WARNING level Log Record"""
        if self._level >= logging.WARNING:
            self._logger.warning(message)
        else:
            raise LogLevelMissMAtch("You tried to create a Log Record of WARNING", self._level)

    def error(self, message: str):
        """Write ERROR level Log Record"""
        if self._level >= logging.ERROR:
            self._logger.error(message)
        else:
            raise LogLevelMissMAtch("You tried to create a Log Record of ERROR", self._level)

    def critical(self, message: str):
        """Write CRITICAL level Log Record"""
        if self._level >= logging.CRITICAL:
            self._logger.critical(message)
        else:
            raise LogLevelMissMAtch("You tried to create a Log Record of CRITICAL", self._level)


if __name__ == "__main__":
    pass