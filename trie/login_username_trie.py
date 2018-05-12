# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/registration-system/

class TrieNode(object):
    __slots__ = 'element','word_finished','children','value','counter','number'

    def __init__(self, element, value=None):
        self.element = element
        self.counter = 0
        self.word_finished = False
        self.children  = []
        self.value = value
    
    def add(self, root, string, value=None):
        node = root
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    child.counter += 1
                    node = child
                    child_found = True

            if not child_found:
                new_node = TrieNode(char)
                new_node.value = value
                node.children.append(new_node)
                node = new_node
        
        node.word_finished = True

    def find_next(self, root, string):
        node = root
        string_exists = True
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    node = child
                    child_found = True
                    break
                else:
                    child_found = False
            
            if not child_found:
                string_exists = False


        if not string_exists:
            self.add(root, string)
            return string

        else:
            if not node.word_finished:
                node.word_finished = True
                return string
            
            else:
                i = 0
                while True:
                    exists, _ = self.string_exists_in_child(node, str(i))
                    if exists:
                        i += 1
                    else:
                        self.add(root, string + str(i))
                        return string + str(i)


    def char_exists_in_child(self, node, char):
        for child in node.children:
            if child.element == char:
                return True, child

        return False, None

    def string_exists_in_child(self, incomingnode, string):
        node = incomingnode
        string_exists = True
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    node = child
                    child_found = True
                    break
                else:
                    child_found = False
            
            if not child_found:
                string_exists = False
        
        return string_exists, node

if __name__ == '__main__':
    n = int(raw_input().strip())

    root = TrieNode("*")
    for i in xrange(n):
        text = raw_input().strip()
        print root.find_next(root, text)

        


