#First decreasing part of the sequence.

def next_permutation(string):
    i = len(string) - 1

    while i > 0 and string[i] < string[i-1]:
        i -= 1
        print i
    if i<=0:
        return False

    j = len(string) - 1
    while string[j] < string[i-1]:
        j -= 1
    string[j], string[i-1] = string[i-1], string[j]

    string[i:] = string[len(string) - 1 : i-1 : -1]
    return "".join(string)

print next_permutation(list("abcba"))
