length = int(raw_input())
array = map(int, raw_input().split())

#f = open("input07.txt","r")
#length = int(f.readline())
#array = map(int, f.readline().split())

dip = []
up = []

def sorted(array):
    for i in xrange(len(array) - 1):
        if array[i] > array[i+1]:
            return 0
    return 1

for i in xrange(length):
    if i == 0:
        if array[i] > array[i+1]:
            up.append(i)
    elif i == length-1:
        if array[i] < array[i-1]:
            dip.append(i)
    elif array[i] > array[i-1] and array[i] > array[i+1]:
        up.append(i)
    elif array[i] < array[i-1] and array[i] < array[i+1]:
        dip.append(i)


print dip
print up
if len(dip) == 2 and len(up) == 2:
    array[up[0]], array[dip[-1]] = array[dip[-1]], array[up[0]]
    if sorted(array):
        print "swap %s %s" % (up[0]+1, dip[-1]+1)
    else:
        print "no"

elif len(dip) > 2 or len(up) > 2:
    print "no"

elif len(dip) == 1 and len(up) == 1:
    test = []
    for i in array:
        test.append(i)

    test[up[0]] , test[dip[0]] = test[dip[0]], test[up[0]]
    if sorted(test):
        print "swap %s %s" % (up[0]+1, dip[0]+1)
    else:
        pointa = min(up[0],dip[0])
        pointb = max(up[0],dip[0])
        test = array[:pointa] + array[pointa:pointb+1][::-1] + array[pointb+1:]
        if sorted(test):
            print "reverse %s %s" % (up[0]+1, dip[0]+1)
        else:
            print "no"

elif len(dip) == 1 and len(ups) == 0:
    test = array[dip[0]::-1] + array[dip[0]+1:len(array)]
    if sorted(test):
        print "reverse %s %s" % (1, dip[0]+1)
    else:
        print "no"

elif len(dip) == 0 and len(ups) == 1:
    test = array[:ups[0]+1] + array[ups[0]::][::-1]
    if sorted(test):
        print "reverse %s %s" % (ups[0]+1, len(array))


