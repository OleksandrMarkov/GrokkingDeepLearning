from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

from keras import models, layers

#model = models.Sequential([
#	layers.Dense(512, activation = 'relu'), # first layer
	# 10-переменный слой потерь, возвращает вероятности принадлежности изображения к цифрам
#	layers.Dense(10, activation = 'softmax') # second layer
#])

#model.compile(optimizer = 'rmsprop', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])


# show the train image
digit = train_images[4]
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

# preparing the image data 
#train_images = train_images.reshape((60000, 28*28))
#train_images = train_images.astype('float32') / 255
#test_images = test_images.reshape((10000, 28*28))
#test_images = test_images.astype('float32') / 255

# learning (сеть перебирает по 128 образцов). Всего 5 итераций по всем данным (эпоха).
#model.fit(train_images, train_labels, epochs = 5, batch_size = 128)

#test_loss, test_acc = model.evaluate(test_images, test_labels)
#print('test_acc: ', test_acc) # about 98%


