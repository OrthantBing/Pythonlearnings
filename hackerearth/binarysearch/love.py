#https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/charsi-in-love/

def binarysearch(array, query, left, right):
    while left <= right:
        mid = ((right - left) // 2) + left
        if array[mid] == query:
            return mid
        elif array[mid] > query:
            right = mid - 1
        elif array[mid] < query:
            left = mid + 1


    if array[mid] == query:
        
        return mid
    else:
        return -1


if __name__ == '__main__':
    inputval = int(raw_input())
    i = 1
    array = []
    while (i * (i + 1)) // 2 < inputval:
        array.append((i * (i+1)) // 2)
        i += 1

    found = False
    for i in xrange(len(array)):
        tocheck = inputval - array[i]
        
        binarysearchval = binarysearch(array, tocheck, i, len(array) - 1)
        
        
        if binarysearchval != -1:
            found = True
            break
        else:
            found = False

    if found:
        print "YES"
    else:
        print "NO"

    #print array




    
