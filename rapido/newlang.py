import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        inputval = input()
        a, delimiter, b = re.split('(\*|\+|\-|\/)', inputval)
        print(a, delimiter, b)
        
