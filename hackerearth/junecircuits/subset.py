import sys
if __name__ == "__main__":
    n, m, d = map(int, raw_input().split())
    fullset = map(int, raw_input().split())
    sortedfullset = sorted(fullset)
    
    length = sys.maxint
    subset = None

    for i in xrange(1<<n-1, 1<<m):
        k = []
        for j in xrange ( m ):
            if (( i & (1 << j)) > 0):
                k.append(sortedfullset[j])

        if len(k) == n:
            out = set()
            for x in xrange(n):
                for y in xrange(x,n):
                    if k[x] + k[y] > d:
                        out.add((k[x], k[y])) 
            if len(out) < length:
                length = len(out)
                subset = k

    final= []
    for x in fullset:
        if x in subset:
            final.append(x)

    print " ".join(map(str, final))
    


    
            

            
        


        
        
       


    
