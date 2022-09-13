# 1 Clear network with some inputs
def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i]*b[i])    
    return output

weights = [0.1, 0.2, -0.1]

def neural_network(input, weights):
    prediction = w_sum(input, weights)
    return prediction

# 2 Predicting and comparison

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

win_or_lose_binary = [1,1,0,1]

true = win_or_lose_binary[0]

input = [toes[0], wlrec[0], nfans[0]] # first game of the season

prediction = neural_network(input, weights)
# 8.5 * 0.1 + 0.65 * 0.2 + 1.2 * (-0.1) = 0.86

error = (prediction - true)**2
# (0.86 - 1)**2 is about -0.02

delta = prediction - true
# 0.86 - 1 = -0.14
# -0.14 < 0 => The prediction has very small value 

#3 Learning: calculating the derivatives 'weight_delta' and adding them to each weight

def ele_mul(number, vector):
    output = [0,0,0]
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output    

weight_deltas = ele_mul(delta, input)
alpha = 0.01

for i in range(len(weights)):
    weights[i] -= alpha * weight_deltas[i]
    print("Weights: " + str(weights))
    print("Weight Deltas: " + str(weight_deltas))
