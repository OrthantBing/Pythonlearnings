def smallercount(array, query, left, right):
    if query < array[0]:
        return -1

    while left <= right:
        mid = ((right - left) // 2) + left
        if array[mid] == query:
            break
        elif array[mid] < query:
            left = mid + 1

        elif array[mid] > query:
            right = mid - 1
    

    while array[mid] >= query:
        mid -= 1
        if mid < 0:
            return -1

    return mid


def greatercount(array, query, left, right):
    if query > array[right]:
        return - 1

    while left <= right:
        mid = ((right - left) // 2) + left
        if array[mid] == query:
            break
        elif array[mid] < query:
            left = mid + 1
        elif array[mid] >= query:
            right = mid - 1

    while array[mid] <= query:
        mid += 1
        if mid > right:
            return -1
    return mid
        



if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    nelements = sorted(map(int, raw_input().split()))
    melements = sorted(map(int, raw_input().split()))

    #allelements = set(nelements + melements)

    nsumofelements = 0
    msumofelements = 0

    for i in nelements:
        fx = 0
        gx = 0

        smallercountindex = smallercount(melements, i, 0, m-1)
        if smallercountindex >= 0:

            fx = smallercountindex + 1
        
        greatercountindex = greatercount(melements, i, 0, m-1)
        if greatercountindex >= 0:
            gx = m - greatercountindex # m is the length so the +1 gets added here itself.

        nsumofelements = nsumofelements + (fx * gx)

    for j in melements:
        fx = 0
        gx = 0
        smallercountindex = smallercount(nelements, j, 0, n-1)
        if smallercountindex >= 0:
            fx = smallercountindex + 1

        greatercountindex = greatercount(nelements, j, 0 , n-1)
        if greatercountindex >= 0:
            gx = n - greatercountindex

        msumofelements = msumofelements + (fx * gx)


    if nsumofelements > msumofelements:
        print "Monk", nsumofelements - msumofelements
    elif msumofelements > nsumofelements:
        print "!Monk", msumofelements - nsumofelements
    else:
        print "Tie"

