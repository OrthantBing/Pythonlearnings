def spiralMatrix(array):
    n = len(array)
    m = len(array[0])
    k = 0
    l = 0

    print (n, m)
    while (k < m or l < n):
        for i in range(k, m, 1):
            print(array[l][i], end=" ")
        l += 1

        for i in range(l, n, 1):
            print(array[i][m-1], end=" ")

        m -= 1

        if (k < m):
            # print (l, m-1)
            for i in range(m-1,l-1,-1):
                print(array[n-1][i], end=" ")
            

        if (l < n):
            for i in range(n-1,k,-1):
                print(array[i][k], end=" ")
            k += 1

        
        

        break

if __name__ == "__main__":
    array = [
                [1,2,3,4,5,6],
                [7, 8, 9, 10, 11, 12],
                [13,14,15,16,17,18]
            ]

    spiralMatrix(array)