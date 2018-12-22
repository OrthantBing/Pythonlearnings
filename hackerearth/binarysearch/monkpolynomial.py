# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monks-encounter-with-polynomial/
import math

def binarysearchpolinomial(a, b, c, k):
    # x should be between 1 and sqrt(k)
    if (c >= k):
        return 0

    right = int(math.sqrt(k)) + 1
    left = 0
    mid = 0
    equation = 0


    while left <= right:
        mid = ((right - left) // 2) + left

        equation = a * mid * mid + b * mid + c

        if equation == k:
            return mid
        elif equation > k:
            right = mid - 1
        elif equation < k:
            left = mid + 1

    ## If we reach here, we dont have and equal to k


    if equation < k:
        while equation < k:
            equation = a * mid * mid + b * mid + c
            mid += 1
        return mid - 1

    return mid

if __name__ == '__main__':
    n = int(raw_input().strip())
    for _ in xrange(n):
        a, b, c, k = map(int, raw_input().split())
        print binarysearchpolinomial(a, b, c, k)
