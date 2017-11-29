array = map(int, raw_input().split())

def binarysearch(array, key):
    array.insert(0,-9999)
    low = 1
    high = len(array) - 1
    while low <= high:
        mid = (low + high) / 2
        if (array[mid] > key):
            high = mid - 1
        elif (array[mid] < key):
            low = mid + 1
        else:
            return mid
    
    return -1

print binarysearch(sorted(array),95) - 1
