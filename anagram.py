string1 = raw_input().strip()
string2 = raw_input().strip()

def isAnagram(string1, string2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in xrange(len(string1)):
        index = ord(string1[i]) - ord('a')
        c1[index] += 1

    for i in xrange(len(string2)):
        index = ord(string2[i]) - ord('a')
        c2[index] += 1


    for i in xrange(26):
        if c1[i] != c2[i]:
            return False
        else:
            pass

    return True

print isAnagram(string1, string2)

