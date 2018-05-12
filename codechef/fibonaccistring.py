#https://www.codechef.com/problems/CLFIBD

if __name__ == "__main__":
    for t in range(int(input())):
        inputstring = raw_input().strip()
        k = {}
        for i in inputstring:
            if i in k:
                k[i] += 1
            else:
                k[i] = 1

        values = [value for _, value in k.iteritems()]

        values.sort()

        ok = True
        n = len(values)
        if n >= 3:
            for i in xrange(2,n):
                if values[i] != values[i-1] + values[i-2]:
                    ok = False
        if ok:
            print "Dynamic"
        else:
            print "Not"



    