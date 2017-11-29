import time

def sleep_decorator(some_function):
    """
    Limits how fast the function
    is called.
    """

    def wrapper(*args, **kwargs):
        time1 = time.time()
        time.sleep(2)
        time2 = time.time()

        print "Time taken to sleep is: %s" % (time2-time1)
        return some_function(*args, **kwargs)

    return wrapper

@sleep_decorator
def add(a, b):
    #return a + b
    pass


print add(10,20)