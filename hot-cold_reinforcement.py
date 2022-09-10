weight = 0.5
input = 0.5

goal_prediction = 0.8

step_amount = 0.001 # usually random

for iteration in range(1101):

    prediction = input * weight
    error = (prediction - goal_prediction)**2
    print(f"Error: {error}. Prediction: {prediction}")
    
    up_prediction = input*(weight + step_amount)
    up_error = (goal_prediction - up_prediction)**2
    
    down_prediction = input*(weight - step_amount)
    down_error = (goal_prediction - down_prediction)**2
    
    if (down_error < up_error):
        weight -= step_amount
        
    if (down_error > up_error):
        weight += step_amount    