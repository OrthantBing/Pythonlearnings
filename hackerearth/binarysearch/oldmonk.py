def binarysearch(array, query, left, right):
    mid = (right - left) // 2 + left
    while left <= right:
        mid = (right - left) // 2 + left
        if array[mid] == query:
            break
        elif array[mid] < query:
            right = mid - 1
        elif array[mid] > query:
            left = mid + 1
    
    #mid -= 1 # simulate do while
    while mid >= 0 and array[mid] <= query:
        mid -= 1

    return mid + 1 # because previously we have moved one step left to check


if __name__ == '__main__':
    cases = int(raw_input())
    for _ in xrange(cases):
        length = int(raw_input())
        A = map(int, raw_input().split())
        B = map(int, raw_input().split())

        diff = 0
        if A[-1] > B[0]:
            print 0
        else:
            for bpos in xrange(length-1, -1, -1):
                apos = binarysearch(A, B[bpos], 0, bpos)
                currentdiff = bpos - apos
                if diff < currentdiff:
                    diff = currentdiff
            print diff

        


