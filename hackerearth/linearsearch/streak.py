if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        string = raw_input().strip()
        streak = True
        for i in xrange(len(string)):
            if i + 1 < len(string):
                if string[i] == '2' and string[i+1] =='1':
                    streak = False
        
        if int(string) % 21 == 0:
            streak = False

        if not streak:
            print "The streak is broken!"
        else:
            print "The streak lives still in our heart!"
                    