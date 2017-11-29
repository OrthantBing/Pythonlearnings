"""Linked Queue Implementation"""
class LinkedQueue(object):
    """FIFO queue implementation using singly linked list for storage."""
    class _Node(object):
        __slots__ = ['_element', '_next']

        def __init__(self, element, nextel=None):
            self._element = element
            self._next = nextel

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, val):
        """Add an element to the queue"""
        if self.is_empty():
            self._head = self._Node(val)
            self._tail = self._head
        else:
            self._tail._next = self._Node(val)
            self._tail = self._tail._next
        self._size += 1


    def dequeue(self):
        """Remove an element from the queue"""
        if self.is_empty():
            raise IndexError("Queue empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

        return answer


    def is_empty(self):
        """Check if queue is empty"""
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        """Return the first element of the queue"""
        if self.is_empty():
            raise IndexError("Queue empty")
        else:
            return self._head._element

    def next(self):
        if self._iterval is None:
            raise StopIteration()
        else:
            returnval =  self._iterval._element
            self._iterval = self._iterval._next
            return returnval

    def __iter__(self):
        self._iterval = self._head
        return self

if __name__ == "__main__":
    obj = LinkedQueue()
    obj.enqueue(10)

    obj.enqueue(20)
    obj.enqueue(30)
    for i in obj:
        print i
