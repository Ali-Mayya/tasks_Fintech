# tasks_Fintech
# Task1 : mage Classification with Data Augmentation

This Python code demonstrates a simple image classification task using the MNIST dataset. The goal is to recognize handwritten digits (0 to 9) from grayscale images. The code utilizes TensorFlow and Keras to build and train a neural network for this classification task.

## Method of Classification Used

The classification model used in this code is a feedforward neural network (also known as a fully connected network). It consists of an input layer with 784 (28x28) neurons (due to the flattened input images), followed by two hidden layers with 128 and 64 neurons, respectively. The activation function used for the hidden layers is Rectified Linear Unit (ReLU), which helps introduce non-linearity to the model. The output layer has 10 neurons, representing the 10 possible classes (digits 0 to 9). The activation function used for the output layer is Softmax, which converts the raw scores into class probabilities, allowing the model to make a probability-based prediction for each class.

## Benefits of the Network's Architecture

- Simplicity: The network's architecture is straightforward, reducing complexity and computation time. For the MNIST dataset, a deeper and more complex network is not required as the task involves relatively simple grayscale images of digits.

- Good Performance: Despite its simplicity, this network architecture has shown good performance for image classification tasks, making it suitable for the MNIST digit recognition problem.

- Generalization: The network's limited depth and number of parameters help prevent overfitting and enhance generalization to unseen data.

## Benefits of Data Augmentation with ImageDataGenerator

- Increased Robustness: Data augmentation, specifically rotation in this case, makes the model more robust to variations in the input data. The model becomes better at recognizing digits that are rotated in the test set.

- Generalization and Reduced Overfitting: Data augmentation artificially increases the size of the training dataset with diverse variations. This reduces overfitting and allows the model to generalize better to unseen data.

## Rotation Data Augmentation with ImageDataGenerator

The code uses ImageDataGenerator to apply rotation data augmentation to the training images. The `rotation_range=90` allows random rotation of images by angles within the range [-90, 90]. This introduces diversity in the training data and helps the model handle rotation variations in the test images.

## Evaluation Metrics

- Accuracy: 94.43% - The proportion of correctly classified instances among all instances. It indicates the overall performance of the model in recognizing digits.

- Confusion Matrix: Provides detailed insights into the model's performance for each class. It shows the number of true positive, true negative, false positive, and false negative predictions for each digit.

- Precision, Recall, and F1-score: These metrics were used to evaluate the model's performance for each individual class. Precision measures the true positive predictions among all positive predictions, recall measures the true positive predictions among all actual positive instances, and the F1-score balances precision and recall.

The chosen evaluation metrics are suitable for the image classification task, providing a comprehensive view of the model's performance on the MNIST dataset.

---

