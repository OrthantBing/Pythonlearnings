

class Vector:
    """Represents a vector in multidimensional space"""
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self): # non-operator overload
        """Return the dimension of the vector"""
        return len(self._coords)

        """return jth coordinate of vector"""

    def __getitem__(self, j): # non-operator overload (overloads the [])
        return self._coords[j]

    def __setitem__(self, j, val): # non-operator overload (overloads the [])
        self.__coords[j] = val

    def __add__(self, other): #operator overload (overloads the + operator)
        if len(self) != len(other)
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other): #overloads the == operator
        return self._coords == other._coords

    def __ne__(self, other): #overloads the != operator
        return not self == other

    def str (self): # non-operator overload.
        """Produce string representation of vector."""
        return   <   + str(self. coords)[1:−1] +   >

if __name__ == '__main__':
    v = Vector(5) # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
    v[−1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
    print(v[4]) # print 45 (via getitem )
    u=v+v #<0,46,0,0,90>(via add )
    print(u) # print <0, 46, 0, 0, 90>
    total = 0 
    for entry in v: # implicit iteration via __len__ and __getitem__
        total += entry

