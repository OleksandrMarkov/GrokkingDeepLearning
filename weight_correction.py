#1 clear network
weight = 0.1
alpha = 0.01

def neural_network(input, weight):
    prediction = input * weight
    return prediction

#2 predicting
number_of_toes = [8.5]
win_or_lose_binary = [1] #  victory

input = number_of_toes[0] # input cannot be changed during predicting
goal_pred = win_or_lose_binary[0] # real observation

for iteration in range(4):
    pred = neural_network(input, weight) # 0.85
    error = (pred - goal_pred)**2 # clear error

    #3 comparison
    delta = pred - goal_pred # 0.85 - 1 = - 0.15

    #4 learning
    weight_delta = input * delta

    #5 correction of weight
    weight -= weight_delta * alpha

    print("Error: " + str(error) + "Prediction:" + str(pred))
