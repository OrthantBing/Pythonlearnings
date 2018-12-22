if __name__ == '__main__':
    n = int(raw_input())
    output = {
        'G:': {},
        'M:': {}
    }
    for _ in xrange(n):
        arr = raw_input().split()
        for i in arr:
            if i.isdigit():
                if i in output[arr[0]]:
                    output[arr[0]][i] += 1
                else:
                    output[arr[0]][i] = 1
            
    # girlmaxdate, girlmaxval = 0, 0
    # boymaxdate, boymaxval = 0, 0
    # for i in output['G:']:
    #     date = int(i)
    #     if date > 0 and date < 32:
    #         currentmaxval = output['G:'][i] * 4
    #         if currentmaxval > girlmaxval:
    #             girlmaxdate = i
    #             girlmaxval = currentmaxval

    # for j in output['M:']:
    #     date = int(j)
    #     if date > 0 and date < 32:
    #         currentmaxval = output['M:'][j] * 3
    #         if currentmaxval > boymaxval:
    #             boymaxdate = j
    #             boymaxval = currentmaxval
    

    
    

