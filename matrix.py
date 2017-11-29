import re

def findifBinA(matrixa, matrixb):
    columna, rowa = len(matrixa[0]), len(matrixa)
    columnb, rowb = len(matrixb[0]), len(matrixb)
    if rowb > rowa or columnb > columna:
        return False
    indexofmatcharray = {}
    for i in xrange(rowa):
        k = re.match(r"(.*)?"+ re.escape(matrixb[0]) + r"(.*)?",matrixa[i])
        if k:
            a,b = k.groups()
            if len(a) == 0:
                indexofmatcharray[i] = -1
            else:
                indexofmatcharray[i] = len(a) - 1

    if len(indexofmatcharray) == 0:
        return False
    else:
        for i in indexofmatcharray:
            x = i
            for j in xrange(rowb):
                print "++++++++++"
                print columna
                print indexofmatcharray[i]+1
                print columnb+indexofmatcharray[i]+1
                print "++++++++++"
                print matrixa[x][indexofmatcharray[i]+1:columnb+indexofmatcharray[i]+1]
                print x
                if matrixb[j] != matrixa[x][indexofmatcharray[i]+1:columnb+indexofmatcharray[i]+1]: # if the content of row of matrixb equal to substring of len
                    break
                else:
                    x += 1
            if x - i == rowb:
                return True

        return False

n = int(raw_input())
for i in range(n):
    row1,column1 = map(int,raw_input().split())
    matrixA = [raw_input() for _ in range(row1) ]
    row2, column2 = map(int, raw_input().split())
    matrixB = [raw_input() for _ in range(row2) ]
    print findifBinA(matrixA, matrixB)
