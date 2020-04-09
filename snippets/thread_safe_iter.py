import threading


class threadsafe_iter:
    """Takes an iterator/generator and makes it thread-safe by
    serializing call to the `next` method of given iterator/generator.
    """
    def __init__(self, it):
        self.it = it
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def next(self):
        with self.lock:
            return self.it.next()


# Now you can take any iterator or generator and make it thread-safe by wrapping it with threadsafe_iter.

# thread unsafe generator
# c1 = count()

# now it is thread-safe
c1 = threadsafe_iter(c1)
# This can be made still easier by writing a decorator.


def threadsafe_generator(f):
    """A decorator that takes a generator function and makes it thread-safe.
    """
    def g(*a, **kw):
        return threadsafe_iter(f(*a, **kw))
    return g
# Now we can use this decorator to make any generator thread-safe.


@threadsafe_generator
def count():
    i = 0
    while True:
        i += 1
        yield i