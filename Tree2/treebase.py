class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by the subclass')
        
        def __eq__(self, o):
            raise NotImplementedError('must be implemented by the subclass')
        
        def __ne__(self, o):
            raise NotImplementedError('must be implemented by the subclass')
    
    def root(self):
        raise NotImplementedError('must be implemented by the subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by the subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by the subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by the subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by the subclass')
    
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if p == self.root():
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p=None):
        if p == None:
            p = self.root()
        
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))
        


    