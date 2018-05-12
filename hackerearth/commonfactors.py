import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)



if __name__ == "__main__":
    (a, b) = [int(i) for i in raw_input().split()]
    gcd = gcd(a, b)
    
    counter = 0
    sqrtgcd = int(math.sqrt(int(gcd)))

    for i in xrange(1, sqrtgcd + 1):
        if gcd % i == 0:
            if (gcd / i == i):
                counter += 1
            else:
                counter += 2
    

    print counter



