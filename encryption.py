import math
text = "".join(raw_input().split())

rows, columns = math.floor(math.sqrt(len(text))),math.ceil(math.sqrt(len(text)))

array = []

i = int(columns)
while True:
    if (i >= int(len(text))):
        array.append(text[i-int(columns):int(len(text))])
        break;
    array.append(text[i-int(columns):i])
    i += int(columns)

print array
#for i in range(int(columns),len(text)+int(columns),int(columns)):
#    array.append(text[i-int(columns):i])

print " ".join([ "".join(map(lambda x: x[i], array)) for i in range(int(columns))])
