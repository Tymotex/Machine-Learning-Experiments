import tensorflow as tf
import matplotlib.pyplot as plt

# Dataset of 28x28 images with labels 0-9
mnistData = tf.keras.datasets.mnist

# Unpacking training data and testing data
(x_train, y_train), (x_test, y_test) = mnistData.load_data()

print(x_train)

# Naturally, each datapoint consists of 784 pixels, each with value 0-255 representing
# the intensity of the writing. We can scale these the domain to 0-1 (easier for the network to work with)
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Sequential models are the 'feed-forward' network models
model = tf.keras.models.Sequential()

# ===== Adding layers =====
# Input layer: the first layer should consist of 784 input nodes.
# The Flatten() method will 'flatten' the n-dimensional datapoint into a single row of values
model.add(tf.keras.layers.Flatten())

# 128 'neurons' in the layer
# 'relu' is a shorthand for 'rectified linear'. This is the go-to activation function
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

# Output layer: 
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# 
plt.imshow(x_train[1])
plt.show()












