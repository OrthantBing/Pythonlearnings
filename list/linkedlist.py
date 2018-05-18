# https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/remove-friends-5/
class LinkedList(object):
    class Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header._next = self.trailer
        self.trailer._prev = self.header
        self.size = 0

    def add(self, element):
        prev = self.trailer._prev
        next = self.trailer
        current = self.Node(element, prev, next)
        prev._next = current
        next._prev = current

    def __str__(self):
        root = self.header
        array = []
        if root._next is None:
            return "Empty List"
        else:
            root = root._next

        while root._next is not None:
            array.append(root._element)
            root = root._next

        return " ".join(map(str, array))

    def deletefriend(self, counter):
        todelete = counter
        
        while todelete > 0:
            print todelete
            root = self.header
            if root._next is None:
                return "Empty List"
            else:
                root = root._next

            DeleteFriend=False
            while root._next is not None:
                prev = root._prev
                current = root
                nextone = root._next

                if current._element < nextone._element:
                    prev._next = nextone
                    nextone._prev = prev
                    DeleteFriend = True
                    # we have deleted the current one
                    todelete -= 1
                    break

                root = root._next


            if DeleteFriend is False:
                trailer = self.trailer
                todelete = self.trailer._prev
                prev_todelete = todelete._prev
                trailer._prev = prev_todelete
                prev_todelete = trailer
                todelete -= 1

                



        
    
if __name__ == '__main__':
    count = int(raw_input())
    for _ in xrange(count):
        a, b = map(int, raw_input().split())
        lists = map(int, raw_input().split())
        linked_list = LinkedList()
        for i in lists:
            linked_list.add(i)
        
        linked_list.deletefriend(b)
        print linked_list
            
