#!.venv/bin/python
import customLogger
import mik

logger = customLogger.Logging(name="testing", level="debug", filemode="a", filename="kim.log", file=True)

levels: dict = {
        "critical": 50,
        "error": 40,
        "warning": 30,
        "info": 20,
        "debug": 10,
        "notset": 0
    }

logger.critical("testiangalka")  # 50
logger.error("testiangalka")  # 40
logger.warning("testiangalka")  # 30
logger.info("testiangalka")  # 20
logger.debug("testiangalka")  # 10