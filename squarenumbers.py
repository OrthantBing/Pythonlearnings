import math
def squarenumbers(low,high):
    low = math.ceil(math.sqrt(low))
    high = math.floor(math.sqrt(high))
    return int(high-low) + 1

print squarenumbers(3,9)
