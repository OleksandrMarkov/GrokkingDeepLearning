from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape) # array 60000x28x28
print(train_images.ndim) # 3
print(train_images.dtype) #uint8

print(test_images.shape) # array 10000x28x28
print(len(test_labels)) # 10000
