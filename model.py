from keras import models, layers
import numpy as np
import matplotlib.pyplot as plt


def train_model(attributes, labels, val_data=None, layer_sizes=None, epochs=50, batch_size=5):
    model = models.Sequential()
    for layer_size in layer_sizes:
        model.add(layers.Dense(layer_size, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    if val_data:
        train_acc = model.fit(attributes, labels, epochs=epochs, batch_size=batch_size, validation_data=val_data)
    else:
        train_acc = model.fit(attributes, labels, epochs=epochs, batch_size=batch_size)

    return model, train_acc


def test_model(model, attributes, labels):
    test_loss, test_acc = model.evaluate(attributes, labels)
    print("Test Loss:", test_loss)
    print("Test Accuracy: ", test_acc)
    return test_loss, test_acc
