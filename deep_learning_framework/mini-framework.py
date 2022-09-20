import numpy as np

class Tensor(object):
    def __init__(self, data, autograd = False,
    creators = None, creation_op = None, id = None):
        self.data = np.array(data)
        self.creation_op = creation_op
        self.creators = creators
        self.grad = None
        self.autograd = autograd
        self.children = {}
        if id is None:
            self.id = np.random.randint(0, 100000)
        else:
            self.id = id
        
        # corretion the number of children
        if creators is not None:
            for c in creators:
                if self.id not in c.children:
                    c.children[self.id] = 1
                else:
                    c.children[self.id] += 1    
        
    # tensor gets grads from all children?    
    def all_children_grads_accounted_for(self):
        for id, cnt in self.children.items():
            if cnt != 0:
                return False
        return True
        
    def backward(self, grad = None, grad_origin = None):
        if self.autograd:
            if grad_origin is not None:
                
                # backward is possible? if yes counter -= 1
                if self.children[grad_origin.id] == 0:
                    raise Exception("cannot backprop more than once")
                else:
                    self.children[grad_origin.id] -= 1
            
            # accumulation of grads from several children
            if self.grad is None:
                self.grad = grad
            else:
                self.grad += grad
            
            if self.creators is not None and ( self.all_children_grads_accounted_for()
            or grad_origin is None): 
                # backward process
                if self.creation_op == "add":    
                    self.creators[0].backward(self.grad, self)
                    self.creators[1].backward(self.grad, self)
                
                if self.creation_op == "neg":
                    self.creators[0].backward(self.grad.__neg__())
                    
    def __add__(self, other):
        if self.autograd == True and other.autograd == True:
            return Tensor(self.data + other.data,
                autograd = True,
                creators = [self, other],
                creation_op = "add")
        return Tensor(self.data + other.data)        
    
    # negation
    def __neg__(self):
        if self.autograd:
            return Tensor(self.data * (-1),
            autograd = True,
            creators = [self],
            creation_op = "neg")
        return Tensor(self.data * (-1))    
    
    # a printable representation of the given object
    def __repr__(self):
        return str(self.data.__repr__())
    
    # a string representation of a class
    def __str__(self):
        return str(self.data.__str__())

# intro
        
#x = Tensor([1,2,3,4,5])
#y = Tensor([2,2,2,2,2])

#print(x.grad) # None
#print(y.grad) # None
#print(x.creators) # None
#print(y.creators) # None

# autograd

#z = x + y
#z.backward(Tensor(np.array([1,1,1,1,1])))

#print(x.grad) # [1,1,1,1,1]
#print(y.grad) # [1,1,1,1,1]
#print(z.data) # [1,2,3,4,5] + [2,2,2,2,2] = [3,4,5,6,7]
#print(z.creators) # [array([1,2,3,4,5]), array([2,2,2,2,2])] 
#print(z.creation_op) # add

# support multiple tensors

a = Tensor([1,2,3,4,5], autograd = True)
b = Tensor([2,2,2,2,2], autograd = True)
c = Tensor([5,4,3,2,1], autograd = True)

d = a + (-b)
e = (-b) + c
f = d + e

f.backward(Tensor(np.array([1,1,1,1,1])))
print(b.grad.data == np.array([-2,-2,-2,-2,-2]))         