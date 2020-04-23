class Set:
    def __init__(self, value=[]):  # Constructor
        self.data = []  # Manages a list
        self.concat(value)

    def issubset(self, other):
        res = []
        for x in self.data:
            if x in other.data:
                res.append(x)
        a, b = (len(self.data), len(other.data))
        #print(type(other))
        if res == self.data and a==b: return print("self <= other")
        elif res == self.data and a<b: return print("self < other")
        else: return print("Error: Test case is Not in subset")

    def issuperset(self, other):
        res = []
        for x in other.data:
            if x in self.data:
                res.append(x)
        a,b = (len(self.data), len(other.data))
        other_list = list(other.data)
        if res == other_list and a == b: return print("self >= other")
        elif res == other_list and a>b: return print("self > other")
        else: return print("Error: Test case is Not in superset")

    def IOR(self, other):
        a,b = (list(self.data), list(other.data))
        com_list = a + b
        combine_list = []
        for x in com_list:
            if not x in combine_list:  # Removes duplicates
                combine_list.append(x)
        self.data = combine_list
        print(Set(self.data))
        #return Set(self.data)

    def intersection_update(self, other):
        #self.data = []
        replace = []
        for x in self.data:
            if x in other.data:  # Pick common items
                replace.append(x)
        self.data = replace
        print(Set(self.data))
        #return Set(self.data)  # Return a new Set

    def difference_update(self, other):
        res = []  # self is the subject
        for x in self.data:
            if not x in other.data:
                res.append(x)
        self.data = res
        print(Set(self.data))
        #return Set(self.data)

    def symmetric_difference_update(self, other):
        res = []  # self is the subject
        for x in self.data:
            if x in other.data:  # Pick common items
                res.append(x)
        a, b = (list(self.data), list(other.data))
        com_list = a + b
        combine_list = []
        for x in com_list:
            if not x in combine_list:  # Removes duplicates
                combine_list.append(x)
        answer = []
        for y in combine_list:
            if not y in res:
                answer.append(y)
        self.data = answer
        print(Set(self.data))
        #return Set(self.data)

    def add(self, elem = []):
        Return_Set= self.data + elem
        Return_list = []
        for x in Return_Set:
            if not x in Return_list:  # Removes duplicates
                Return_list.append(x)
        self.data = Return_list
        return Set(self.data)

    def remove(self, elem):
        pos=0
        if not elem in  self.data:
            raise KeyError('{0} is not element in self.data'.format(elem))
        for i in self.data:
            if i == elem:
               pos = self.data.index(i)
        del self.data[pos]
        return Set(self.data)

    def intersection(self, other):  # other is any sequence
        res = []  # self is the subject
        for x in self.data:
            if x in other.data:  # Pick common items
                res.append(x)
        return Set(res)  # Return a new Set

    def union(self, other):  # other is any sequence
        res = self.data[:]  # Copy of my list
        for x in other:  # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:  # Removes duplicates
                self.data.append(x)

    def __len__(self):
        return len(self.data)  # len(self)
    def __getitem__(self, key):
        return self.data[key]  # self[i], self[i:j]
    def __and__(self, other):
        return self.intersection(other)  # self & other
    def __or__(self, other):
        return self.union(other)  # self | other
    def __repr__(self):
        return 'Set({})'.format(repr(self.data))
    def __iter__(self):
        return iter(self.data)  # for x in self:

print("=====Test self <= other=====")
x,y = (Set([1,2,2,3]), Set([2,3,1]))
x.issubset(y)

print("=====Test self < other=====")
x,y = (Set([1,2]), Set([1,2,3]))
x.issubset(y)

print("=====Test self >= other=====")
x,y = (Set([1,2,3]), Set([1,2,3,3,3]))
x.issuperset(y)

print("=====Test self > other=====")
x,y = (Set([1,2,3]), Set([2]))
x.issuperset(y)

print("=====Test self |= other======")
x,y = (Set([1,2,2,3]), Set([3,4,5,6]))
x.IOR(y)

print("=====Test self &= other=====")
x,y = (Set([1,2,2,3,4]), Set([3,4,5,6]))
x.intersection_update(y)

print("=====Test self _= other======")
x,y = (Set([1,2,3,4]), Set([3,4,5,6]))
x.difference_update(y)

print("=====Test self ^= other======")
x,y = (Set([1,2,3,4]), Set([3,4,5,6]))
x.symmetric_difference_update(y)

print("=====Add element elem to the set======")
x = Set([1,2,3,4,7,10])
print(x.add([7,8,9]))

print("======Remove element elem from the set======")
x = Set([1,2,3,4,7,10])
print(x.remove(1))
#print(x, y, len(x))
#print(x.intersection(y), y.union(x))
#print(x & y, x | y)
#print(x[2], y[:2])
#for element in x:
    #print(element, end=' ')
#print()
#print(3 not in y)  # membership test
#print(list(x))  # convert to list because x is iterable
