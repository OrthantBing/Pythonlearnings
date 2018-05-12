class TrieNode(object):
    __slots__ = 'element','word_finished','children','counter'

    def __init__(self, element):
        self.element = element
        self.word_finished = False
        self.children = []
        self.counter = 0

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

    def find_suggestion(self, root, string):
        node = root
        string_exists = True
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    child.counter += 1
                    child_found = True
                    node = child
                    break
            
            if not child_found:
                string_exists = False
        
        if not string_exists:
            return "No suggestions"

        else:
            strings_array = []
            if node.word_finished:
                strings_array.append(string)
            self.compile_strings(node, strings_array, string)
            return "\n".join(strings_array)

    def compile_strings(self, node, array, string):
        for child in node.children:
            if child.word_finished:
                array.append(string + child.element)
            self.compile_strings(child, array, string + child.element)

if __name__ == '__main__':
    n = int(raw_input().strip())
    root = TrieNode("*")
    for _ in xrange(n):
        text = raw_input().strip().lower()
        root.add(root, text)

    m = int(raw_input().strip())
    for _ in xrange(m):
        text = raw_input().strip().lower()
        print root.find_suggestion(root, text)

