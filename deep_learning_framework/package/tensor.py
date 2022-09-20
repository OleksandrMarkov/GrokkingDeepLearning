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
            if grad is None:
                grad = Tensor(np.ones_like(self.data))
            
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
                
                if self.creation_op == "sub":
                    new = Tensor(self.grad.data)
                    self.creators[0].backward(new, self)
                    new = Tensor(self.grad.__neg__().data)
                    self.creators[1].backward(new, self)    
                
                if self.creation_op == "mul":
                    new = self.grad * self.creators[1]
                    self.creators[0].backward(new, self)
                    new = self.grad * self.creators[0]
                    self.creators[1].backward(new, self)
                
                if self.creation_op == "mm":
                    act = self.creators[0] # layer of activation
                    weights = self.creators[1] # weight matrix
                    
                    # backpropagation
                    # layer_1_delta = layer_2_delta.dot(weights_1_2.T)
                    new = self.grad.mm(weights.transpose())
                    act.backward(new)
                    new = self.grad.transpose().mm(act).transpose()
                    weights.backward(new)
                
                if self.creation_op == "transpose":
                    self.creators[0].backward(self.grad.transpose())
                
                if "sum" in self.creation_op:
                    dim = int(self.creation_op.split("_")[1])
                    ds = self.creators[0].data.shape[dim]
                    self.creators[0].backward(self.grad.expand(dim, ds))
                
                if "expand" in self.creation_op:
                    dim = int(self.creation_op.split("_")[1])
                    self.creators[0].backward(self.grad.sum(dim))
                
                if self.creation_op == "sigmoid":
                    ones = Tensor(np.ones_like(self.grad.data))    
                    self.creators[0].backward(self.grad * (self * (ones - self)))

                if self.creation_op == "tanh":
                    ones = Tensor(np.ones_like(self.grad.data))    
                    self.creators[0].backward(self.grad * (ones - (self * self)))
                    
    # addition    
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
    
    # subtraction
    def __sub__(self, other):
        if self.autograd and other.autograd:
            return Tensor(self.data - other.data,
            autograd = True,
            creators = [self, other],
            creation_op = "sub")
        return Tensor(self.data - other.data)    
    
    # multiplication
    def __mul__(self, other):
        if self.autograd and other.autograd:
            return Tensor(self.data * other.data,
            autograd = True,
            creators = [self, other],
            creation_op = "mul")
        return Tensor(self.data * other.data)

    # summation
    def sum(self, dim):
        if self.autograd:
            return Tensor(self.data.sum(dim),
            autograd = True,
            creators = [self],
            creation_op = "sum_" + str(dim))
        return Tensor(self.data.sum(dim))
    
    # expanding
    def expand(self, dim, copies):
        trans_cmd = list(range(0, len(self.data.shape)))
        trans_cmd.insert(dim, len(self.data.shape))
        new_shape = list(self.data.shape) + [copies]
        
        new_data = self.data.repeat(copies).reshape(new_shape)    
        new_data = new_data.transpose(trans_cmd)
        
        if self.autograd:
            return Tensor(new_data,
            autograd = True,
            creators = [self],
            creation_op = "expand_" + str(dim))
        
        return Tensor(new_data)    
    
    # transposition
    def transpose(self):
        if self.autograd:
            return Tensor(self.data.transpose(),
            autograd = True,
            creators = [self],
            creation_op = "transpose")
        return Tensor(self.data.transpose()) 
    
    # matrix multiplication
    def mm(self, x):
        if self.autograd:
            return Tensor(self.data.dot(x.data),
            autograd = True,
            creators = [self, x],
            creation_op = "mm")
        return Tensor(self.data.dot(x.data))    
    
    def sigmoid(self):
        if self.autograd:
            return Tensor(1 / (1 + np.exp(-self.data)),
            autograd = True,
            creators = [self],
            creation_op = "sigmoid")
        return Tensor(1 / (1 + np.exp(-self.data)))    
        
    def tanh(self):
        if self.autograd:
            return Tensor(np.tanh(self.data),
            autograd = True,
            creators = [self],
            creation_op = "tanh")
        return Tensor(np.tanh(self.data))
    
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

#a = Tensor([1,2,3,4,5], autograd = True)
#b = Tensor([2,2,2,2,2], autograd = True)
#c = Tensor([5,4,3,2,1], autograd = True)

#d = a + b
#e = b + c
#f = d + e
#e = (-b) + c

#f.backward(Tensor(np.array([1,1,1,1,1])))
#print(b.grad.data == np.array([2,2,2,2,2]))

# support for additional functions
#x = Tensor(np.array([ [1,2,3], [4,5,6] ]))
#y = x.sum(0) 
#y2 = x.sum(1)
#z = x.expand(dim=2, copies=4)
#print(y)
#print(y2)
#print(z)
