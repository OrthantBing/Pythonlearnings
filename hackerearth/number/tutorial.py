def binaryexponent(x, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return binaryexponent((x * x)%m, n/2, m)
    else:
        return (x * binaryexponent((x * x)%m, (n-1)/2, m)) % m 

def binaryexponentiter(x, n, m):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % m
        x = x*x % m
        n = n // 2

    return result
        

if __name__ == '__main__':

