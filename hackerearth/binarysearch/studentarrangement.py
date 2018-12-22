#https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/student-arrangement-6/
if __name__ == '__main__':
    n, m, k = map(int, raw_input().split())
    store = [0 for _ in xrange(m)]
    # we will not include 0th pos
    unablecount = 0

    array = map(int, raw_input().split())
    length = len(array)
    for i in array:
        updated = False
        if store[i-1] < k:
            store[i-1] += 1
            updated = True
        else:
            for t in xrange(i, i+k):
                
                index = t % k

                if store[index] < k:
                    store[index] += 1
                    unablecount += 1
                    updated = True
                    break
        
        if not updated:
            unablecount += 1

    print unablecount

                