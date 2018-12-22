if __name__ == '__main__':
    stringlist = list(raw_input().strip())
    k = {}
    finalstring = []
    for i in stringlist:
        if i not in k:
            k[i] = 1
            finalstring.append(i)
        
    print "".join(finalstring)
    
        
    
