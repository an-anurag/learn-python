"""
5.

I am in general agreement with David, but I think more needs to be said. To paraphrase The Princess Bride - I do not think this code means what you think it means. Your code has:

logger1 = logging.getLogger('')
...
logger2 = logging.getLogger('')
which means that logger1 and logger2 are the same logger, so when you set the level of logger2 to ERROR you actually end up setting the level of logger1 at the same time. In order to get two different loggers, you would need to supply two different logger names. For example:

logger1 = logging.getLogger('user')
...
logger2 = logging.getLogger('dev')
Worse still, you are calling the logging module's critical(), info() and warning() methods and expecting that both loggers will get the messages. This only works because you used the empty string as the name for both logger1 and logger2 and thus they are not only the same logger, they are also the root logger. If you use different names for the two loggers as I have suggested, then you'll need to call the critical(), info() and warning() methods on each logger individually (i.e. you'll need two calls rather than just one).

What I think you really want is to have two different handlers on a single logger. For example:

import logging

mylogger = logging.getLogger('mylogger')
handler1 = logging.FileHandler('usr.log')
handler1.setLevel(logging.INFO)
mylogger.addHandler(handler1)
handler2 = logging.FileHandler('dev.log')
handler2.setLevel(logging.ERROR)
mylogger.addHandler(handler2)
mylogger.setLevel(logging.INFO)

mylogger.critical('A critical message')
mylogger.info('An info message')
Once you've made this change, then you can use filters as David has already mentioned. Here's a quick sample filter:

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level
You can apply the filter to each of the two handlers like this:

handler1.addFilter(MyFilter(logging.INFO))
...
handler2.addFilter(MyFilter(logging.ERROR))
This will restrict each handler to only write out log messages at the level specified.

"""