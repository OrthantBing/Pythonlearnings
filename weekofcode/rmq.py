length, querylength = map(int,raw_input().split())

array = map(int,raw_input().split())

for _ in xrange(querylength):
    left, right, x, y = map(int, raw_input().split())
    print len(filter(lambda z: z % x == y, array[left:right+1]))