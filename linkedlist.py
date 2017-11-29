class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setData(self, value):
        self.data = value

    def setNext(self, nextNode):
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        tempnode = Node(value)
        tempnode.setNext(self.head)
        self.head = tempnode
        self.count += 1

    def search(self, value):
        testnode = self.head
        while testnode is not None:
            if testnode.getData() == value:
                return True
            testnode = testnode.next

        return False

    def _remove(self, value):
        testnode = self.head

        prevnode = None
        while testnode is not None:
            if testnode.value == value:
                if prevnode is None:
                    self.head = self.head.next
                    return True
                else:
                    prevnode.next = testnode.next
                    return True
            else:
                prevnode = testnode
                testnode = testnode.next

        return False

    def remove(self, value):
        out = self._remove(value)
        if out:
            print "%s removed" % (value)
        else:
            print "%s not found" % (value)

    def __str__(self):
        testnode = self.head
        nodevalues = []
        while testnode is not None:
            nodevalues.append(testnode.value)
            testnode = testnode.next

        return "->".join(nodevalues)

    def __len__(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        return count

