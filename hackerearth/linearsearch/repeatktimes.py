import sys
if __name__ == '__main__':
    n = int(raw_input())
    array = raw_input().split()
    repeatvalue = int(raw_input().strip())
    h = {}
    for i in array:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
    
    lower = sys.maxint

    for key, value in h.iteritems():
        if value == repeatvalue:

            if int(key) < int(lower):
                lower = key
        
    print lower
            