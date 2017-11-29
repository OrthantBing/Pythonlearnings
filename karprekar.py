def intlen(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def numsplit(n,pos):
    if intlen(n) <= pos:
        return (0,n)
    else:
        return (n // (10 ** pos), n % (10 ** pos))

lista = []
lowerbound, upperbound = int(raw_input()), int(raw_input())
for i in xrange(lowerbound,upperbound+1):
    a,b = numsplit(i ** 2, intlen(i))
    if a + b == i:
        lista.append(i)

if len(lista):
    print " ".join(map(str,lista))
else:
    print "INVALID RANGE"
