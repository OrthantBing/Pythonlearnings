from binarytree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, e, parent=None, left=None, right= None):
            self._element = e
            self._parent = parent
            self._left = left
            self._right = right

        
    class Position(BinaryTree.Position):
        __slots__ = '_element', '_container'
        def __init__(self, container, element):
            self._container = container
            self._element = element

        def element(self):
            return self._element._element

        def __eq__(self, other):
            if type(other) is type(self) and other._element == self._element:
                return True

        def __ne__(self, other):
            return self is not other

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p should be of correct instance")

        if p._container is not self:
            raise ValueError("P does not belong to this container")

        if p._element._parent is p._element:
            raise ValueError("Node deleted")

        return p._element

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._size = 0
        self._root = None

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def left(self, p):
        return self._make_position(p._element._left)

    def right(self, p):
        return self._make_position(p._element._right)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p=None):
        if p is None:
            return 0
        count = 0
        node = self._validate(p)
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Root is not empty")
        node = self._Node(e)
        self._root = node
        self._size += 1
        return self._make_position(node)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left is not empty to update")
        else:
            node._left = self._Node(e,node)
            self._size += 1
            return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Node is not empty to add")
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        if node is None:
            raise ValueError("Node is empty to replace")
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        if self.num_children() == 2:
            raise ValueError("Cant delete since node has more than one leaf")
        node = self._validate(p)
        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for deleteing or deprecating a node.
        return node._element # the element that was deleted.

        
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self._is_leaf(p):
            raise ValueError('position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('nodes must be of same type')
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            self._size += t1._size
            t1._size = None
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            self._size += t2._size
            t2._size = 0

    def __iter__(self):
        for p in self.positions():
            yield p

    def positions(self):
        return self.preorder(ordering='preorderlabelpath')

    def preorder(self, ordering='preorder'):
        if not self.is_empty():
            if ordering == 'preorder':
                for p in self._subtree_preorder(self.root()):
                    yield p
            elif ordering == 'inorder':
                for p in self._subtree_inorder(self.root()):
                    yield p
            elif ordering == 'postorder':
                for p in self._subtree_postorder(self.root()):
                    yield p
            elif ordering == 'preorderlabel':
                for p in self._subtree_preorder_label(self.root(),1):
                    yield p
            elif ordering == 'preorderlabelpath':
                self.preorder_label(self.root(),1, [])
            

    def _subtree_preorder(self, p):
        yield p.element()
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def _subtree_preorder_label(self, p, depth):
        printvalue = 2*depth*' ' + str(p.element())
        yield printvalue
        for c in self.children(p):
            for other in self._subtree_preorder_label(c,depth + 1):
                yield other

    def _subtree_preorder_label_path(self, p, depth, path):
        printval = 2*depth*' ' + '.'.join([str(i+1) for i in path]) + ' ' + str(p.element())
        yield printval
        path.append(0)
        for c in self.children(p):
            for other in self._subtree_preorder_label_path(c, depth+1, path):
                yield other
    
    def preorder_label(self, p, depth, path):
        path.append(0)
        printval = 2*depth*' ' + '.'.join([str(i+1) for i in path]) + ' ' + str(p.element())
        print(printval)
        
        for c in self.children(p):
            self.preorder_label(c, depth+1, path)
            path[-1] += 1
        path.pop()

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p.element()

    def breadfirstsearch(self, p):
        queue = []
        queue.append(p)
        while len(queue) > 0:
            current = queue.pop()
            yield current.element()
            if current.num_children > 0:
                for i in self.children(current):
                    queue.append(i)

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p.element()
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

