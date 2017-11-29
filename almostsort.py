#length = int(raw_input())
#array = map(int, raw_input().split())

f = open('input17.txt','r')
length = int(f.readline())
array = map(int, f.readline().split())
test = sorted(array)

elems = []

for i in xrange(length):
    if test[i] != array[i]:
#        print test[i], array[i]
        elems.append(i)

print elems

if len(elems) == 2:
    print "yes"
    print "swap %s %s" % (elems[0]+1, elems[1]+1)
elif len(elems) > 2:
    i = 1
    while i < len(elems):
        print elems[i], elems[i-1], array[elems[i]], array[elems[i-1]]
        if elems[i] - elems[i-1] != 1 or array[elems[i]] > array[elems[i-1]]:
            print i, len(elems)
            print "no"
            break
        i += 1

    if i == len(elems):
        print "yes"
        print "reverse %s %s" % (elems[0]+1, elems[-1]+1)
