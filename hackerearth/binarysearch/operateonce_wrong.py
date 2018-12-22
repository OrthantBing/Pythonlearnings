if __name__ == '__main__':
    cases = int(raw_input())
    for _ in xrange(cases):
        length = int(raw_input())
        array = map(int, raw_input().split())
        left = 0
        hash1 = {
            1: 0,
            2: 0,
            3: 0
        }
        right = 0
        maxval = 0
        while left < len(array):
            val = 0
            if right < left:
                right = left
                hash1 = {
                    1: 0,
                    2: 0,
                    3: 0
                }
            if hash1[1] <= 2 and hash1[3] <= 2:
                while right < len(array):
                    hash1[array[right]] += 1

                    if hash1[1] > 2 or hash1[3] > 2:
                        break

                    if hash1[1] == 2 and hash1[3] == 0:
                        val = hash1[2] + 1

                    elif hash1[1] == 0 and hash1[3] == 2:
                        val = hash1[2] + 1
                        

                    elif hash1[1] == 1 and hash1[3] == 1:
                        val = hash1[2] + 2

                    elif (hash1[1] > 1 and hash1[3] == 1) or (hash1[1] == 1 and hash1[3] > 1):
                        val = hash1[2] + 2
                        
                    else:
                        val = hash1[2]

                    
                    if val > maxval:
                        maxval = val
                    #print left, right, val, hash1, maxval
                    right += 1
            
            if hash1[array[left]] > 0:
                hash1[array[left]] -= 1
            
            #print hash1
            left += 1

        print maxval

            


            
            

                

    