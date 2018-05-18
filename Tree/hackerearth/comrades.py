from collections import deque
import math

class Tree(object):
    class Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, e, parent=None):
            self._element = e
            self._parent = parent
            self._children = []

    def __init__(self):
        self._root = self.Node(0)
        self.nodehash = {0: self._root}

    def special_add(self, node_element_array):
        for index, value in enumerate(node_element_array):
            soldier_element = index + 1
            soldier_parent_element = value
            soldier_parent_node = None
            soldier_element_node = None

            # We are now sure that we have soldier's parent element in the tree
            if soldier_parent_element in self.nodehash:
                soldier_parent_node = self.nodehash[soldier_parent_element]
            else:
                soldier_parent_node = self.Node(soldier_parent_element)
                self.nodehash[soldier_parent_element] = soldier_parent_node

            
            if soldier_element in self.nodehash:
                soldier_element_node = self.nodehash[soldier_element]
            else:
                soldier_element_node = self.Node(soldier_element)
                self.nodehash[soldier_element] = soldier_element_node

            soldier_element_node._parent = soldier_parent_node
            soldier_parent_node._children.append(soldier_element_node)



    def hand_and_fist(self):
        handshake = 0
        fistbump = 0
        queue = deque()
        queue.append(self._root)
        while len(queue) > 0:
            node = queue.popleft()
            for i in node._children:
                queue.append(i)
            
            fistbump_members = len(node._children)
            if fistbump_members > 1:
                fistbump += math.factorial(fistbump_members) / (math.factorial(fistbump_members - 2) * 2)

            handshake += len(node._children)
            #print [i._element for i in node._children]
        return handshake - 1, fistbump


    def comrades(self):
        arr = [self._root]
        returnval = []
        while len(arr) > 0:
            itr_arr = []
            returnval.append(len(arr))
            for node in arr:
                for i in node._children:
                    itr_arr.append(i)
            
            arr = itr_arr
        
        
        handshake = 0
        for index, val in enumerate(returnval[1:]):
            handshake += val*index
        return handshake

    def printKDistant(self, root, k, arr):
        if root is None:
            return
        if k == 0:
            arr.append(root._element)
        else:
            for i in root._children:
                self.printKDistant(i, k-1, arr)

    def shake(self):
        senior = 0
        handshake = 0
        fistbump = 0

        i = 1
        while True:
            arr = []
            self.printKDistant(self._root, i, arr)
            print i
            print arr
            if len(arr) > 1:
                fistbump += math.factorial(len(arr)) / (math.factorial(len(arr) - 2) * 2)

            if len(arr) == 0:
                break
            
            i += 1

            handshake += senior * len(arr)
            senior += len(arr)

        print handshake, fistbump

if __name__ == '__main__':
    cases = int(raw_input())
    for _ in xrange(cases):
        tree = Tree()
        case_count = int(raw_input())
        case = map(int, raw_input().split())
        tree.special_add(case)
        #print " ".join(map(str, tree.hand_and_fist()))
        # arr = []
        # tree.printKDistant(tree._root, 0, arr)
        # print arr
        # tree.shake()
        handshake = tree.comrades()
        fistbump = (case_count * (case_count - 1) / 2) - handshake
        print " ".join([str(handshake), str(fistbump)])
        
           
