import math

def subsequence(array, binary, length):
    return_array = []
    for i in xrange(length):
        if (binary & (1 << i)):
            return_array.append(array[i])
    
    return return_array
    
def generate_subsequence(array):
    n = len(array)
    limit = int(math.pow(2, n))
    sub_sequence = []
    for i in xrange(1, limit):
        string = subsequence(array, i, n)
        sub_sequence.append(string)

    return sub_sequence

def xor(array):
    final = 0
    for i in array:
        a = final
        b = i
        xorval = 0

        multiplier = 1
        while (a > 0 or b > 0):
            tempa = a % 10
            tempb = b % 10
            a = a / 10
            b = b / 10

            tempxor = (tempa + tempb) % 10
            xorval = xorval + tempxor * multiplier
            multiplier = multiplier * 10
        final = xorval
    return xorval

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    input_array = map(long, raw_input().split())
    subsequencearray = generate_subsequence(input_array)
    d = {}

    
    for i in subsequencearray:
        length = len(i)
        if length in d:
            d[length].append(i)
        else:
            d[length] = []
            d[length].append(i)
    
    
    requiredarray = d[m]
    maxxorval = 0 
    
    for i in requiredarray:
        xorval = xor(i)
        if xorval > maxxorval:
            maxxorval = xorval
    
    print maxxorval
