import sys

if __name__ == '__main__':
    length = int(raw_input())
    array = map(int, raw_input().split())
    total = 0
    count = 0
    pos = False
    maxnegative = -sys.maxint + 1
    for i in array:
        if i > 0:
            total += i
            count += 1
            pos = True
        else:
            if i > maxnegative:
                maxnegative = i
        
    
    if pos:
        print total, count
    else:
        print maxnegative, 1

        
