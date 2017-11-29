
if __name__ == "__main__":
    length, times = map(int, raw_input().split())
    array = [0] * length
    d = {}
    for _ in xrange(times):
        a, b, summer = map(int, raw_input().split())
        for i in xrange(a-1, b):
            if i in d:
                d[i] += summer
            else:
                d[i] = summer
    
    if d.keys():
        print max(d.values())
    else:
        print 0
    
    """
    for _ in xrange(times):
        a,b,summer = map(int, raw_input().split())
        for i in xrange(a-1, b):
            array[i] += summer
    """
        
