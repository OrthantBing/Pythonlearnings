from treebase import Tree

class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by the subclass')
    
    def right(self, p):
        raise NotImplementedError('must be implemented by the subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)

