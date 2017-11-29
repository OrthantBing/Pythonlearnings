'''
test = {}
n = int(raw_input())
for _ in range(n):
    name = str(raw_input())
    score = float(raw_input())
    if score in test:
        test[score].append(name)
    else:
        test[score] = []
        test[score].append(name)

def second_smallest(array):
    m1 = m2 = float('+inf')
    count = 0
    for i in array:
        if i == m1 or i == m2:
            continue
        count += 1
        if i < m1:
            if i < m2:
                m2, m1 = i, m2
            else:
                m1 = i
    return m1 if count >= 2 else None

for j in test[second_smallest(test.keys())]:
    print j

#    list.append([name, score])

# list.sort(key=lambda x: x[1])
'''
test = []
n = int(raw_input())
for _ in range(n):
    name = str(raw_input())
    mark = float(raw_input())
    test.append([name, mark])
    
second_lowest = list(set(sorted([marks for name, marks in test])))[1]

print sorted([marks for name, marks in test])

print second_lowest

for i in test:
    if i[1] == second_lowest:
        print i[0]


