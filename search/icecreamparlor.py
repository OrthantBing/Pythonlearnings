tccount = int(raw_input())

def binarysearch(temparray, key):
    array = temparray[:]
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

for _ in xrange(tccount):
    value = int(raw_input())
    iccount = int(raw_input())
    icoriginalarray = map(int, raw_input().split())

    temp = sorted(icoriginalarray)
    foundindex = None
    firstindex = None
    for i in xrange(len(temp)):
        remaining = value - temp[i]
        foundindex = binarysearch(temp, remaining) - 1

        print temp, remaining
        
        if foundindex != -1:
            a, b = temp[foundindex], temp[i]
            foundindex = icoriginalarray.index(temp[foundindex])
            
            firstindex = icoriginalarray.index(temp[i])
            break
    

    if firstindex < foundindex:
        print " ".join(map(str,[firstindex + 1, foundindex + 1]))
    else:
        print " ".join(map(str, [foundindex + 1, firstindex + 1]))