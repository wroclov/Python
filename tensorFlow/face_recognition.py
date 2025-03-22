import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

# Load images and labels
def load_data(data_dir, img_size=(100, 100)):
    X, y, labels = [], [], {}
    label_id = 0

    for person in os.listdir(data_dir):
        person_dir = os.path.join(data_dir, person)
        if not os.path.isdir(person_dir):
            continue

        if person not in labels:
            labels[person] = label_id
            label_id += 1

        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, img_size)
            X.append(img)
            y.append(labels[person])

    X = np.array(X) / 255.0  # Normalize
    X = X.reshape(-1, img_size[0], img_size[1], 1)
    y = np.array(y)

    return X, y, labels

# Define CNN model
def create_model(input_shape, num_classes):
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Train model
data_dir = "faces_dataset"  # Folder containing subfolders of faces
X, y, labels = load_data(data_dir)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = create_model(X.shape[1:], len(labels))
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save model
# h5 stands for Hierarchical Data Format 5 (HDF5), a popular format for storing large numerical data.
model.save("face_recognition_model.h5") 

# Recognize a new face
def recognize_face(image_path, model, labels, img_size=(100, 100)):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, img_size)
    img = img / 255.0
    img = img.reshape(1, img_size[0], img_size[1], 1)

    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)
    
    for name, label in labels.items():
        if label == predicted_label:
            return name
    return "Unknown"

# Load model and test
model = keras.models.load_model("face_recognition_model.h5")
test_image = "test_face.jpg"
recognized_person = recognize_face(test_image, model, labels)
print(f"Recognized Person: {recognized_person}")
