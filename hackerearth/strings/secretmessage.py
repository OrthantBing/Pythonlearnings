if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        length, shiftinput = map(int, raw_input().split())
        string = raw_input().strip()
        shift = shiftinput % 26

        returnstring = list()
        for i in string:
            # Capital letters
            val = ord(i)
            shifted = val
            if val >= 65 and val <= 90:
                shifted = shifted + shift
                if shifted > 90:
                    shifted = shifted - 90 + 64
                    
                returnstring.append(chr(shifted))
            
            elif val >= 97 and val <= 122:
                shifted = shifted + shift
                if shifted > 122:
                    shifted = shifted - 122 + 96
                    
                returnstring.append(chr(shifted))

            # Check if it is a number
            elif i.isdigit():
                val = int(i)
                shiftnum = shiftinput % 10
                shifted = val + shiftnum
                shifted = shifted % 10
                returnstring.append(str(shifted))

            else:
                returnstring.append(chr(shifted))
        
        print "".join(returnstring)

                