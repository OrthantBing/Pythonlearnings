string = raw_input()
i = 0
while i < len(string)-1:
    if string[i] == string[i+1]:
        string = string[:i] + string[i+2:]
        i = 0
    else:
        i += 1

if len(string) == 0:
    print "Empty String"
else:
    print string