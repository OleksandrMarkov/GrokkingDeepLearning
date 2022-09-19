import numpy as np

class Tensor(object):
    def __init__(self,data):
        self.data = np.array(data)
    
    def __add__(self, other):
        return Tensor(self.data + other.data)
    
    # a printable representation of the given object
    def __repr__(self):
        return str(self.data.__repr__())
    
    # a string representation of a class
    def __str__(self):
        return str(self.data.__str__())
        
x = Tensor([1,2,3,4,5])
print(x)

y = x+x
print(y)        