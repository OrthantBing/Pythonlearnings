def isPalindrome(val):
    check = list(str(val))
    start = 0
    end = len(check) - 1
    isPalindrome = True
    while start <= end:
        if check[start] != check[end]:
            isPalindrome = False
            break
        start += 1
        end -= 1
    
    return isPalindrome



if __name__ == "__main__":
    n = int(raw_input())
    for _ in xrange(n):
        a, b = map(int, raw_input().split())
        count = 0
        for i in xrange(a, b+1):
            if isPalindrome(i):
                count += 1
        
        print count

            