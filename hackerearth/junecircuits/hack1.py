import sys
import itertools
if __name__ == "__main__":
    n, m, d = map(int, raw_input().split())
    fullset = map(int, raw_input().split())
    sortedfullset = sorted(fullset)

    sliced = sortedfullset[:n]

    final = []
    for x in fullset:
        if x in sliced:
            final.append(x)

    print " ".join(map(str, final))

