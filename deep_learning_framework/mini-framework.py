import numpy as np

class Tensor(object):
    def __init__(self,data, creators=None, creation_op=None):
        self.data = np.array(data)
        self.creation_op = creation_op
        self.creators = creators
        self.grad = None
        
    def backward(self,grad):
        self.grad = grad
        if self.creation_op == "add":
            self.creators[0].backward(grad)
            self.creators[1].backward(grad)
                
        
    def __add__(self, other):
        return Tensor(self.data + other.data,
                creators = [self, other],
                creation_op = "add")
    
    # a printable representation of the given object
    def __repr__(self):
        return str(self.data.__repr__())
    
    # a string representation of a class
    def __str__(self):
        return str(self.data.__str__())
        
x = Tensor([1,2,3,4,5])
y = Tensor([2,2,2,2,2])

#print(x)
#y = x+x
#print(y)

print(x.grad) # None
print(y.grad) # None

z = x + y
# autograd (автоматичне обчислення градієнта)
z.backward(Tensor(np.array([1,1,1,1,1])))

print(x.grad) # [1,1,1,1,1]
print(y.grad) # [1,1,1,1,1]
print(z.data) # [1,2,3,4,5] + [2,2,2,2,2] = [3,4,5,6,7]
print(z.creators) # [array([1,2,3,4,5]), array([2,2,2,2,2])] 
print(z.creation_op) # add
        