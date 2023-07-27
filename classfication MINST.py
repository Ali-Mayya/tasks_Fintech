import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

# Load the MNIST dataset and split it into training and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to the range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Convert labels to one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Create an ImageDataGenerator for data augmentation
datagen = ImageDataGenerator(rotation_range=90)  # Allowable rotation angle in the range [-90, 90]
# i applied the in order to make the model more able to recognize the flipped images or rotated images or numbers

# Use fit to compute augmentation statistics on the training data
datagen.fit(x_train.reshape(-1, 28, 28, 1))  # Reshape data for ImageDataGenerator to work with

# Create a simple neural network model
model = Sequential()

# Add layers to the model
model.add(Flatten(input_shape=(28, 28)))  # Flatten 2D array (28x28) to 1D array (length 784)
model.add(Dense(128, activation='relu'))   # Fully connected layer with 128 neurons and ReLU activation
model.add(Dense(64, activation='relu'))    # Fully connected layer with 64 neurons and ReLU activation
model.add(Dense(10, activation='softmax')) # Output layer with 10 neurons for classification (digits 0 to 9)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model on augmented data
model.fit(datagen.flow(x_train.reshape(-1, 28, 28, 1), y_train, batch_size=32),
          steps_per_epoch=len(x_train) // 32, epochs=5, validation_data=(x_test.reshape(-1, 28, 28, 1), y_test))

# Evaluate the accuracy on the test data
accuracy = model.evaluate(x_test.reshape(-1, 28, 28, 1), y_test)[1]
print("Accuracy on test data: {:.2f}%".format(accuracy * 100))


#using evalution metrrics

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

y_pred = model.predict(x_test.reshape(-1, 28, 28, 1))
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

# 1. Accuracy
accuracy = accuracy_score(y_true_classes, y_pred_classes)
print("Accuracy: {:.2f}%".format(accuracy * 100))

# 2. Confusion Matrix
confusion_mtx = confusion_matrix(y_true_classes, y_pred_classes)
print("Confusion Matrix:")
print(confusion_mtx)

# 3. Precision, Recall, and F1 Score (per class)
classification_rep = classification_report(y_true_classes, y_pred_classes)
print("Classification Report:")
print(classification_rep)

##printing the results

import random

cpt = 0
c = 0
predict = list()
print(" the number corresponding to the classified images ")
for i in range(1, 21):
    cpt = cpt + 1
    # /content/images/images/train/angry/0.jpg
    plt.subplot(7, 5, cpt)
    plt.imshow(x_test[cpt])
    predict.append(y_pred_classes[cpt])
    if (i % 5 == 0):
        print(predict[c:c + i])
        c = i

# plt.tight_layout()
plt.show()