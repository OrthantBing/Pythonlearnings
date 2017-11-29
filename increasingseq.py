a,b = map(int,raw_input().split())
seq = map(int,raw_input().split())
count = 0
for i in xrange(a):
    if seq[i] + b in seq and seq[i] + 2*b in seq:
        count += 1

print count
