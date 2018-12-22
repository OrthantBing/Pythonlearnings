#https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/tree-counting-3/

class Tree(object):
    class Node:
        __slots__ = '_element', '_parent', '_children', '_value'

        def __init__(self, e, value, parent=None):
            self._element = e
            self._value = value
            self._parent = parent
            self._children = []

        def __str__(self):
            print("element: {}, value: {}".format(self._element, self._value))

    def __init__(self):
        self._root = None
        self.nodehash = {}


    def addNodes(self, nodes, relationship):
        for i, node_value in enumerate(nodes):
            node_element = i + 1
            node = self.Node(node_element, node_value)
            self.nodehash[node_element] = node
            if node_element == 1:
                self._root = node
                

        for j, element in enumerate(relationship):
            node_element = j + 1
            parent = self.nodehash[element]
            child = self.nodehash[node_element + 1]
            parent._children.append(child)
            child._parent = parent

    def children_level(self):
        arr = [self._root]
        level = 1
        level_hash = {1 : arr}
        children_hash = {}

        while len(arr) > 0:
            level += 1
            temp = []
            for i in arr:
                for j in i._children:
                    temp.append(j)

            if len(temp) == 0: 
                break

            for i in range(1, level):
                #level_hash[i] = level_hash[i+1] + temp
                if i not in children_hash:
                    children_hash[i] = []

                children_hash[i] = children_hash[i] + temp 

            level_hash[level] = temp
            arr = temp

        return level_hash, children_hash

    def find_triplets(self, childrenhash, kvalue):
        triplets = []
        for key, value in childrenhash.items():
            i = self.nodehash[key]
            for j in value:
                for k in value:
                    if j != k:
                        checkvalue = i._value + j._value + k._value
                        if checkvalue >= kvalue:
                            toappend = set([i._value,j._value,k._value])
                            if toappend not in triplets:
                                triplets.append(toappend)
                            # triplets.append((i._value,j._value,k._value))

        return len(triplets)

    
    

if __name__ == '__main__':
    n, k = map(int, input().split())
    treeval = map(int, input().split())
    node_relationship = map(int, input().split())
    tree = Tree()
    tree.addNodes(treeval, node_relationship)
    val, children = tree.children_level()

    # for key, value in children.items():
    #     print(key)
    #     print([i._element for i in value])

    print(tree.find_triplets(children, k))
    


    
