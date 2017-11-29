def nonrecursiveheappermute(array):
    n = len(array)
    init = [0 for i in xrange(n)]

    print array

    i = 0
    while i < n:
        if init[i] < i:
            if i%2 == 1:
                array[0], array[i] = array[i], array[0]
            else:
                array[init[i]], array[i] = array[i], array[init[i]]
            print array
            init[i] += 1
            i = 0

        else:
            init[i] = 0
            i += 1

nonrecursiveheappermute([1,2,3,4])
#print [i for i in nonrecursiveheappermute([1,2,3,4])]
