# Worst possible implementation.
import re

def possible(inp, out):
    if inp == out:
        return True
    elif len(inp) > len(out):
        return False
    elif (bool(re.search(inp,out)) or bool(re.search("".join(reversed(inp)),out))) != True:
        return False
    else:
        return possible(inp + 'A', out) or possible("".join(reversed(inp)) + "B", out)

inp = raw_input()
out = raw_input().strip()

if possible(inp, out):
    print "Possible"
else:
    print "Impossible"