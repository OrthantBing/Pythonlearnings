class Tree(object):
    class Node:
        __slots__ = '_element', '_parent', '_children', '_color'

        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []
            self._color = None

    def __init__(self):
        self._root = None
        self.nodehash = {}

    def add(self, node_element_array):
        for index, value in enumerate(node_element_array):
            child_node_element = index+2
            child_node = None 
            
            if child_node_element in self.nodehash:
                child_node = self.nodehash[child_node_element]
            else:
                child_node = self.Node(child_node_element)
                self.nodehash[child_node_element] = child_node

            parent_node_element = value
            parent_node = None
            
            if parent_node_element in self.nodehash:
                parent_node = self.nodehash[parent_node_element]
            else:
                parent_node = self.Node(parent_node_element)
                self.nodehash[parent_node_element] = parent_node

            child_node._parent = parent_node
            parent_node._children.append(child_node)


    def setRoot(self):
        for key, value in self.nodehash:
            if value._parent is None:
                self._root = value
                break
        print "There is something terribly wrong"

    def attachColor(self, array):
        for index, value in enumerate(array):
            self.nodehash[index+1]._color = value

    def findSimilarColor(self):
        counterarray = []
        for i in xrange(len(self.nodehash)):
            element = i+1
            node = self.nodehash[element]
            colortocheck = node._color
            counter = 0
            node_found = False

            while node._parent is not None:
                parent = node._parent
                counter += 1
                if colortocheck == parent._color:
                    node = parent
                    node_found = True
                    break
                else:
                    node = parent

            if node_found:
                counterarray.append(node._element)
            else:
                counterarray.append(-1)
        
        return counterarray

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    #  n nodes
    #  m colors

    array = map(int, raw_input().split())
    tree = Tree()
    tree.add(array)
    # Not necessary since we are using the hash and parent to traverse
    #tree.setRoot()

    colorarray = map(int, raw_input().split())
    tree.attachColor(colorarray)

    print " ".join(map(str, tree.findSimilarColor()))   

