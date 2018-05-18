#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/ma5termind-and-xor-minimization/
import math
import sys
MAX_LEN_INT = len(bin(sys.maxint)[2:])

def NumStringToBinString(string):
    num = int(string)
    return bin(num)[2:].zfill(MAX_LEN_INT)

def BinStringToNumString(string):
    return int(string, 2)


def subsequence(array, binary, len):
    return_array = []
    returnval = 0
    for i in xrange(len):
        if (binary & (1 << i)):
            return_array.append(array[i])
            returnval += array[i]
    return returnval

def generate_subsequence(array):
    n = len(array)
    limit = int(math.pow(2, n))
    sub_sequence = []
    for i in xrange(1, limit):
        string = subsequence(array, i, n)  
        sub_sequence.append(string)
    
    return sub_sequence

class TrieNode(object):
    __slots__ = 'element', 'word_counter', 'zero', 'one', 'word_finished', 'counter', 'value'

    def __init__(self, element, value = None):
        self.element = element
        self.value = value
        self.word_finished = False
        self.word_counter = 0
        self.counter = 0
        self.zero = None
        self.one = None
        self.value = value
        
    def add(self, root, string, arrindex):
        node = root
        for index, char in enumerate(string):
            if char == '1':
                if node.one is not None:
                    node = node.one
                    node.counter += 1

                else:
                    new_node = TrieNode(char)
                    new_node.value = string[:index + 1]
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
                print "Something terrible happened"
                exit()

        node.word_finished = True
        node.word_counter += 1
    
    def query_min(self, root, string):
        node = root

        for char in string:
            if char == '1':
                if node.one is not None:
                    node = node.one
                else:
                    node = node.zero
            elif char == '0':
                if node.zero is not None:
                    node = node.zero
                else:
                    node = node.one
            else:
                print "Soethign terrible in query"
                exit()

        return str(BinStringToNumString(node.value)), str(node.word_counter)


if __name__ == '__main__':
    n = int(raw_input())
    input_array = map(int, raw_input().split())
    subsequencearray = generate_subsequence(input_array)

    root = TrieNode("*")
    for j in subsequencearray:
        root.add(root, NumStringToBinString(str(j)), j)
    
    query = int(raw_input())
    for _ in xrange(query):
        x = raw_input().strip()
        #print root.query_min(root, NumStringToBinString(str(x)))
        print " ".join(root.query_min(root, NumStringToBinString(str(x))))