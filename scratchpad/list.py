if __name__ == '__main__':
    N = int(raw_input())
    dummyarray = []
    for i in range(N):
        command = raw_input().strip().split(" ")
        # Ideally if it is known that all the ones are ints
        # We can do [i for i in inputstring.split(" ")]
        # or map(int, inputstring.split(" "))
        if command[0] == "insert":
            #dummyarray[command[1]] = command[2]
            dummyarray.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print dummyarray
        elif command[0] == "remove":
            dummyarray.remove(int(command[1]))
        elif command[0] == "append":
            dummyarray.append(int(command[1]))
        elif command[0] == "sort":
            dummyarray.sort()
        elif command[0] == "pop":
            dummyarray.pop()
        elif command[0] == "reverse":
            dummyarray.reverse()
            dummyarray.index
