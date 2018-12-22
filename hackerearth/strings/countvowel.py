if __name__ == "__main__":
    n = int(raw_input())
    for _ in xrange(n):
        string = raw_input().strip()
        count = 0
        for i in string:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                count += 1
        
        print count