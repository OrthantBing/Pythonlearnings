class Node:
    def __init__(self):
        self._array = [None] * 26
        self._isLeaf = False

    def children(self):
        return filter(lambda x: x, self._array)

class Trie:
    def __init__(self):
        self.root = getNode()

    def getNode(self):
        return Node()

    def _chartoindex(c):
        return ord(c) - ord('a')

    def insert(self, key):
        crawlNode = self.root
        for i in range(len(key)):
            index = self._chartoindex(key[i])
            if not crawlNode.array[index]:
                newNode = self.getNode()
                crawlNode.array[index] = newNode
                crawlNode = newNode
            else:
                crawlNode = self._chartoindex[i]
                
        crawlNode._isLeaf = True

    def search(self, key):
        crawlNode = self.root
        for i in range(len(key)):
            index = self._chartoindex[key[i]]
            if not crawlNode.array[index]:
                return False
            else:
                crawlNode = crawlNode.array[index]

        return crawlNode != None and crawlNode._isLeaf
    
if __name__ == '__main__':
    node = Node()
    print(node)
    node.