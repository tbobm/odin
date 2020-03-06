"""Setup and configure the odin logger."""
import logging


def build_logger(logger_name: str, level: int = logging.INFO) -> logging.Logger:
    """Return a configured logger."""
    logger_configuration = {
        "format": "%(asctime)s %(process)d %(levelname)s %(name)s %(message)s"
    }
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.propagate = False
    formatter = logging.Formatter(logger_configuration["format"])

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
