if __name__ == '__main__':
    n = int(raw_input())
    array = sorted(map(int, raw_input().split()))
    print " ".join((str(sum(array[:n-1])),str(sum(array[1:]))))
