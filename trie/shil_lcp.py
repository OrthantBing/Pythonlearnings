# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/shil-and-lcp-pairsmonk/
from collections import deque

class TrieNode(object):
    __slots__ = 'element', 'counter', 'word_finished', 'children'

    def __init__(self, element):
        self.element = element
        self.counter = 1
        self.children = []
        self.word_finished = False

    def add(self, root, string):
        node = root
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    child.counter += 1
                    child_found = True
                    node = child
                    break
            
            if not child_found:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.word_finished = True

    def calcualte_val(self, array):
        sum = 0
        i = 0
        while i < len(array):
            j = i+1
            while j < len(array):
                sum = array[i] * array[j]
                j += 1

            i += 1
        return sum
        
    def find(self, root):
        node = root
        counter = 0
        array = []
        testarray = []
        for child in node.children:
            if child.element == node.element:
                array.append(1)
            else:
                array.append(child.counter)
                testarray.append(child.element)
        
        print testarray
        print array
        val = self.calcualte_val(array)
        return val
           
    def generate_array(self, root):
        node = root
        queue = deque()
        queue.append(node)
        array = []

        while len(queue) > 0:
            node = queue.popleft()
            array.append(self.find(node))

            for child in node.children:
                queue.append(child)

        return array    
            
if __name__ == '__main__':
    n = int(raw_input().strip())
    root = TrieNode("*")
    for _ in xrange(n):
        s = raw_input()
        root.add(root, s)
    
    print root.generate_array(root)

