if __name__ == '__main__':
    count = int(raw_input())
    n = 1000000
    for _ in xrange(count):
        maxval = int(raw_input())
        if maxval <= 2:
            print n // maxval
        else:
            array = [i for i in xrange(maxval, n, maxval)]
            j = 2
            truefalsearray = [True for i in xrange(len(array))]
            while j * j <= n and j < maxval:
                # for k in xrange(j, n+1, j):
                #     if array[k] % j == 0:
                #         truefalsearray[k] = False
                # i += 1
                for k in xrange(len(array)):
                    if array[k] % j == 0:
                        truefalsearray[k] = False
                j += 1
            returncount = 0
            for l in xrange(len(array)):
                if truefalsearray[l] is True:
                    if array[l] % maxval == 0:
                        returncount += 1

            print returncount
