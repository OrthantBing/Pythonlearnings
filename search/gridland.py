from operator import itemgetter
if __name__ == '__main__':
    r, c, k = map(int, raw_input().split())
    mergeinterval = {}
    inputs = []
    for _ in xrange(k):
        inputs.append(map(int, raw_input().split()))
    
    inputs = sorted(inputs, key=itemgetter(0,1))

    for item in inputs:
        if item[0] in mergeinterval:
            tempc1, tempc2 = mergeinterval[item[0]][-1]
            if tempc2 < item[1]:
                mergeinterval[item[0]].append([item[1], item[2]])
            else:
                if tempc2 < item[2]:
                    mergeinterval[item[0]][-1][1] = item[2]
                else:
                    mergeinterval[item[0]][-1][1] = tempc2
        else:
            mergeinterval[item[0]] = []
            mergeinterval[item[0]].append([item[1], item[2]])
        
    #print mergeinterval

    contributionfromfullrows = (r - len(mergeinterval)) * c
    
    contributionsfrompartial = 0
    for key in mergeinterval:
        sum = 0
        for values in mergeinterval[key]:
            #print values
            #print c
            sum += values[1] - values[0] + 1
        contributionsfrompartial += c - sum
    
    print contributionfromfullrows + contributionsfrompartial

"""

        r, c1, c2 = map(int, raw_input().split())
        if r in mergeinterval:
            mergeinterval
        
        if r in mergeingerval:
            tempc1, tempc2 = mergeinterval[-1]

            # if there is no overlap
            # push it to the mergeinterval
            if tempc2 < c1:
                mergeinterval[r].append([c1, c2])

            # if there is overlap, probably it would be in the last part.
            else:
                mergeinterval[r][-1][1] = c2
        else:
            mergeinterval[r].append([c1,c2])
"""
