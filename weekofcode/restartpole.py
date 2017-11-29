from itertools import combinations
if __name__ == "__main__":
    poles, stacks = map(int,raw_input().split())
    polecostarray = []
    for _ in xrange(poles):
        polecostarray.append(tuple(map(int,raw_input().split())))

    dic = {}
    test = {}
    print polecostarray
    for i in xrange(len(polecostarray)):
        for j in xrange(len(polecostarray)-1,i,-1):
            #print polecostarray[j][0], polecostarray[i][0]
            dic[str(polecostarray[j][0]) + '-' + str(polecostarray[i][0])] = (polecostarray[j][0] - polecostarray[i][0]) * polecostarray[j][1]
            if polecostarray[i][0] in test:
                test[polecostarray[i][0]].append((polecostarray[j][0] - polecostarray[i][0]) * polecostarray[j][1])
            else:
                test[polecostarray[i][0]] = []
                test[polecostarray[i][0]].append((polecostarray[j][0] - polecostarray[i][0]) * polecostarray[j][1])

    
    polelist = map(lambda x: x[0], polecostarray)
    #tuple([polelist[0]] + list[i])
    totalcomb = [ tuple([polelist[0]] + list(i)) for i in combinations(polelist[1:], stacks)]
    print totalcomb
    print len(dic)


