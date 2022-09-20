from package.tensor import Tensor
from package.SGD import SGD
from package.linear import Linear
from package.sequential import Sequential
from package.MSELoss import MSELoss

from package.tanh import Tanh
from package.sigmoid import Sigmoid

import numpy as np
np.random.seed(0)

if __name__ == '__main__':
    data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd = True)
    target = Tensor(np.array([[0],[1],[0],[1]]), autograd = True)

    model = Sequential([Linear(2,3), Tanh(), Linear(3,1), Sigmoid()])
    criterion = MSELoss()    
        
    optim = SGD(parameters = model.get_parameters(), alpha = 1)

    for i in range(10):
        # Predict
        pred = model.forward(data)
        
        # Compare
        loss = criterion.forward(pred, target)
        
        # Learn
        loss.backward(Tensor(np.ones_like(loss.data)))
        optim.step()
        print(loss)