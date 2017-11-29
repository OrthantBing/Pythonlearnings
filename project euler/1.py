for _ in xrange(int(raw_input())):
    value = int(raw_input()) - 1
    
    divisibleby3 = 3 * ((value // 3) * ((value // 3) + 1) // 2)
    divisibleby5 = 5 * ((value // 5) * ((value // 5) + 1) // 2)
    divisibleby15 = 15 * ((value // 15) * ((value // 15) + 1) // 2)
    print divisibleby3 + divisibleby5 - divisibleby15