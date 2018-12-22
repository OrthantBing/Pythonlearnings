if __name__ == '__main__':
    n = int(raw_input())
    array = map(int, raw_input().split())
    sumarray = []
    val = 0
    for i in xrange(len(array)):
        val = val + array[i]
        sumarray.append(val)

    print sumarray

    inputs = int(raw_input())
    for _ in xrange(inputs):
        val = int(raw_input())
        lower = 0
        higher = len(sumarray) - 1
        
        if val > sumarray[-1]:
            print -1
            continue
            
        found = False
        while lower <= higher:
            mid = ((higher - lower) // 2) + lower
            if val == sumarray[mid]:
                found = True
                break
            elif val < sumarray[mid]:
                higher = mid - 1
            elif val > sumarray[mid]:
                lower = mid + 1

        if found:
            print mid + 1
        else:
            print lower + 1

