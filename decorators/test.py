
def log(somefunction):
    def wrapped(a, b):
        print "Before executing"
        somefunction(a, b)
        print "After executing"
    
    return wrapped


@log
def add(a, b):
    print "Sum of a and b is %s" % (a + b,)

add(5,10)