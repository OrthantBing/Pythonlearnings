class TrieNode(object):
    __slots__ = 'element','word_finished','children', 'value', 'counter'

    def __init__(self, element, value=None):
        self.element = element
        self.word_finished = False
        self.children = []
        self.value = value
        self.counter = 0

    def add(self, root, string, value=None):
        node = root
        
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    child.counter += 1
                    node = child
                    child_found = True

                    # This indicates that there is
                    # some bigger child value
                    if child.value < value:
                        child.value = value
                    break
                
            if not child_found:
                new_node = TrieNode(char)
                new_node.value = value
                node.children.append(new_node)
                node = new_node
        
        node.word_finished = True
        #node.value = value

    def find_prefix(self, root, string):
        node = root
        
        for char in string:
            
            child_found = False
            for child in node.children:
                
                if child.element == char:
                    node = child
                    child_found = True
                    break
            if not child_found:
                return -1

        
        return node.value

        

if __name__ == '__main__':
    n,q= [int(i) for i in raw_input().split()]
    root = TrieNode("*", -1)
    for i in xrange(n):
        text, value = raw_input().split()
        root.add(root, text.strip(), int(value))

    for j in xrange(q):
        text = raw_input().strip()
        print root.find_prefix(root, text)



        