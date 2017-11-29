test = int(raw_input())
array = map(int,raw_input().split())

while len(array) > 0:
    print len(array)
    minvalue = min(array)
    array = filter(lambda x: x > 0, map(lambda x: x - minvalue, array))
