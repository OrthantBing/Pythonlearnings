if __name__ == '__main__':
    setA_length, setA, count = int(raw_input()), set(map(int, raw_input().split())), int(raw_input())
    for i in range(count):
        command, count, setB = raw_input().split(), set(map(int, raw_input().split()))
        if command == 'intersection_update':
            setA &= setB
        elif command == 'symmetric_difference_update':
            setA ^= setB
        elif command == 'difference_update':
            setA -= setB
        elif command == 'update':
            setA |= setB

    print sum(setA)

