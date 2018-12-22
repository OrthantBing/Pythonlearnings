def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def extendedgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extendedgcd(b, a%b)
        return (g, y, x-(a//b)*y)
  

if __name__ == '__main__':
    print gcd(81, 18)
    print extendedgcd(16, 10)
    
