
# 5

import logging


class LogFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.__level = level

    def filter(self, rec):
        return rec.levelno == self.__level


class Logger:

    def __init__(self):
        self.logger = logging.getLogger("DEMO")
        handler2 = logging.FileHandler('error.log')
        handler2.setLevel(logging.ERROR)
        handler2.addFilter(LogFilter(logging.ERROR))

        self.logger.addHandler(handler2)
        handler1 = logging.FileHandler('information.log')
        handler1.setLevel(logging.INFO)
        handler1.addFilter(LogFilter(logging.INFO))
        self.logger.addHandler(handler1)


log = Logger().logger

log.info("This is info")
log.error("This is error")
log.info("This is another info")
log.error("This is another error")
log.warning("this is warning")
log.info("This is 3rd info")
log.critical("This is critical")
log.error("This is 4th error")



