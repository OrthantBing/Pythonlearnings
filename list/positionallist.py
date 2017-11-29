from linkedlistbase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)
    


    def _validate(self, p):
        if p is not isinstance(self.Position):
            raise TypeError("p must be of proper position type")

        if p._container is not self:
            raise ValueError("p does not belong to this class")

        if p._node._next is None:
            raise ValueError("p is no longer valid")
        
        return p._node

    def _make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        else: 
            return self.Position(node)

    def first(self):
        return self._make_position(self.head())

    def last(self):
        return self._make_position(self.tail())

    def before(self, p):
        node_at_p = self._validate(p)
        return self._make_position(node_at_p._prev)

    def after(self, p):
        node_at_p = self._validate(p)
        return self._make_position(node_at_p._next)

    def iter(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor._element
            cursor = self.after(cursor)

    
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self.header, self.header._next)
        
    def add_last(self, e):
        return self._insert_between(e, self.trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        return self._delete_node(self._validate(p))

    def replace(self, p, e):
        node = self._validate(p)
        node._element = e
        return self._make_position(node)

    @staticmethod
    def insertion_sort(L):
        if len(L) > 1:
            marker = L.first()
            while marker != L.last():
                pivot = L.after(marker)
                value = pivot.element()
                if marker.element() < value:
                    marker = pivot
                else:
                    walk = marker
                    while walk != L.first() and L.before(walk).element() > value:
                        marker = L.before(walk)
                        
                    L.delete(pivot)
                    L.add_before(walk, value)


