class Student(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Name: %s, Age: %s" % (self.name,self.age)

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age


class XII(object):
    def __init__(self):
        self.members = []
        self.count = 0

    def Insert(self, obj):
        if type(obj) is Student:
            self.members.append(obj)
            self.count += 1
        else:
            raise "Incompatible Object: %s" % type(obj)

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def sort(self):
        self.members = sorted(self.members)

    def __repr__(self):
        return "\n".join(map(str,self.members))

if __name__ == '__main__':
    o = XII()
    o.Insert(Student(name="test", age=13))
    o.Insert(Student(name="zage", age=10))
    o.Insert(Student(name="king", age=18))

    print o

    o.sort()

    print o
