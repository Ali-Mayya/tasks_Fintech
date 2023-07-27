# tasks_Fintech
# Task1 : Images Classification in MNIST with Data Augmentation

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

# Task 2: Database SQL-Python
In this task, I utilized SQLite to organize the database for employee information. The choice of SQLite was driven by its simplicity, user-friendliness, and my prior experience with the technology. The database file was named "company_Insta_Perm.db," and it featured a single table called "employee."

## Table Structure
The "employee" table includes the following columns:

- id (INTEGER PRIMARY KEY): A unique identifier for each employee, serving as the primary key for data integrity.
- name (TEXT NOT NULL): The name of the employee, stored as text to accommodate diverse names.
- age (INTEGER NOT NULL): The age of the employee, represented as an integer for precise numerical storage.
- position (TEXT NOT NULL): The job position or title of the employee, stored as text to allow descriptive entries.
- city (TEXT NOT NULL): The city where the employee is based, also stored as text to accommodate various locations.
- 
## Functionality
To interact with the "employee" table, the code includes four vital functions:

- Add Data (add_data)
The add_data function enables the addition of new employee records to the "employee" table. It accepts input parameters such as the employee's name, age, position, and city, and inserts the provided data into the table using the SQL INSERT command. The function ensures the successful addition of data by committing the changes to the database.

- Get Data (get_data)
The get_data function facilitates the retrieval of employee records based on specified conditions from the "employee" table. It employs the SQL SELECT command to filter data according to the provided query conditions. Once the matched records are found, the function fetches and displays them on the console, making data extraction convenient.

- Update Data (update_data)
The update_data function empowers the updating of employee records in the "employee" table based on specified conditions. It uses the SQL UPDATE command to modify the relevant data fields as per the new values provided in the query. To ensure data consistency, the function commits the changes to the database after updating the records.

- Delete Data (delete_data)
Lastly, the delete_data function provides the capability to remove employee records based on specific criteria. Using the SQL DELETE command, it identifies and deletes the desired data entries from the "employee" table. Similar to other functions, this function ensures the permanence of data removal by committing the changes to the database.

## Justification
SQLite proves to be an ideal choice for this project due to its lightweight and serverless nature. As a self-contained, file-based database management system, SQLite eliminates the need for a separate database server, making it particularly suitable for small-scale projects or prototypes. Additionally, the ease of installation and setup, along with my prior experience with SQLite, expedited the development process and streamlined the interaction with the database.

The decision to employ a single-table structure for the database was pragmatic, as it allows a clear and concise demonstration of basic CRUD operations. This simplicity enables readers to grasp the essence of the code effortlessly, making it an ideal choice for showcasing employee record management.

Note: The provided script showcases efficient interaction with an SQLite database for managing employee records.

---
# Task3: Integration with Google API

In this Python script, we integrated with the Google Geocoding API to retrieve latitude and longitude coordinates for a given address. The code is organized as follows:

## Function for Geocoding Data

The core functionality is wrapped within the `get_geocoding_data` function, which takes the API key and address as input. This function sends a request to the Google Geocoding API and processes the response to extract the geocoding data (latitude and longitude).

## API Request and Error Handling

We used the `requests` library to make an API request to the Google Geocoding service. The code is designed with a try-except block to handle potential errors, such as connectivity issues or invalid API keys. This ensures smooth execution and user-friendliness.

## Data Processing and Output

After obtaining the API response, the code processes the JSON data to extract the geocoding information. We check the 'status' field to confirm if the request was successful. If the status is 'OK', we extract and print the latitude and longitude data. In case of an error, an appropriate error message is displayed.

# Justification and Benefits

The following are the benefits of the methods used in the script:

## Function Modularity

By encapsulating the core logic within the `get_geocoding_data` function, the code becomes more organized and modular. This approach enhances code readability and allows easy reuse for different addresses and API keys.

## Ease of API Interaction

The `requests` library simplifies making API requests, handling the complexities of HTTP communication. Its simple syntax and wide usage make it a suitable choice for this task.

## Error Handling

The try-except block ensures graceful handling of errors during API requests. Instead of abrupt program termination, users receive informative error messages, aiding in debugging and providing a better user experience.

## JSON Data Processing

The script processes the API response, which is typically in JSON format, to extract the required geocoding data. JSON is a lightweight and easy-to-read data interchange format, commonly used in web APIs.

## User-Friendly Output

The script presents the obtained geocoding data in a clear and concise format, with explicit information about the address, latitude, and longitude. This user-friendly approach improves script usability.



In summary, the code effectively integrates with the Google Geocoding API, retrieves geocoding data for a specified address, and presents the results in a user-friendly manner. The chosen methods and organization enhance code modularity, error handling, data processing, and overall user experience when interacting with the API.


