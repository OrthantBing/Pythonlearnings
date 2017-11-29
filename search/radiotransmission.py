n, ran = map(int,raw_input().split())
array = map(int, raw_input().split())

print sorted(array)

i = 0
count = 0
location = 0

while i < n:
    location = x[i] + ran
    while i < n and x[i] <= location:
        i += 1
    
    # Only when x[i] > location we break out of loop
    # So we need this 
    i -= 1
    location = x[i] + ran
    while i < n and x[i] <= location:
        i += 1
    
    # Now we dont need to update i value
    # Since it is already moved out of the
    # previous block

    count += 1

print count
