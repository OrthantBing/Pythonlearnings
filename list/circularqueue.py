"""Circular queue"""
class CircularQueue(object):
    class _Node(object):
        __slots__ = ['_element', '_next']

        def __init__(self, element, nextel=None):
            self._element = element
            self._next = nextel

    def __init__(self):
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self, val):
        # when there is no element in the circular queue
        if self.is_empty():
            self._tail = self._Node(val)
            self._tail._next = self._tail

        else:
            element = self._Node(val)
            element._next = self._tail._next
            self._tail._next = element
            self._tail = element
        self._size += 1

    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail._next

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next

        self._size -= 1
        return oldhead

    def first(self):
        if self.is_empty():
            raise IndexError("Queue Empty")
        head = self._tail._next
        return head._element

