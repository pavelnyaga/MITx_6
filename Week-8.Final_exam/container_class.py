class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        counter = 0
        
        for v in self.vals.keys():
            if v == e:
                counter += self.vals[e]
            
        return counter
    
    def __add__(self, other):
        
        res = Bag()
        
        for v in self.vals.keys():
            if v in other.vals.keys():
                for i in range(self.vals[v] + other.vals[v]):
                    res.insert(v)
            else:
                for i in range(self.vals[v]):
                    res.insert(v)
                
        for v in other.vals.keys():
            if v not in res.vals.keys():
                for i in range(other.vals[v]):
                    res.insert(v)
        
        return res

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            self.vals.pop(e)
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals:
            return True
        else:
            return False

d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)

d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))