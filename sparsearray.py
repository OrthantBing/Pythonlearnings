from collections import Counter

count = int(raw_input())
counterhash = Counter()
for _ in xrange(count):
    counterhash[raw_input().strip()] += 1

print counterhash

queries = int(raw_input())
for q in xrange(queries):
    print counterhash[raw_input().strip()]

    
