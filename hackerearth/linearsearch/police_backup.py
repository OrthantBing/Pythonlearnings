if __name__ == '__main__':
    testcase = int(raw_input())
    
    for case in xrange(testcase):
        n, k = map(int, raw_input().split())
        police = 0
        for _ in xrange(n):
            array = raw_input().split()
            i = 0
            # for i in xrange(len(array)):
            while i < len(array):
                if i - 1 >= 0:
                    if (array[i] == 'P' and array[i - 1] == 'T') or (array[i] == 'T' and array[i-1] == 'P'):
                        
                        police += 1
                        i += 1

                elif i + 1 < len(array):
                    if (array[i] == 'P' and array[i+1] == 'T') or (array[i] == 'T' and array[i+1] == 'P'):
                        
                        police += 1
                        i += 2
                i += 1
                

        
        print police