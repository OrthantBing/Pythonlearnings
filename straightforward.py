def permutation(n, k):
    if k != 0 and n%k != 0:
        return -1

    arr = [None] * (n+1)
    for i in range(1, len(arr)):
        if arr[i] is None:
            arr[i] = i + k
            arr[i+k] = i

    return " ".join(map(str, arr[1:]))

for _ in xrange(int(raw_input())):
    n, k = map(int,raw_input().split())
    print permutation(n, k)
