from package.tensor import Tensor
from package.SGD import SGD
from package.linear import Linear
from package.sequential import Sequential
import numpy as np
np.random.seed(0)

if __name__ == '__main__':
    data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd = True)
    target = Tensor(np.array([[0],[1],[0],[1]]), autograd = True)

    model = Sequential([Linear(2,3), Linear(3,1)])
    
    optim = SGD(parameters = model.get_parameters(), alpha = 0.05)

    for i in range(10):
        # Predict
        pred = model.forward(data)
        
        # Compare
        loss = ((pred - target)*(pred - target)).sum(0)
        
        # Learn
        loss.backward(Tensor(np.ones_like(loss.data)))
        optim.step()
        print(loss)