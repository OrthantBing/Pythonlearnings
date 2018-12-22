def gcd_utils(x, y):
    while(y):
        x, y = y, x % y

    return x

def lcm_utils(x, y):
    lcm = (x * y) // gcd_utils(x, y)
    return lcm

def find_lcm(array):
    lcm = lcm_utils(array[0], array[1])
    for i in range(2, len(array)):
        lcm = lcm_utils(lcm, array[i])

    return lcm

def find_gcd(array):
    gcd = gcd_utils(array[0], array[1])
    for i in range(2, len(array)):
        gcd = gcd_utils(gcd, array[i])

    return gcd

if __name__ == '__main__':
    n = int(input())
    denominations = list(map(int, input().split()))

    if len(denominations) <= 2:
        if ( find_gcd(denominations) != 1):
            print ("Fake Offer!")
        else:
            a = denominations[0] * denominations[1] - (denominations[0] + denominations[1])
            print(a)

    elif len(denominations) == 3:
        lcm1 = find_lcm([denominations[0], denominations[1]])
        lcm2 = find_lcm([denominations[2], denominations[0]])

        a = lcm1 + lcm2 - denominations[0] - denominations[1] - denominations[2]
        if a > max(denominations):
            print(a)
        else:
            print("Fake Offer!")

    else: 
        print ("Fake Offer!")