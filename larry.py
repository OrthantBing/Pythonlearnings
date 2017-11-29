for _ in xrange(int(raw_input())):
    length = int(raw_input())
    items = map(int,raw_input().split())
    inversionarray = []
    for i in xrange(length-1):
        count = 0
        for j in xrange(i+1,length):
            if items[i] > items[j]:
                count += 1
        inversionarray.append(count)
    
    maxval = sum(inversionarray)
    if maxval % 2 == 0:
        print "YES"
    else:
        print "NO"