import logging
import sys


def setup_logging() -> logging.Logger:
    """Setup logging configuration for the bot."""
    logger = logging.getLogger("bot")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
