def minmin(a, b):
    return "min(%s, %s)" % (a,b) 

value = int(raw_input())

a = "int"
b = "int"

for i in xrange(value - 1):
    a, b = a, minmin(a,b)

print b