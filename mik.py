#!.venv/bin/python
import customLogger

logger = customLogger.Logging(name="mik", level="debug", filemode="a", filename="mik.log", file=True)

levels: dict = {
        "critical": 50,
        "error": 40,
        "warning": 30,
        "info": 20,
        "debug": 10,
        "notset": 0
    }

logger.critical("6547657")  # 50
logger.error("746756")  # 40
logger.warning("567467")  # 30
logger.info("47657457")  # 20
logger.debug("54764665446")  # 10