def neural_network(input, weights):
    output = 0
    for i in range(len(input)):
        output += (input[i]*weights[i])
    return output

def ele_mul(scalar, vector):
    output = [0,0,0]
    for i in range(len(output)):
        output[i] = scalar * vector[i]
    return output

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

win_or_lose_binary = [1,1,0,1]
true = win_or_lose_binary[0]

alpha = 0.01
input = [toes[0], wlrec[0], nfans[0]] # first game of the season
weights = [0.1, 0.2, -0.1]

for iteration in range(3):
    prediction = neural_network(input, weights)

    error = (prediction - true)**2
    delta = prediction - true

    weight_deltas = ele_mul(delta, input)
    print("Iteration:" + str(iteration + 1))
    print("Prediction:" + str(prediction))
    print("Error:" + str(error))
    print("Delta:" + str(delta))
    print("weights:" + str(weights))
    print("Weight Deltas: " + str(weight_deltas))

    for i in range(len(weights)):
        weights[i] -= alpha * weight_deltas[i]
