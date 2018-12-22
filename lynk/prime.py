def sieve(num):
    array = [True for _ in range(num + 1)]
    number = 2
    while (number * number < num):
        if array[number] == True:
            for check in range(number*2, num+1, number):
                array[check] = False
        number+=1
    
    for i in range(2, num):
        if array[i]:
            print(i,)


if __name__ == '__main__':
    num = int(input())
    sieve(num)
    