k = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

if __name__ == "__main__":
    n = int(raw_input())
    for i in xrange(n):
        count = int(raw_input())
        string = raw_input().strip()
        returnstring = []
        rna = False
        for z in string:
            if z in k:
                returnstring.append(k[z])
            else:
                rna = True
                break
        if rna:
            print "Error RNA nucleobases found!"
        else:
            print "".join(returnstring)

        

