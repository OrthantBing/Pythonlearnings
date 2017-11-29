import sys

s = int(raw_input())
coins = map(int, raw_input().split())

array = [ sys.maxsize ] * s

# Initialize the first value to 0
array[0] = 0
index = [-1] * s
for j in coins:
    for i in xrange(1,s):
        if j <= i:
            if array[i - j] + 1 < array[i]:
                array[i] = 1 + array[i - j]
                index[i] = coins.index(j)

print array
print index



