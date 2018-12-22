if __name__ == '__main__':
    count = int(raw_input())
    squarehash = {}
    for _ in xrange(count):
        key, val = map(int, raw_input().split())
        if key in squarehash:
            squarehash[key].append(val)
        else:
            squarehash[key] = [ val ]

    
    size = 0
    val = [-1, -1]

    for key in sorted(squarehash.keys()):
        array = squarehash[key]
        for i in xrange(len(array)):
            for j in xrange(i+1, len(array)):
                diff = 0
                if array[i] > array[j]:
                    diff = array[i] - array[j]
                else:
                    diff = array[j] - array[i]

                # lets check if hash exists.
                # xval to check
                xval = key + diff
                if xval in squarehash:
                    if array[i] in squarehash[xval] and array[j] in squarehash[xval]:
                        if diff > size:
                            size = diff
                            if array[i] < array[j]:
                                val[0] = key
                                val[1] = array[i]
                            else:
                                val[0] = key
                                val[1] = array[j]
    
    if val[0] == -1:
        print -1
    else:
        print val[0], val[1]

                        


    
    