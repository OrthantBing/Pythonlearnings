from collections import deque

class TrieNode(object):
    __slots__ = 'element', 'counter', 'word_finished', 'children'

    def __init__(self, element):
        self.element = element
        self.counter = 0
        self.children = []
        self.word_finished = False

    def add(self, root, string):
        node = root
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    child_found = True
                    child.counter += 1
                    node = child
                    break

            if not child_found:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node

        node.word_finished = True

    def find_suggestion_count(self, root, string):
        node = root
        string_exists = True
        for char in string:
            child_found = False
            for child in node.children:
                if child.element == char:
                    child_found = True
                    node = child
                    break
            
            if not child_found:
                string_exists = False
                break

        if not string_exists:
            return 0

        else:
            return node.counter + 1

    def getNodeCount(self, root):
        if root is None:
            return 0
        
        
        queue = deque()
        queue.append(root)

        count = 1
        while len(queue) > 0:
            node = queue.popleft()

            for child in node.children:
                queue.append(child)
                count += 1

        return count # The root node


if __name__ == '__main__':
    n = int(raw_input().strip())
    root = TrieNode("*")
    # root.add(root, "hackerrank")
    # root.add(root, "hackerearth")

    # root.add(root, "hackerasdf")
    # print root.find_suggestion_count(root, "h")

    # for _ in xrange(n):
    #     subroutine, string = raw_input().split()
    #     if subroutine == 'add':
    #         root.add(root, string)
    #     elif subroutine == 'find':
    #         print root.find_suggestion_count(root, string)
    #     else:
    #         print "WTF"

    for _ in xrange(n):
        string = raw_input()
        root.add(root, string)

    print root.getNodeCount(root)



            

