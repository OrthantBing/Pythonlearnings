# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/sumit-and-chocolates-c9e3069d/

if __name__ == '__main__':
    cases = int(raw_input())
    
    

    for _ in xrange(cases):
        n, k = map(int, raw_input().split())
        string = raw_input().strip()
        left = 0    

        maxval = 0
        while left <= len(string) - 1:
            kalticount = 0
            pointer = left + 1
            val = 0
            while kalticount <= k:
                if pointer >= len(string):
                    break
                if string[pointer] == string[left]:
                    val += 1
                    pointer += 1
                else:
                    if kalticount == k:
                        break
                    kalticount += 1
                    val += 1
                    pointer += 1
            
            if val > maxval:
                maxval = val

            left += 1
        
        print maxval + 1
             
        
