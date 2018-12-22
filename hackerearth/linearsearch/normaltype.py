if __name__ == "__main__":
    n = int(raw_input())
    array = map(int, raw_input().split())
    uniqcount = len(set(array))
    counter = 0
    for i in xrange(len(array)):
        for j in xrange(i + uniqcount - 1, len(array)):
            if len(set(array[i:j+1])) == uniqcount:
                counter += 1

    print counter