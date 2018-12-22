def permutation(arr, l):
    if (l == 1):
#        yield ",".join(map(str,arr))
        yield arr
    for i in xrange(l):
        for j in permutation(arr, l-1):
#            yield ",".join(map(str,arr))
            yield arr

        if l%2==1:
            arr[0], arr[l-1] = arr[l-1], arr[0]
        else:
            arr[i], arr[l-1] = arr[l-1], arr[i]

cases = int(raw_input())
for _ in xrange(cases):
    found = 0
    test, diff = map(int, raw_input().split())
    values = [i for i in xrange(1,test+1)] # this contains the original files.
    for i in permutation([i for i in xrange(1,test+1)], test): # i contains the permutation value

        outval = [ abs(i[k] - values[k] ) for k in xrange(len(i)) ]

        if all( j == diff for j in outval):
            print " ".join(map(str, i))
            found = 1
            break

    if(found == 0):
        print -1
