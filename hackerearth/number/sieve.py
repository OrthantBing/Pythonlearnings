if __name__ == '__main__':
    n = int(raw_input())
    primes = [True for _ in xrange(n+1)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i * i <= n:

        if primes[i] == True:
            for j in xrange(i*2, n+1, i):
                primes[j] = False

        i += 1
    
    count = 0
    for p in xrange(2, n):
        if primes[p]:
            count += 1

    print count
        
            

    