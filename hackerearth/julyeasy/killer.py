from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

if __name__ == '__main__':
    cases = int(raw_input())
    for _ in xrange(cases):
        P, X = map(int, raw_input().split())
        array = [i for i in xrange(32001)]
        for i in xrange(2, 32001):
            if isPrime(i):
                if i <= P:
                    indextodelete = i * i
                    counter = 2
                    while indextodelete < 32001:
                        array[indextodelete] = 0
                        indextodelete = indextodelete * counter
                        counter += 1
                else:
                    indextodelete = i
                    counter = 2
                    while indextodelete < 32001:
                        array[indextodelete] = 0
                        indextodelete = indextodelete * counter
                        counter += 1
        
        alive = 0
        for i in xrange(1, 32001):
            if array[i] != 0:
                alive += 1
            
            if alive == X:
                print i
                break
        


                

