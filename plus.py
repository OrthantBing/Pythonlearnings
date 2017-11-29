#!usr/local/bin/python

row, column = map(int,raw_input().split())

array = []

for _ in xrange(row):
    array.append(raw_input().strip())

dic = {}

for i in xrange(1,30,4):
    dic[i] = []

for i in xrange(row):
    for j in xrange(column):
        # We are going to enter inside only if the current is green
        # So that we need to check only the outer ones.
        # i.e. +-1
        if array[i][j] == 'G':
            # The max value we can shift up or down
            maxshiftcheck = min(row-1-i,i-0,column-1-j,j-0)
            #print (i,j)
            #print maxshiftcheck

            # append the vals to the appropriate dic.
            dicvalue = min(row-i,i-0,column-j,j-0) * 4 + 1
            if maxshiftcheck == 0:
                #dic[1].append((i,j))
                dic[1].append([(i,j)])
            else:
                # initially appending the block contributing to 1 square m
                #dic[1].append((i,j))
                dic[1].append([(i,j)])
                for k in xrange(1,maxshiftcheck+1):
                    # Check if the surrounding ones are contributing.
                    # If they are, we are appending with the previous values, so that we can filter overlapping ones.
                    if array[abs(i-k)][j] == 'G' and array[i+k][j] == 'G' and array[i][abs(j-k)] == 'G' and array[i][j+k] == 'G':
                        # eg:
                        # if (2,2) is the center,
                        # (1,2),(3,2),(2,1),(2,3) is the ones surrounding it.
                        # so appending it and creating a single tuple as (2,2),(1,2),(3,2),(2,1),(2,3)
                        # This will make sense if we append it to the current value. here it is 5 sq.m
                        #dic[4*k+1].append( ( tuple([(i-k,j),(i+k,j),(i,j-k),(i,j+k)] + [dic[4*(k-1)+1][-1][:]] ) ))
                        dic[4*k+1].append(  [(i-k,j),(i+k,j),(i,j-k),(i,j+k)] + dic[4*(k-1)+1][-1][:] )

                    else:
                        break
    
availabledic = sorted(filter(lambda x: len(dic[x]) > 0, dic),reverse=True)
print dic
maxval = 0


for i in xrange(len(availabledic)):
    #if maxval: 
        #break
    for j in xrange(i,len(availabledic)):
        #if maxval:
            #break
        if i == j:
            if len(dic[availabledic[j]]) == 1:
                continue
            else:
                found = False
                for k in xrange(len(dic[availabledic[j]])):
                    for l in xrange(k+1,len(dic[availabledic[j]])):
                        found = all([m not in dic[availabledic[j]][l] for m in dic[availabledic[j]][k]])
                        #print [m not in dic[availabledic[j]][l] for m in dic[availabledic[i]][k]]                       
                        if found:
                            test = availabledic[j] * availabledic[j]
                            if maxval < test:
                                maxval = test
                            #break
                    #if maxval:
                        #break
        # case when i != j we have different size of pluses to find area from
        else:
            for k in xrange(len(dic[availabledic[i]])):
                for l in xrange(len(dic[availabledic[j]])):
                    found = all([m not in dic[availabledic[j]][l] for m in dic[availabledic[i]][k]])
                    #print all([m not in dic[availabledic[j]][l]] for m in dic[availabledic[i]][k])
                    if found:
                        test = availabledic[i] * availabledic[j]
                        if maxval < test:
                            maxval = test
                        #break
                #if maxval:
                    #break
    #if maxval:
        #break

print maxval

                
