import numpy as np

np.random.seed(0)

data = np.array([ [0,0], [0,1], [1,0], [1,1] ])
target = np.array([ [0], [1], [0], [1] ])

weights_0_1 = np.random.rand(2,3)
weights_1_2 = np.random.rand(3,1)

for i in range(10):
    layer_1 = data.dot(weights_0_1) # prediction
    layer_2 = layer_1.dot(weights_1_2)
    
    diff = (layer_2 - target) # comparing
    sqdiff = (diff * diff)
    
    loss = sqdiff.sum(0) # error
    
    # learning
    layer_1_grad = diff.dot(weights_1_2.transpose()) # backpropagation
    weights_1_2_update = layer_1.transpose().dot(diff)
    weights_0_1_update = data.transpose().dot(layer_1_grad)
    
    weights_1_2 -= weights_1_2_update * 0.1
    weights_0_1 -= weights_0_1_update * 0.1
    print(loss[0])