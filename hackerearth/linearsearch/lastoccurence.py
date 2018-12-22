import sys
if __name__ == '__main__':
    length, search = map(int, raw_input().split())
    array = map(int, raw_input().split())

    found = False
    index = sys.maxint
    for i in xrange(len(array) - 1, -1, -1):
        if array[i] == search:
            found = True
            index = i + 1
            break

    if found:
        print index
    else:
        print -1