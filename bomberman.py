row, column, sec = map(int,raw_input().split())

def _Print(arr):
    for i in arr:
        print "".join(map(str,i))

def convert(val):
    if val == '.':
        return 0
    else:
        return 3
def _Print1(array):
    def rep(k):
        if k == 0:
            return "."
        else:
            return "0"

    for i in array:
        print "".join(map(rep, i))

def swapfor3and5(array):
    for i in xrange(len(array)):
        for j in xrange(len(array[0])):
            if array[i][j] - 1 == 0:
                array[i][j] = 0
                if i > 0 and i < len(array) - 1 and j > 0 and j < len(array[0]) -1:
                    array[i-1][j] = 0
                    array[i+1][j] = 0
                    array[i][j-1] = 0
                    array[i][j+1] = 0

                elif i == 0 and j == 0:
                    array[i+1][j] = 0
                    array[i][j+1] = 0
                elif i == len(array) - 1 and j == len(array[0]) - 1:
                    array[i][j-1] = 0
                    array[i-1][j] = 0

                elif i == 0 and j == len(array[0]) - 1:
                    array[i][j-1] = 0
                    array[i+1][j] = 0

                elif i == len(array) - 1 and j == 0:
                    array[i-1][j] = 0
                    array[i][j+1] = 0

                elif i == 0 and j > 0 and j < len(array[0]) - 1:
                    array[i+1][j] = 0
                    array[i][j-1] = 0
                    array[i][j+1] = 0

                elif j == 0 and i > 0 and i < len(array) - 1:
                    array[i-1][j] = 0
                    array[i][j+1] = 0
                    array[i+1][j] = 0

                elif i == len(array) - 1 and j > 0 and j < len(array[0]) - 1:
                    array[i][j-1] = 0
                    array[i][j+1] = 0
                    array[i-1][j] = 0

                elif j == len(array) - 1 and i > 0 and i < len(array[0]) - 1:
                    array[i-1][j] = 0
                    array[i+1][j] = 0
                    array[i][j-1] = 0


            elif array[i][j] > 0:
                array[i][j] -= 1

array = []
for i in xrange(row):
    array.append(map(int,map(convert,list(raw_input()))))

if sec % 2 == 0:
     #print ["".join(map(str,[0 for i in xrange(column)])) for _ in xrange(row)]
     _Print([[0 for i in xrange(column)] for _ in xrange(row)])

else:
    actualval = -1
    if sec <=5:
        actualval = sec
    else:
        while sec <= 5:
            sec -= 4

        actualval = sec

    for i in xrange(1,actualval+1):
        # Second -> i
        if i == 1:
            for i in xrange(len(array)):
                for j in xrange(len(array[0])):
                    if array[i][j] > 0:
                        array[i][j] -= 1
            print array
            _Print1(array)
        elif i == 2:
            for i in xrange(len(array)):
                for j in xrange(len(array[0])):
                    if array[i][j] > 0:
                        array[i][j] -= 1
                    elif array[i][j] == 0:
                        array[i][j] = 3
            print array
            _Print1(array)

        elif i == 3:
            test = []
            for k in array:
                test.append(k[:])
            for i in xrange(len(array)):
                for j in xrange(len(array[0])):
                    if array[i][j] - 1 == 0:
                        array[i][j] = 0
                        # other than corners
                        if i > 0 and i < len(array) - 1 and j > 0 and j < len(array[0]) -1:
                            array[i-1][j] = 0
                            array[i+1][j] = 0
                            array[i][j-1] = 0
                            array[i][j+1] = 0
                        # corner(0,0)
                        elif i == 0 and j == 0:
                            array[i+1][j] = 0
                            array[i][j+1] = 0
                        #corner(len-1,len-1)
                        elif i == len(array) - 1 and j == len(array[0]) - 1:
                            array[i][j-1] = 0
                            array[i-1][j] = 0
                        #corner(0,len-1)
                        elif i == 0 and j == len(array[0]) - 1:
                            array[i][j-1] = 0
                            array[i+1][j] = 0

                        elif i == len(array) - 1 and j == 0:
                            array[i-1][j] = 0
                            array[i][j+1] = 0

                        elif i == 0 and j > 0 and j < len(array[0]) - 1:
                            array[i+1][j] = 0
                            array[i][j-1] = 0
                            array[i][j+1] = 0

                        elif j == 0 and i > 0 and i < len(array) - 1:
                            array[i-1][j] = 0
                            array[i][j+1] = 0
                            array[i+1][j] = 0

                        elif i == len(array) - 1 and j > 0 and j < len(array[0]) - 1:
                            array[i][j-1] = 0
                            array[i][j+1] = 0
                            array[i-1][j] = 0

                        elif j == len(array) - 1 and i > 0 and i < len(array[0]) - 1:
                            array[i-1][j] = 0
                            array[i+1][j] = 0
                            array[i][j-1] = 0


                    elif array[i][j] > 0:
                        array[i][j] -= 1

                    print "XXXXXXXXXXXXXXXXXXXXXX"
                    print array[i]
                    _Print1(array)
        elif i == 4:
            for i in xrange(len(array)):
                for j in xrange(len(array[0])):
                    if array[i][j] == 0:
                        array[i][j] = 3
                    else:
                        array[i][j] -= 1

        elif i == 5:
            swapfor3and5(array)
            # do as in 3

    _Print1(array)
