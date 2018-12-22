import sys
def isTriangle(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    else:
        return False

def getMinAndMaxVal(arr):
    a, b, c = arr
    maxval = min(a+b, b+c, c+a)
    minval = max(a, b, c) - min(a, b, c)
    return (minval, maxval)


if __name__ == "__main__":
    n = int(raw_input())
    array = map(int, raw_input().split())

    count = n + n-1

    # for i in xrange(n):
    #     if i+3 <= n:
    #         a, b, c = array[i:i+3]
    #         if isTriangle(a, b, c):
    #             count += 1

    # print count
    for i in xrange(n):
        j = i+3
        first = True
        minval = 0
        maxval = sys.maxint
        while j <= n:
            # print i,j
            testarray = array[i:j]
            if first:
                first = False
                minval, maxval = getMinAndMaxVal(testarray)
                if isTriangle(testarray[0], testarray[1], testarray[2]):
                    count += 1
                else:
                    break
            else:
                # recompute max val
                newmaxval = min(testarray[:len(testarray) - 1]) + testarray[-1]
                if  newmaxval < maxval:
                    maxval = newmaxval
                if testarray[-1] >= minval and testarray[-1] <= maxval:
                    count += 1
                else:
                    break
            j += 1
    print count



