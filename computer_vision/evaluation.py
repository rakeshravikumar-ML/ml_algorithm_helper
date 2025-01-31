import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

def plot_loss_curves(history):
    """
    Plots training and validation loss/accuracy curves.
    """
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    
    epochs = range(len(loss))

    plt.figure(figsize=(8, 6))
    
    # Plot loss
    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss, label='Train Loss')
    plt.plot(epochs, val_loss, label='Val Loss')
    plt.legend()
    plt.title('Loss')
    
    # Plot accuracy
    plt.subplot(1, 2, 2)
    plt.plot(epochs, acc, label='Train Accuracy')
    plt.plot(epochs, val_acc, label='Val Accuracy')
    plt.legend()
    plt.title('Accuracy')
    
    plt.show()
    
def evaluate_model(model, test_data):
    """
    Evaluates the model on test data and prints classification metrics.
    """
    predictions = model.predict(test_data)
    y_true = np.concatenate([y for x, y in test_data], axis=0)
    y_pred = np.argmax(predictions, axis=1)
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

