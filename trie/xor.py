#https://www.hackerearth.com/practice/notes/lalitkundu95/tutorial-on-trie-and-example-problems/
import sys
MAX_INT_LEN = len(bin(sys.maxint)[2:])

def NumStringToBinString(string):
    num = int(string)
    return bin(num)[2:].zfill(MAX_INT_LEN)

def BinStringToNumString(string):
    return int(string, 2)



class TrieNode(object):
    __slots__ = 'element','value','word_finished','zero', 'one','counter'

    def __init__(self, element, value=None):
        self.element = element
        self.value = value
        self.word_finished = False
        self.counter = 0
        # self.children = []
        self.zero = None
        self.one = None

    def add(self, root, string):
        node = root
        for index, char in enumerate(string):
            child_found = False
            
            if node.zero is not None: 
                if node.zero.element == char:
                    node.zero.counter += 1
                    node = node.zero
                    child_found = True
            elif node.one is not None:
                if node.one.element == char:
                    node.one.counter += 1
                    node = node.one
                    child_found = True
            
            # for child in node.children:
            #     if child.element == char:
            #         child.counter += 1
            #         node = child
            #         child_found = true

            if not child_found:
                new_node = TrieNode(char)
                new_node.value = string[:index+1]
                # node.children.append(new_node)
                if char == '1':
                    node.one = new_node
                else:
                    node.zero = new_node

                node = new_node

        node.word_finished = True


    def query(self, root, string):
        node = root
        finalstring = ''
        for char in string:
            if char == '1':
                if node.zero is not None:
                    finalstring += node.zero.element
                    node = node.zero
                elif node.one is not None:
                    finalstring += node.one.element
                    node = node.one
                else:
                    print "Something terribly wrong"
                    exit()
            else:
                if node.one is not None:
                    finalstring += node.one.element
                    node = node.one
                elif node.zero is not None:
                    finalstring += node.zero.element
                    node = node.zero
                else:
                    print "Something terribly wrong"
                    exit()
        return finalstring


    def max_xor_subarray(self, root, array):
        ans = 0
        pre = 0
        # root.add(root, "0")
        for i in xrange(len(array)):
            pre = pre ^ int(array[i])
            root.add(root, NumStringToBinString(str(pre)))
            s = NumStringToBinString(str(pre))
            ans = max(ans, int(BinStringToNumString(root.query(root, s))))
            
        print ans


if __name__ == "__main__":
    string_arr = raw_input().split()
    
    root = TrieNode("*")
    root.max_xor_subarray(root, string_arr)
    # for string in string_arr:
    #     root.add(root,NumStringToBinString(string))

    # inputcount = int(raw_input())

    # for _ in xrange(inputcount):
    #     s = NumStringToBinString(raw_input().strip())
    #     print BinStringToNumString(root.query(root, s))


     