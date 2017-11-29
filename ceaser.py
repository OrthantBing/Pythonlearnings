length = int(raw_input())
string = raw_input().strip()
jump = int(raw_input())

small = []
capital = []

for i in xrange(65,91):
    capital.append(chr(i))

for j in xrange(97,123):
    small.append(chr(j))

outputstring = []
for s in string:
    if s.islower():
        tocal = (small.index(s) + jump) % 26
        outputstring.append(small[tocal])
    elif s.isupper():
        tocal = (capital.index(s) + jump) % 26
        outputstring.append(capital[tocal])
    else:
        outputstring.append(s)

print "".join(outputstring)
