class node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def next(self):
        if self.next is not None:
            return "Empty list"
        else:
            print self.value
            self = self.next


test = node("initial")
initialnode = test
array = [1,2,3,4,5]
for i in array:
    initialnode.next = node(i)
    initialnode = initialnode.next

while initialnode.next is not None:
    print initialnode.value
