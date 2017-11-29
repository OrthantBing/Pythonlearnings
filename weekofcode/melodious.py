count = int(raw_input())

consonants = "b c d f g h j k l m n p q r s t v w x z".split()
vowels = "a e i o u".split()

returnvalue1 = []
returnvalue2 = []

def append(array,flag):
    test = []
    if flag == 'c':
        corv = consonants
    else:
        corv = vowels

    if len(array) == 0:
        for i in corv:
            test.append("".join([i]))
    else:
        for i in corv:
            for j in array:
                test.append("".join([i,j]))

    return test

a1 = ['c','v','c','v','c','v']
a2 = ['v','c','v','c','v','c']

for i in xrange(count):
    returnvalue1 = append(returnvalue1,a1[i])
    returnvalue2 = append(returnvalue2,a2[i])


print "\n".join(returnvalue1 + returnvalue2)


"""
for i in consonants:
    for j in vowels:
        for k in consonants:
            for l in vowels:
                for m in consonants:
                    for n in vowels:
                        returnvalue.append("".join([i,j,k,l,m,n]))
"""




