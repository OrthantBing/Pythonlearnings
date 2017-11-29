inputdata = "St.Ri.g.n"

data = list(inputdata)
temp = []
for i in xrange(len(inputdata)):
    if data[i] != '.':
        temp.append(data[i])


for i in xrange(len(inputdata)):
    if data[i] != '.':
        data[i] = temp.pop()

print "".join(data)


