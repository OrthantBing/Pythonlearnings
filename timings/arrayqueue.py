class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._A = [None] * DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def enqueue(self, obj):
        pass

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        if self.is_empty():
            return IndexError("Queue empty")

        returnvalue = self._A[self._front]
        self._A[self._front] = None
        self._front = (self._front + 1) % len(self._A)
        self._size -= 1
        return returvalue

    def enqueue(self):
        if self._size == len(self._A):
            self._resize(2 * len(self._A))

        avail = (self._front + self._size) % len(self._A)
        self._A[avail] = e
        self._size += 1

    def resize(self, c):
        old = self._data

        self._data = [None] * c
        walk = self._front

        for k in range(self._size):
            self._A[k] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0
        

    
