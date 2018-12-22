if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        string = raw_input()
        left = 0
        right = len(string) - 1

        palindrome = True
        while left <= right:
            if string[left] != string[right]:
                palindrome = False
                break

            left += 1
            right -= 1

        if palindrome:
            if len(string) % 2 == 0:
                print "YES", "EVEN"
            else:
                print "YES", "ODD"
        else:
            print "NO"