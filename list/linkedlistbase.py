class _DoublyLinkedBase:
    class Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, e, prev, next):
            self._element = e
            self._prev = prev
            self._next = next

    def __init__(self):
        prev_sentinel = self.Node(None, None, None)
        next_sentinel = self.Node(None, None, None)
        self.header = next_sentinel
        self.trailer = prev_sentinel
        self.header._next = self.trailer
        self.trailer._prev = self.header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, p, n):
        node = self.Node(e, p, n)
        p._next = node
        n._prev = node
        self._size += 1
        return node

    def head(self):
        return self.header._next

    def tail(self):
        return self.trailer._next

    def _delete_node(self, node):
        prev_node = node._prev
        next_node = node._next
        element = node._element
        prev_node._next = next_node
        next_node._prev = prev_node
        node._prev = node._next = node._element = None
        self._size -= 1
        return element




        