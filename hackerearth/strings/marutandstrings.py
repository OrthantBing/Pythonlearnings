#https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/marut-and-strings-4/
import sys
if __name__ == '__main__':
    n_str = raw_input()
    n = 0
    if not bool(n_str):
        print "Invalid Test"
        sys.exit()

    elif not str.isdigit(n_str):
        print "Invalid Test"
        sys.exit()
    else:
        n = int(n_str)

    if n < 1 or n > 10:
        print "Invalid Test"
        sys.exit()

    for _ in xrange(n):
        lower = 0
        upper = 0
        junk = 0
        invalid = False
        inp = list(raw_input().strip())
        if len(inp) < 1 or len(inp) > 100:
            print "Invalid Input"
            sys.exit()

        for i in inp:
            val = ord(i)
            if val == 32:
                invalid = True
                break
            elif val >= 97 and val <= 122:
                lower += 1
            elif val >= 65 and val <= 90:
                upper += 1
            else:
                junk += 1
        
        if invalid:
            print "Invalid Input"
            continue

        if lower == 0 and upper == 0:
            print "Invalid Input"
            continue
        
        if lower <= upper:
            print lower
        else:
            print upper
