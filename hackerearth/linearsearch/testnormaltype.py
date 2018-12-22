
    
if __name__ == '__main__':
    n = int(raw_input())
    array = raw_input().split()
    hash = {}
    subarrays = 0
    counter = 0
    requiredcounter = len(set(array))

    left = 0
    right = 0
    window = 0
    while left < len(array):
        while right < len(array) and window < requiredcounter:
            if array[right] in hash:
                hash[array[right]] += 1
            else:
                hash[array[right]] = 1
            
            if hash[array[right]] == 1:
                window += 1 ## new element added, increase window
            
            right += 1 ## while increment

        if window == requiredcounter:
            counter += len(array) - right + 1
        

        hash[array[left]] -= 1

        if hash[array[left]] == 0:
            window -= 1

        left += 1 ## while increment
    print counter
        
