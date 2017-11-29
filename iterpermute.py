def permutation(array, l, r):
    if l==r:
        return array
    else:
        for i in xrange(l,r+1):
            array[i], array[l] = array[l], array[i]
            permutation(array, l+1, r)
            array[i], array[l] = array[l], array[i]

print permutation([1,2,3,4],0,3)
#print permutation([1,2,3,4],0,3)
