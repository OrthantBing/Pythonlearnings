n = int(raw_input())
array = []
for i in xrange(n):
    array.append(map(int,raw_input().strip()))

for i in xrange(1,n-1):
    for j in xrange(1,n-1):
        val = array[i][j]
        if val > array[i-1][j] and val > array[i+1][j] and val > array[i][j-1] and val > array[i][j+1]:
            array[i][j] = 'X'

for i in xrange(n):
    print "".join(map(str,array[i]))

