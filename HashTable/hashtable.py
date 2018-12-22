class MapBase():
    class _Item:
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __eq__(self, other):
            return self._key == other._key
        def __ne__(self, other):
            return not (self == other)
        def __lt__(self, other):
            return self._key < other._key

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""
    def __init__(self, cap=11, p=109345121):
        """create an empty hash-table map"""
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
    
    def _hash_function(self, k):
        return (hash(k) self. scale + self. shift) % self. prime % len(self. table)

    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self,k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)   #subroutine maintains self._n
        if self._n > len(self._table) // 2: #keep load factor <=0.5
            self._resize(2*len(self._table) - 1) # this number is usually prime.

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c): # resize bucket array to capacity c
        old = list(self.items()) # record existing items
        self._table = c * [None] # reset table to desired capacity
        self._n = 0        # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v     # reinsert old key-value pair



class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k): 
        bucket = self. table[j]
        if bucket is None:
            raise KeyError( Key Error:   + repr(k)) 
        return bucket[k]
    
    def _bucket_setitem(self, j, k, v): 
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap() # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:   # key was new to the table
            self._n += 1                    # increase the map size.

    def _bucket_delitem(self, j, k): 
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( Key Error:   + repr(k))
         del bucket[k]

    def __iter__ (self):
        for bucket in self._table:
            if bucket is not None:  # non empty slot
                for key in bucket:
                    yield key