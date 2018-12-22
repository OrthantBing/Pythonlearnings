if __name__ == "__main__":
    count = int(raw_input())
    string = list(raw_input())

    lastindex = len(string) - 1

    for _ in xrange(count):
        leftarray = []
        rightarray = []
        i = lastindex
        while i >= 0:
            if i == lastindex and lastindex % 2 != 0:
                leftarray.append(string[i])
                if i-1 >= 0:
                    leftarray.append(string[i - 1])
                if i-2 >= 0:
                    rightarray.append(string[i - 2])

                i -= 3
            else:
                leftarray.append(string[i])
                if i - 1 >= 0:
                    rightarray.append(string[i - 1])
                i -= 2
        
        leftarray.reverse()
        string = leftarray + rightarray

    
    print "".join(string)
        

