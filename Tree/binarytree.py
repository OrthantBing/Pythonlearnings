class BinaryTree:
    def __init__(self, obj):
        self.val = obj
        self.leftChild = None
        self.rightChild = None

    def addLeft(self, obj):
        if self.leftChild is None:
            self.leftChild = BinaryTree(obj)

        else:
            t = BinaryTree(obj)
            t.leftChild = self.leftChild
            self.leftChild = t
    def addRight(self, obj):
        if self.rightChild is None:
            self.rightChild = BinaryTree(obj)
        else: 
            t = BinaryTree(obj)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.val = obj

    def getRootVal(self):
        return self.val
