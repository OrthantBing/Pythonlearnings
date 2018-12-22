def factorize(v):
    returnlist = list()
    i = 2
    while i * i <= v:
        while v % i == 0:
            returnlist.append(i) 
            v = v // i

        i += 1

    if (v != 1):
        returnlist.append(v)

    return returnlist

if __name__ == '__main__':
    print factorize(50)
