# Write your code here
from collections import deque

if __name__ == '__main__':
    count = int(input())
    string = deque(list(input()))
    lastindex = len(string) - 1

    for i in range(count):
        leftarray = deque()
        rightarray = deque()
        test = lastindex 
        for i in range(test, -1, -2):

            leftarray.appendleft(string[i])
            if ( i - 1 >= 0):
                rightarray.append(string[i - 1])

        leftarray.extend(rightarray)
        string = leftarray


    print("".join(string))
    