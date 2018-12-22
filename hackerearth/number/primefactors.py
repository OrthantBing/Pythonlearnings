if __name__ == "__main__":
    count = int(raw_input())
    n = 1000000
    for _ in xrange(count):
        maxval = int(raw_input())
        if maxval > 2:

            primes = [True for _ in xrange(n+1)]
            primes[0] = False
            primes[1] = False
            i = 2
            while i * i <= n and i < maxval:
                if primes[i] == True:
                    for j in xrange(i, n+1, i):
                        primes[j] = False

                i += 1
            returncount = 0
            for j in xrange(n+1):
                if primes[j] is True:
                    if j % maxval ==  0:
                        returncount += 1
            
            print returncount
        
        else:
            print n // maxval

