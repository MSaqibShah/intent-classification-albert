import colorlog
import logging

TEXT_LEVEL_NUM = 9
INTENT_LEVEL_NUM = 10
logging.addLevelName(TEXT_LEVEL_NUM, "TEXT")
logging.addLevelName(INTENT_LEVEL_NUM, "INTENT")


def text(self, message, *args, **kws):
    if self.isEnabledFor(TEXT_LEVEL_NUM):
        self._log(TEXT_LEVEL_NUM, message, args, **kws)
    else:
        self._log(9, message, args, **kws)


def intent(self, message, *args, **kws):
    if self.isEnabledFor(INTENT_LEVEL_NUM):
        self._log(INTENT_LEVEL_NUM, message, args, **kws)
    else:
        self._log(10, message, args, **kws)


# Attach the method to Logger class
logging.Logger.text = text
logging.Logger.intent = intent


def set_logger_color(logger):
    handler = colorlog.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        '%(message_log_color)s%(message)s',
        # '%(log_color)s%(levelname)s:%(name)s%(reset)s %(message_log_color)s%(message)s',
        datefmt=None,
        reset=True,
        log_colors={
            "TEXT": "blue",
            "INTENT": "red",
        },
        secondary_log_colors={
            'message': {
                "TEXT": "green",
                "INTENT": "blue",
            }
        },
        style='%'
    )
    logger.addHandler(handler)
    handler.setFormatter(formatter)


def create_logger():
    logger = logging.getLogger()
    set_logger_color(logger)
    logger.setLevel(logging.DEBUG)
    return logger


# def log_text(logger, data):
#     logger.setLevel(colorlog.colorlog.logging.TEXT)
#     logger.info(logger, data, "TEXT")
#     logger.setLevel(colorlog.colorlog.logging.DEFAULT)


# def log(logger, data, log_type="TEXT"):
#     if log_type == "TEXT":
#         logger.info(data)
#     elif log_type == "INTENT":
#         logger.info(data)
#     else:
#         logger.info(data
