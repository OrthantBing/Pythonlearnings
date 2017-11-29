length = int(raw_input())

array = map(int, raw_input().split())

def swap(a, b):
    array[a], array[b] = array[b], array[a]

def toCorrectPosition(array, index, low, high):
    minindex = index
    maxindex = high
    while True:
        while array[low] <= array[index]:
            low += 1
            if low >= maxindex:
                break
        while array[high] >= array[index]:
            high -= 1
            if high <= minindex:
                break
        
        if low >= high:
            swap(index, high)
            break
        else:
            swap(low, high)
    
    print array
    return high

def sort(array, low, high):
    if low >= high: 
        return 
    part = toCorrectPosition(array, low, low, high)
    sort(array, low, part - 1)
    sort(array, part + 1, high)


sort(array, 0, len(array) - 1)

