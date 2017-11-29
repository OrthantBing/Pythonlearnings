def separate(n):
    while n > 0:
        test = n%10
        yield test
        n = n//10

number = 1012
count = 0
for i in separate(number):
    if i == 0:
        pass
    elif number % i == 0:
        count += 1
    else:
        pass

print count
