if __name__ == '__main__':
    n = int(raw_input())
    k = {}
    for _ in xrange(n):
        inp = raw_input().strip()
        if inp in k:
            print " ".join((str(len(inp)), inp[len(inp)//2]))
            break
        l = list(inp)
        l.reverse()
        val = "".join(l)

        k[val] = 1
        
        