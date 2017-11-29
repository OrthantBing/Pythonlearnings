import sys

def coinmin(coins, value):
    # Takes into account the base case of 0 -> 0
    T = [0 if _ == 0 else sys.maxint for _ in xrange(value + 1)]
    R = [-1 for _ in xrange(value + 1)]

    howtoreach = [-1 for _ in xrange(value + 1)]

    for i in coins:
        print T
        print R
        for j in xrange(1, value+1):
            if (j >= i):
                if (1 + T[j-i]) <= T[j]:
                    T[j] = 1 + T[j - i]
                    R[j] = coins.index(i)

    print T
    print R

coinmin([7,2,3,6], 13)


