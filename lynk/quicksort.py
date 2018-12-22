
def partition(arr, left, right):
    randomPivotIndex = left
    i = left
    j = right

    while True:
        while arr[i] <= arr[randomPivotIndex]:
            i += 1
            if i >= right:
                break

        while arr[j] >= arr[randomPivotIndex]:
            j -= 1
            if j <= left:
                break

        if i >= j:
            arr[randomPivotIndex], arr[j] = arr[j], arr[randomPivotIndex]
            break

        else:
            arr[i], arr[j] = arr[j], arr[i]

    return j # The new random pivot element
        

def sortUtils(arr, left, right):
    # Terminating Condition
    if left >= right:
        return

    partitionElement = partition(arr, left, right)
    sortUtils(arr, left, partitionElement - 1)
    sortUtils(arr, partitionElement + 1, right)

def sort(array):
    sortUtils(array, 0, len(array) - 1)

if __name__ == '__main__':
    array = list(map(int, input().split()))
    sort(array)
    print(array)