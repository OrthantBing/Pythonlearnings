
from itertools import combinations
import sys

def arraydistance(array, cost, part):
    sum = 0
    for j in xrange(len(part)-1,-1,-1):
        if j == len(part) - 1:
            if array.index(part[j]) == len(array) - 1:
                sum += 0
                continue
            else:
                calcsum = array[array.index(part[j])+1:]
        else:
            calcsum = array[array.index(part[j])+1:array.index(part[j+1])]
        # Here there can be 2 possiblities
        # it can be empty indicating the above and below are 2 positions

        if len(calcsum) == 0:
            continue
        else:
            for i in calcsum:
                sum += (i - part[j]) * cost[array.index(i)]
    return sum


if __name__ == "__main__":
    poles, stacks = map(int,raw_input().split())

    poleheightarray = []
    costheightarray = []

    polecostarray = []
    for _ in xrange(poles):
        z = tuple(map(int,raw_input().split()))
        polecostarray.append(z)
        poleheightarray.append(z[0])
        costheightarray.append(z[1])
        
    polelist = map(lambda x: x[0], polecostarray)

    totalcomb = [ tuple([polelist[0]] + list(i)) for i in combinations(polelist[1:], stacks - 1 )]

    minsum = sys.maxsize
    for i in totalcomb:
        s = arraydistance(poleheightarray,costheightarray,i)
        if s < minsum:
            minsum = s
    
    print minsum
    


