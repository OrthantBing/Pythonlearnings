if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        string = raw_input().strip()
        suvojit = 0
        suvo = 0
        for i in xrange(len(string)):
            if i + 6 < len(string):
                if string[i] == 'S' and string[i+1] == 'U' and string[i+2] == 'V' and string[i+3] == 'O' and string[i+4] == 'J' and string[i+5] == 'I' and string[i+6] == 'T':
                    suvojit += 1
                elif string[i] == 'S' and string[i+1] == 'U' and string[i+2] == 'V' and string[i+3] == 'O':
                    suvo += 1
            elif i + 3 < len(string):
                if string[i] == 'S' and string[i+1] == 'U' and string[i+2] == 'V' and string[i+3] == 'O':
                    suvo += 1
    
        strs = "SUVO = " + str(suvo) + ", SUVOJIT = " + str(suvojit)
        print strs
                
            
