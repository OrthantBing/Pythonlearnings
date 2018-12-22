if __name__ == '__main__':
    n, t = map(int, raw_input().split())
    array = map(int, raw_input().split())
    maxval = max(array)
    sumval = sum(array)

    returnval = 0
    for i in xrange(maxval, sumval + 1):
        checkval = 0
        j = 0 # incrementer array
        while j < len(array): 
            checkval = checkval + array[j] # we have the val to check right now
            if checkval > i:
                checkval = array[j] # remove from being counted
                returnval += 1 # increment the days         
                j += 1   
            
            elif checkval == i:
                j += 1
                returnval += 1
                checkval = 0
            else:
                if j == len(array) - 1:
                    returnval += 1

                j += 1
            
        
        # now we are out of the loop.
        if returnval == t:
            print i
            break

        returnval = 0

    




        
