total = int(raw_input())
array = map(int, raw_input().split())

counter = [0] * 100

for i in array:
    counter[i] += 1

print " ".join(map(str,counter))



