def partition(arr, low, high):
    print "i: %s, j: %s" % (low, high)
    val = arr[low]
    i = low
    j = high
    while True:
        while arr[i] < val:
            i += 1
            if i == high:
                break

        while arr[j] > val:
            j -= 1
            if j == low:
                break

        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    print "$$$$$$$$$$$$$$$$$"
    print (arr)
    print (low, j)
    print (arr[low], arr[j])
    arr[low], arr[j] = arr[j], arr[low]

    print arr

    return j

def sort(arr, low, high):
    if high <= low:
        return

    part = partition(arr, low, high)
    sort(arr, low, part - 1 )
    sort(arr, part + 1, high)


length = int(raw_input())
arr = map(int,raw_input().split())

# i am going to do this inplace
# since it is inplace use array positions
sort(arr, 0, len(arr) - 1)
print arr
