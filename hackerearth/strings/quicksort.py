def partition(array, startindex, endindex):
    pivot = array[endindex]
    partitionindex = startindex
    for i in xrange(startindex, endindex):
        if ord(array[i]) >= ord(pivot):
            array[i], array[partitionindex] = array[partitionindex], array[i]
            partitionindex += 1
    
    array[partitionindex], array[endindex] =  array[endindex], array[partitionindex]
    return partitionindex

    

def quicksort(array, startindex, endindex):
    if startindex < endindex:
        partitionindex = partition(array, startindex, endindex)
        quicksort(array, startindex, partitionindex - 1)
        quicksort(array, partitionindex + 1, endindex)


if __name__ == '__main__':
    count = int(raw_input())
    # array = map(int, raw_input().split())
    for i in xrange(count):
        arraylist, startindex, endindex = raw_input().split()
        array = list(arraylist)
        quicksort(array, int(startindex), int(endindex))
        print "".join(array)



