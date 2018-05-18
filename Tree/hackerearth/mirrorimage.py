class BinaryTree(object):
    class Node:
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, e, parent=None, left=None, right=None):
            self._element = e
            self._parent = parent
            self._left = left
            self._right = right
    
    def __init__(self):
        self._size = 0
        #self._root = None
        # Specifically for this question
        self._root = self.Node(1)
        self.nodehash = {1: self._root}

    def add(self, node_element, element, direction):
        parent_node = self.nodehash[node_element]
        nodetoadd = self.Node(element, parent_node)
        self.nodehash[element] = nodetoadd
        if direction == 'L':
            parent_node._left = nodetoadd
        elif direction == 'R':
            parent_node._right = nodetoadd
        else:
            print "WTF"
            exit()

    def findpath(self, element):
        node = self.nodehash[element]
        array = []
        while node._parent is not None:
            parent = node._parent
            if parent._left is not None:
                if parent._left._element == node._element:
                    array.append('L')
            if parent._right is not None:
                if parent._right._element == node._element:
                    array.append('R')
            node = parent

        return array

    def findmirrornode(self, array):
        node = self._root
        while len(array) > 0:
            direction = array.pop()
            if direction == 'L':
                if node._right is not None:
                    node = node._right
                else:
                    return -1
            elif direction == 'R':
                if node._left is not None:
                    node = node._left
                else:
                    return -1

        # Now we have exhausted all the array elements
        return node._element        


        
if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    tree = BinaryTree()

    for _ in xrange(n-1):
        node, element, direction = raw_input().split()
        tree.add(int(node), int(element), direction)
    
    for _ in xrange(m):
        e = int(raw_input())
        array = tree.findpath(e)
        print tree.findmirrornode(array)


        
        