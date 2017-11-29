import re

string1 = "qwerasdf"
string2 = "qwerbsdf"

matchindex = 0
operation = 0
for i in reversed(range(len(string2))):
    operation +=1
    if (re.match(string2[:i],string1)):
        matchindex = i
        break;

print "operation: " + str(operation)
print len(string1) - matchindex + operation
