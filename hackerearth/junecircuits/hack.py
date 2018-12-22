import sys
import itertools
if __name__ == "__main__":
    n, m, d = map(int, raw_input().split())
    fullset = map(int, raw_input().split())
    sortedfullset = sorted(fullset)
    
    length = sys.maxint
    subset = None

    combs = list(itertools.combinations(sortedfullset, n))

    for k in combs:
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