def binarysearch(array, l, r, key):
    counter = 0
    while r-l > 1:
        counter += 1
        m = l + ((r - l) // 2)
        if array[m] <= key:
            l = m
        else:
            r = m

    print counter
    if array[l] == key:
        return l
    else:
        return -1

print binarysearch([1,3,5,6,8,9,10,12,17,44],0,len([1,3,5,6,8,9,10,12,17,44]) - 1, 6)

def Traditional(array, l, r, key):
    counter = 0
    while l <= r:
        counter += 1
        m = l + (r - l) // 2
        if array[m] == key:
            print counter
            return m
        elif array[m] <= key:
            l = m+1
        else:
            r = m-1

    print counter
    return -1

print Traditional([1,3,5,6,8,9,10,12,17,44],0,len([1,3,5,6,8,9,10,12,17,44]) - 1, 6)
def Floor(array, l, r, key):
    while r-l > 1:
        pass

    return True
