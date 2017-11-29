"""
Node contains the unit of Linked list
"""
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

    def isEmpty(self):
        return self.value == None

    def isLast(self):
        self.next == None

    def __str__(self):
        return "Node: " + str(self.value)

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        head = self.head

        # If the head is empty
        if head is None:
            self.head = Node(value)
            return True

        # If value is less than the head
        if head.value > value:
                temp = Node(value)
                temp.next = head
                self.head = temp
                return True

        # Now we know that the value is greater than head.
        # So it should be either at the end or between the nodes.
        while head.next is not None:
            # If it is between two nodes
            if head.value < value and head.next.value > value:
                temp = Node(value)
                temp.next = head.next
                head.next = temp
                return True

            else:
                head = head.next

        # If we reach here the next value is the last one
        # and it is lesser than the value.
        temp = Node(value)
        head.next = temp
        
    def __str__(self):
        array = []
        temp = self.head
        while temp is not None:
            array.append(temp.value)
            temp = temp.next
        
        return " ".join(map(str,array))

        