"""
from collections import Counter
array = [1,2,3,4,5,6]
k = 3
test = Counter()

for i in range(len(array)):
    for j in range(i+1,(len(array))):
        if (array[i] + array[j]) % k == 0:
            test[array[i]] += 1
            test[array[j]] += 1

print test
"""
count, k = 4,3
array = [1,7,2,4]
remainder = map(lambda x: x%k, array)
print remainder
