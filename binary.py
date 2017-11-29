def dectobinary(val):
    test = ''
    while val > 0:
        test += str(val % 2)
        val = val // 2
    return test[::-1]

print dectobinary(31)
print dectobinary(12)
