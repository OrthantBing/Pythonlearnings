from collections import Counter
from itertools import combinations

length = int(raw_input())
string = raw_input()

C = Counter(string)

max_len = 0
for (c1,c2) in combinations(set(string),2):
    if abs(C[c1] - C[c2]) <= 1:
        t = [i for i in string if i in [c1,c2]]
            if all([t[j] != t[j-1] for j in xrange(1, len(t)) ]):
                max_len = max(max_len, len(t))

print max_len
