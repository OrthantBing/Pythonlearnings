
if __name__ == '__main__':
    testcases = int(raw_input())
    for case in xrange(testcases):
        n, k = map(int, raw_input().split())
        police = 0
        for _ in xrange(n):
            array = raw_input().split()
            tracker = [True for _ in xrange(len(array))]
            # search for a police
            for i in xrange(len(array)):
                found = False
                if array[i] == 'P':
                    for j in xrange(i-k, i+k+1, 1):
                        if j >= 0 and j < len(array):
                            if array[j] == 'T' and tracker[j] is True:
                                found = True
                                tracker[j] = False
                                break
                    
                    if found:
                        police += 1
                
        print police
