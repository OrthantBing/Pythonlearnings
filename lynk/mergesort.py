
def merge(leftarray, rightarray):
    mergearray = []

    i = 0
    j = 0

    while i < len(leftarray) and j < len(rightarray):
        if leftarray[i] <= rightarray[j]:
            mergearray.append(leftarray[i])
            i += 1
        elif rightarray[j] <= leftarray[i]:
            mergearray.append(rightarray[i])
            j += 1

    while i < len(leftarray):
        mergearray.append(leftarray[i])
        i += 1

    while j < len(rightarray):
        mergearray.append(rightarray[j])
        j += 1
    
    return mergearray

def sort(array):
    if (len(array)) == 1:
        return array

    midpoint = len(array) // 2

    leftarray = sort(array[0:midpoint])
    rightarray = sort(array[midpoint:])
    return merge(leftarray, rightarray)

if __name__=='__main__':
    array = list(map(int, input().split()))
    sortedArray = sort(array)
    print (sortedArray)
