def arraydistance(array, cost, part):
    sum = 0
    for j in xrange(len(part)-1,-1,-1):
        if j == len(part) - 1:
            if array.index(part[j]) == len(array) - 1:
                sum += 0
                continue
            else:
                calcsum = array[array.index(part[j])+1:]
        else:
            calcsum = array[array.index(part[j])+1:array.index(part[j+1])]
        # Here there can be 2 possiblities
        # it can be empty indicating the above and below are 2 positions

        print calcsum
        if len(calcsum) == 0:
            continue
        else:
            for i in calcsum:
                print j, i, cost[array.index(i)]
                sum += (i - part[j]) * cost[array.index(i)]
    return sum

array = [10,12,16,18,30,32]
cost = [15,17,18,13,10,1]
part = [10,32]

print arraydistance(array,cost,part)


    
