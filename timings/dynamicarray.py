import ctypes
import math

class DynamicArray: 
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def popat(self, k):
        returnval = self._A[k]
        for j in range(k, self._n - 1):
            print self._A[j]
            self._A[j] = self._A[j+1]
        self._n -= 1
        cap = int(math.ceil(float(self._capacity) / 2))
        if self._n == cap:
            self._resize(cap)
        
    def pop(self):
        returnval = self._A[self._n - 1]
        self._n -= 1
        cap = int(math.ceil(float(self._capacity) / 2))
        if self._n == cap:
            self._resize(cap)

        return returnval

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]

        self._A = B
        self._capacity = c
        return

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        else:
            return self._A[index]

    
    def __str__(self):
        return " ".join(map(str, [self._A[i] for i in range(self._n)]))

