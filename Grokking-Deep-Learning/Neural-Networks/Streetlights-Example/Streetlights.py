import numpy as np

streetlights = np.array([[ 1, 0, 1 ],				
                         [ 0, 1, 1 ],				
                         [ 0, 0, 1 ],					
                         [ 1, 1, 1 ],					
                         [ 0, 1, 1 ],					
                         [ 1, 0, 1 ]])

walk_vs_stop = np.array([[0],
                         [1],
                         [0],
                         [1],
                         [1],
                         [0]])

weights = np.array([0.5, 0.48, -0.7])
alpha = 0.1
input = streetlights[0]
true_value = walk_vs_stop[0]

# for i in range(20):
#     prediction = np.dot(input, weights)
#     error = (prediction - true_value) ** 2
#     delta = prediction - true_value
#     weight_delta = delta * input
#     weights = weights - (alpha * weight_delta)
#     print("Error: {}, Prediction: {}".format(error, prediction))


for iteration in range(40):
    error_for_all_lights = 0
    for row_index in range(len(walk_vs_stop)):
        input = streetlights[row_index]
        goal_prediction = walk_vs_stop[row_index]
        prediction = np.dot(input, weights)
        error = (goal_prediction - prediction) ** 2
        error_for_all_lights += error
        delta = prediction - goal_prediction
        weights = weights - (alpha * (input * delta))
        print("Prediction:" + str(prediction))
    print("Error:" + str(error_for_all_lights) + "\n")

print("Should be 1: {}".format(np.dot([1, 1, 1], weights)))
print("Should be 0: {}".format(np.dot([1, 0, 1], weights)))

print("Should be 1: {}".format(np.dot([0, 1, 0], weights)))
print("Should be 0: {}".format(np.dot([0, 0, 0], weights)))


