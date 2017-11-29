def permutation(arr):
    returnvalue = []
    def permute(array,l):
        if l == 1:
            returnvalue.append("".join(map(str,array)))

        for i in xrange(l):
            permute(array,l-1)
            if i % 2 == 1:
                array[0], array[l-1] = array[l-1], array[0]
            else:
                array[i], array[l-1] = array[l-1], array[i]

    permute(arr,len(arr))
    return returnvalue

print permutation([1,2,3,4])


