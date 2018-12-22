def binarysearch(array, query):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = ((right - left) // 2) + left

        if array[mid] == query:
            return mid

        elif array[mid] < query:
            left = mid + 1
        
        elif array[mid] > query:
            right = mid - 1

    if array[mid] > query:
        while array[mid] > query:
            mid -= 1

    return mid

if __name__ == '__main__':
    count = int(raw_input())
    array = sorted(map(int, raw_input().split()))

    rounds = int(raw_input())
    for _ in xrange(rounds):
        power = int(raw_input())
        mid = binarysearch(array,power)
        outval = sum(array[0:mid+1])
        print mid + 1, outval
