if __name__ == '__main__':
    n, t = map(int, raw_input().split())
    array = map(int, raw_input().split())
    maxval = max(array)
    sumarray = sum(array)

    

    left = maxval
    right = sumarray
    mid = 0
    while left <= right:
        mid = (right - left) // 2 + left
        returnval = 0

        j = 0
        checkval = 0
        while j < len(array):
            checkval = checkval + array[j]
            if checkval > mid:
                checkval = array[j]
                returnval += 1
                j += 1
            
            elif checkval == mid:
                j += 1
                returnval += 1
                checkval = 0
            else:
                if j == len(array) - 1:
                    returnval += 1
                j += 1
        
        if returnval == t:
            break

        elif returnval < t:
            right = mid - 1
        else:
            left = mid + 1

    print mid
        
            

                
