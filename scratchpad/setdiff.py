# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

if __name__ == '__main__':
    count1, arr1, count2, arr2 = raw_input(), set(map(int,raw_input().strip().split())), raw_input(), set(map(int,raw_input().strip().split()))
    print(arr1)
    print(arr2)
    print("#" * 30)
    diff1 = arr1.difference(arr2)
    diff2 = arr2.difference(arr1)
    print(*arr1, sep='\n')
    print(*arr2, sep='\n')
