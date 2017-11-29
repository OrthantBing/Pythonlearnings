def longestincreasingsubsequence(array):
    T = [1 for _ in array]
    for i in range(len(array)):
        for j in range(0,i):
            if array[i] > array[j]:
                if T[i] < T[j] + 1:
                    T[i] = T[j] + 1

    print T

longestincreasingsubsequence([3,4,-1,0,6,2,3])
