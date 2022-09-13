           #toes %win #fans
weights = [[0.1, 0.1, -0.3], # hurt?
           [0.1, 0.2, 0.0], # win?
           [0.0, 1.3, 0.1] ] # sad?

def w_sum(a,b):
    assert(len(a)==len(b))
    output = 0

    for i in range(len(a)):
        output += (a[i]*b[i])
    return output

def vect_mat_mul(vector, matrix):
    assert(len(matrix) == len(vector))
    output = [0,0,0]
    for i in range(len(vector)):
        output[i] = w_sum(vector, matrix[i])
    return output

def neural_network(input, weights):
    prediction = vect_mat_mul(input, weights)
    return prediction

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1,1,0,1]
sad = [0.1, 0.0, 0.1, 0.2]

alpha = 0.01


input = [toes[0], wlrec[0], nfans[0]]
true = [hurt[0], win[0], sad[0]]

prediction = neural_network(input, weights)

error = [0,0,0]
delta = [0,0,0]

for i in range(len(true)):
    error[i] = (prediction[i] - true[i])**2
    delta[i] = prediction[i] - true[i]


import numpy as np

def outer_prod(vect_a, vect_b):
    # a matrix of zeros
    output = np.zeros((len(vect_a), len(vect_b)))

    for i in range(len(vect_a)):
        for j in range(len(vect_b)):
            output[i][j] = vect_a[i]*vect_b[j]
    return output

weight_deltas = outer_prod(delta, input)

for i in range(len(weights)):
    for j in range(len(weights[0])):
        weights[i][j] -= alpha * weight_deltas[i][j]
        print("Weights:" + str(weights[i][j]))
        print("Weight Deltas:" + str(weight_deltas[i][j]))
