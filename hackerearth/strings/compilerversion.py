import sys
if __name__ == '__main__':
    while True:
        string = sys.stdin.readline().rstrip('\n')
        returnstring = []
        i = 0
        comment = False
        if not string:
            break

        while i < len(string):
            if i + 1 < len(string):
                if string[i] == '/' and string[i+1] == '/':
                    comment = True
                    break
                elif string[i] == '-' and string[i+1] == '>':
                    returnstring.append('.')
                    i += 2
                else:
                    returnstring.append(string[i])
                    i += 1
            else:
                returnstring.append(string[i])
                i += 1
        
        if comment:
            while i < len(string):
                returnstring.append(string[i])
                i += 1

        print "".join(returnstring)
