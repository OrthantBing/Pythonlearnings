from linkedlist import Node, LinkedList

test = LinkedList()

test.add("Anton")
test.add("Winston")
test.add("Christy")
test.add("Thomson")

print test

print "Count: %s" % (test.count)
print len(test)

print test.search("Christy")

test.remove("Thomso")
print test

test.remove("Thomson")
print test

test.remove("Anton")
print test

test.remove("Christy")
print test

test.remove("Winston")
print test

test.remove("Mus")

