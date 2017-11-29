def knapsack(weights,values, key):
    rows = len(weights) + 1
    cols = key + 1

    T = [[0 for _ in range(cols)] for l in range(rows)]

    for i in range(1,rows):
        for j in range(1,cols):
            if j < weights[i-1]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], values[i-1] + T[i-1][j - weights[i-1]])

    print T

knapsack([1,3,4,5],[1,4,5,7], 7)
