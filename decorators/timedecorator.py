import time

def timing_function(some_function):
    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in (range(0,1000)):
        for k in (range(0,20)):
            num_list.append(num)
            #print ("\nSum of all numbers: " + str((sum(num_list))))
            sum(num_list)

print(my_function())