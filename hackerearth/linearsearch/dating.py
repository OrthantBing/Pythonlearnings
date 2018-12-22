if __name__ == '__main__':
    n = int(raw_input())
    output = { }
    for _ in xrange(n):
        arr = raw_input().split()
        for i in arr:
            if i.isdigit():
                if i in output:
                    if arr[0] == 'G:':
                        output[i] += 4
                    elif arr[0] == 'M:':
                        output[i] += 3
                else:
                    if arr[0] == 'G:':
                        output[i] = 4
                    elif arr[0] == 'M:':
                        output[i] = 3

    maxval = 0
    dateval = 0
    isThereDate = True
    for key in output:
        date = int(key)
        if date > 0 and date < 32:
            if maxval == output[key]:
                isThereDate = False
                break
            elif maxval <= output[key]:
                dateval = key
                maxval = output[key]


    if not isThereDate:
        print "No Date"
    elif dateval in ['19', '20']:
        print "Date"
    else:
        print "No Date"
        
                