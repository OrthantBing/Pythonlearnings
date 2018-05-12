#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/micros-house-30/

def kadence(array):
    maxcurrent = maxglobal = array[0]
    for i in xrange(len(array)):
        maxcurrent = max(array[i], maxcurrent ^ array[i])
        if maxcurrent > maxglobal:
            maxglobal = maxcurrent
    
    return maxglobal


     

if __name__ == "__main__":
    n, m = map(int, raw_input.split())
    array_2d = []

    for _ in xrange(n):
        temp = map(int, raw_input.split())
        if len(temp) != m:
            print "The column length mismatch"
            exit

        array_2d.append(temp)

    for i in xrange(m):
        temp_array = []
        for j in xrange(n):
            temp_array.append(array_2d[j][i])




