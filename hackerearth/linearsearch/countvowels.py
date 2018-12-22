if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        string = raw_input().strip()
        counter = 0
        for i in string:
            if i=='a' or i =='e' or i == 'i' or i =='o' or i=='u' or i=='A' or i =='E' or i == 'I' or i =='O' or i =='U':
                counter += 1
            
        print counter