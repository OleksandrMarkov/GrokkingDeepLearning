from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape) # 60000 28 28
print(test_images.shape) # 10000 28 28
print(len(test_labels)) # 10000