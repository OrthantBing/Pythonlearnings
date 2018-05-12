class TrieNode(object):

    class Node(object):
        def __init__(self, element):
            self.element = element
            self.word_finished = False
            self.counter = 0
            self.children = {}

        def __hash__(self):
            return hash(self)

    def __init__(self):
        rootnode = Node("*")
        self.trie = rootnode
        return rootnode

    def add_string(self, root, string):


        