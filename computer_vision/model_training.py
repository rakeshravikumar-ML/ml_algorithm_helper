# This file contains the model training script for Computer Vision projects.
import tensorflow as tf
from tensorflow.keras import layers, models

def create_model(input_shape=(224, 224, 3), num_classes=10):
    """
    Builds and compiles a CNN model.
    """
    model = models.Sequential([
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
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model(model, train_data, val_data, epochs=10):
    """
    Trains the model using training data.
    """
    return model.fit(train_data, validation_data=val_data, epochs=epochs)
