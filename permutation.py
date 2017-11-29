def permutation(arr):
    returnarray = []
    def permute(array, l, r):
        if l==r:
            print array
            print returnarray
            returnarray.append("".join(map(str,array)))
        else:
            for i in xrange(l,r+1):
                array[i], array[l] = array[l], array[i]
                permute(array, l+1, r)
                array[i], array[l] = array[l], array[i]

    permute(arr, 0, len(arr)-1)
    return returnarray

print permutation([1,2,3,4])
