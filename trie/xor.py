import sys
MAX_LEN_INT = len(bin(sys.maxint)[2:])

def NumStringToBinString(string):
    num = int(string)
    return bin(num)[2:].zfill(MAX_LEN_INT)

def BinStringToNumString(string):
    return int(string, 2)

class TrieNode(object):
    __slots__ = 'element', 'value', 'index', 'counter', 'zero', 'one', 'word_finished'

    def __init__(self, element, value=None):
        self.element = element
        self.value = value
        self.word_finished = False
        self.counter = 0
        self.zero = None
        self.one = None
        self.index = None

    def add(self, root, string, arrindex):
        node = root

        for index, char in enumerate(string):
            if char == '1':
                if node.one is not None:
                    node = node.one
                    node.counter += 1

                    
                else:
                    new_node = TrieNode(char)
                    new_node.value = string[:index+1]
                    node.one = new_node
                    node = new_node
            elif char == '0':
                if node.zero is not None:
                    node = node.zero
                    node.counter += 1

                   
                else:
                    new_node = TrieNode(char)
                    new_node.value = string[:index + 1]
                    node.zero = new_node
                    node = new_node
            else:
                print "Something terribly wront happened"
                exit()
        
        node.word_finished = True
        node.index = arrindex

    def query(self, root, string):
        node = root

        for index, char in enumerate(string):
            if char == '1':
                if node.zero is not None:
                    node = node.zero
                else: 
                    node = node.one
            elif char == '0':
                if node.one is not None:
                    node = node.one
                else:
                    node = node.zero
            else:
                print "something terribly wrong"
                exit()
                
        return int(BinStringToNumString(string)) ^ int(BinStringToNumString(node.value)), node.index


    def xor_sub_array(self, root, array):
        ans = 0
        pre = 0

        initial = 0
        final = 0
        for i in xrange(len(array)):
            pre = pre ^ int(array[i])
            root.add(root, NumStringToBinString(str(pre)), i)
            s = NumStringToBinString(str(pre))
            print "String" + s

            uptonow, index = root.query(root, s)

            if ans < uptonow:
                initial = index
                ans = uptonow
                final = i
        
        print "Max xor subarray:  " + str(ans)
        print "initial: " + str(initial) 
        print "Final: " + str(final)

if __name__ == "__main__":

    string_arr = raw_input().split()
    root = TrieNode('*')

    root.xor_sub_array(root, string_arr)


import sys
MAX_LEN_INT = len(bin(sys.maxint)[2:])

def NumStringToBinString(string):
    num = int(string)
    return bin(num)[2:].zfill(MAX_LEN_INT)

def BinStringToNumString(string):
    return int(string, 2)

class TrieNode(object):
    __slots__ = 'element', 'value', 'index', 'counter', 'zero', 'one', 'word_finished'

    def __init__(self, element, value=None):
        self.element = element
        self.value = value
        self.word_finished = False
        self.counter = 0
        self.zero = None
        self.one = None
        self.index = None

    def add(self, root, string, arrindex):
        node = root

        for index, char in enumerate(string):
            if char == '1':
                if node.one is not None:
                    node = node.one
                    node.counter += 1

                    
                else:
                    new_node = TrieNode(char)
                    new_node.value = string[:index+1]
                    node.one = new_node
                    node = new_node
            elif char == '0':
                if node.zero is not None:
                    node = node.zero
                    node.counter += 1

                   
                else:
                    new_node = TrieNode(char)
                    new_node.value = string[:index + 1]
                    node.zero = new_node
                    node = new_node
            else:
                print "Something terribly wront happened"
                exit()
        
        node.word_finished = True
        node.index = arrindex

    def query(self, root, string):
        node = root

        for index, char in enumerate(string):
            if char == '1':
                if node.zero is not None:
                    node = node.zero
                else: 
                    node = node.one
            elif char == '0':
                if node.one is not None:
                    node = node.one
                else:
                    node = node.zero
            else:
                print "something terribly wrong"
                exit()
                
        return int(BinStringToNumString(string)) ^ int(BinStringToNumString(node.value)), node.index


    def xor_sub_array(self, root, array):
        ans = 0
        pre = 0

        initial = 0
        final = 0
        for i in xrange(len(array)):
            pre = pre ^ int(array[i])
            root.add(root, NumStringToBinString(str(pre)), i)
            s = NumStringToBinString(str(pre))
            print "String" + s

            uptonow, index = root.query(root, s)

            if ans < uptonow:
                initial = index
                ans = uptonow
                final = i
        
        print "Max xor subarray:  " + str(ans)
        print "initial: " + str(initial) 
        print "Final: " + str(final)

if __name__ == "__main__":

    string_arr = raw_input().split()
    root = TrieNode('*')

    root.xor_sub_array(root, string_arr)


