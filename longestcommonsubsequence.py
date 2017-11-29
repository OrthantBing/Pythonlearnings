def longestcommonsubsequence(sequence1, sequence2):

    rows = len(sequence1) + 1

    cols = len(sequence2) + 1

    # Initialize the 2D matrix to 0
    T = [[0 for _ in xrange(cols)] for i in xrange(rows)]

    for i in xrange(1, rows):
        for j in xrange(1, cols):
            if sequence1[i-1] == sequence2[j-1]:
                T[i][j] = T[i-1][j-1] + 1

            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])


    print T

    commonval = []
    row = rows - 1
    col = cols - 1
    while row != 0 and col != 0:
        if T[row][col] == T[row-1][col]:
            row -= 1
        elif T[row][col] == T[row][col-1]:
            col -= 1
        else:
            print row
            commonval.append(sequence1[row-1])
            row -= 1
            col -= 1

    print commonval
longestcommonsubsequence("abcdef", "ackfjh")

