from collections import Counter
a_len = int(raw_input())
a_list = map(int, raw_input().split())
b_len = int(raw_input())
b_list = map(int,raw_input().split())

a_hash = Counter(a_list)
b_hash = Counter(b_list)

# b_hash has everything.

result = []
for i in b_hash:
    if i in a_hash:
        if a_hash[i] != b_hash[i]:
            for _ in xrange(b_hash[i] - a_hash[i]):
                result.append(i)
    else:
        for _ in xrange(b_hash[i]):
            result.append(i)

print b_hash
print " ".join(map(str, sorted(result)))