def fibonacci(n):
    array = []
    i, j = 0, 1
    while i < n:
        i, j = i+j, i
        if i < n: 
            array.append(i)

    return array

for _ in xrange(int(raw_input())):
    test = fibonacci(int(raw_input()))
    print test 
    print sum(filter(lambda x: x % 2 == 0, test))
