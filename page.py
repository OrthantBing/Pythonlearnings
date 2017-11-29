def group(lst, n):
    for i in range(0,len(lst),n):
        val = lst[i:i+n]
        yield tuple(val)

chapters, ppp = map(int,raw_input().split())
ppc = map(int,raw_input().split())

dict = []
for i in xrange(1,chapters+1):
    for j in group(range(1,ppc[i-1]+1), ppp):
        #dict.append({i: j})
        dict.append(j)

count = 0
for i in range(len(dict)):
    if i+1 in dict[i]:
        count += 1

"""
for i in range(len(dict)):
    if i+1 in dict[i]:
        print dict[i]
        if i+1 in dict[i][i+1]:
            count += 1
"""
print dict
print count
