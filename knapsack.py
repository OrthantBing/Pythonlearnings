def knapsack(values, weights, total):
    total_items = len(weights)

    rows = total_items + 1
    cols = total + 1

    T = [[0 for _ in xrange(cols)] for _ in xrange(rows)]

    print T

    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i - 1]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], values[i-1] + T[i-1][j - weights[i-1]])

knapsack([1,4,5,7], [1,3,4,5], 7)

