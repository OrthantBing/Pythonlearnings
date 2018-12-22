def mergesort(array):
    length = len(array)
    if length < 2:
        return
    mid = length // 2
    left = array[:mid]
    right = array[mid:]
    mergesort(left)
    mergesort(right)
    merge(left, right, array)
    

def merge(leftarray, rightarray, array):
    nL = len(leftarray)
    nR = len(rightarray)
    i, j, k = 0, 0, 0
    while (i < nL and j < nR):
        if ord(leftarray[i]) >= ord(rightarray[j]):
            array[k] = leftarray[i]
            i += 1
        else:
            array[k] = rightarray[j]
            
            j += 1
        k += 1
    while i < nL:
        array[k] = leftarray[i]
        i += 1
        k += 1

    while j < nR:
        array[k] = rightarray[j]
        j += 1
        k += 1


def preparemergesort(array, startindex, endindex):
    arraytosort = array[startindex: endindex+1]
    mergesort(arraytosort)
    returnarray = array[:startindex] + arraytosort + array[endindex+1:]
    return returnarray


if __name__ == '__main__':
    n = int(raw_input())
    # array = map(int, raw_input().split())
    # mergesort(array)
    # print " "
    for i in xrange(n):
        arraylist, startindex, endindex = raw_input().split()
        array = list(arraylist)
        print "".join(preparemergesort(array, int(startindex), int(endindex)))