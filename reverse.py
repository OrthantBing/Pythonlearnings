def reverse(num):
    finalnum = 0
    while num > 0:
        test = num % 10
        finalnum = finalnum * 10 + test
        num = num//10
    return finalnum

print reverse(112)
print reverse(3)
print reverse(2006)
print reverse(214)
