def fact(x):
    return 1 if x<=1 else x * fact(x-1)

def findsmallercounttoright(string,index):
    count = 0
    for i in range(index+1,len(string)):
        if string[i] < string[index]:
            count += 1
    return count

def findrank(string):
    rank = 1;
    factval = fact(len(string))
    for i in xrange(len(string)):
        # find the possible positions
        factval /= len(string) - i
        countright = findsmallercounttoright(string,i)
        rank += countright * factval
    return rank

def next_permutation(string):
    i = len(string) - 1

    while i > 0 and string[i] <= string[i-1]:
        i -= 1
    if i<=0:
        return False
    j = len(string) - 1
    while string[j] <= string[i-1]:
        j -= 1
    string[j], string[i-1] = string[i-1], string[j]

    string[i:] = string[len(string) - 1 : i-1 : -1]
    return "".join(string)

string = "bbb"
print string
print string, "rank is ",findrank(string)
nextval = next_permutation(list(string))
print nextval
print nextval, "rank is ", findrank(nextval)
