def binarysearch(array, query, arraylength):
    left = 0
    right = arraylength - 1
    while left <= right:
        mid = ((right - left) // 2) + left
        if query == array[mid]:
            return mid
        elif query < array[mid]:
            right = mid - 1
        elif query > array[mid]:
            left = mid + 1
    
    return -1
        

if __name__ == '__main__':
    n = int(raw_input())
    array = map(int, raw_input().split())
    array.sort() # This is mutating the array. Fuck it
    arraylength = len(array)

    queries = int(raw_input().strip())
    for _ in xrange(queries):
        query = int(raw_input())
        val = binarysearch(array, query, arraylength)
        if val != -1:
            print val + 1
