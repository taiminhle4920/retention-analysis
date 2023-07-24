from data_file import write_to_file, read_data_file
from preprocessing import preprocess
from vectorize import vectorize_data, randomize
from model import train_model, test_model
import numpy as np
import matplotlib.pyplot as plt


def save_sets(name, train_size=1000):
    data = preprocess(name)
    attributes, labels = randomize(*vectorize_data(data))
    x_train, x_test = attributes[:train_size], attributes[train_size:]
    y_train, y_test = labels[:train_size], labels[train_size:]
    write_to_file('training_data', x_train, y_train)
    write_to_file('testing_data', x_test, y_test)


def train_and_validate(train_size=750, layer_sizes=None, tries=5):
    for i in range(tries):
        x, y = randomize(*read_data_file('training_data'))
        x_train, x_test = x[:train_size], x[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]
        model, history = train_model(x_train, y_train, (x_test, y_test), layer_sizes=layer_sizes)

        plt.clf()
        loss = history.history['loss']
        val_loss = history.history['val_loss']
        epochs = range(1, len(loss) + 1)
        plt.plot(epochs, loss, 'bo', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

        plt.clf()
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']
        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracies')
        plt.legend()
        plt.show()


def get_model(layer_sizes=None, epochs=10):
    return train_model(*randomize(*read_data_file('training_data')), layer_sizes=layer_sizes, epochs=epochs)[0]


def train_and_test(layer_sizes=None, epochs=None):
    model = get_model(layer_sizes=layer_sizes, epochs=epochs)
    x_test, y_test = randomize(*read_data_file('testing_data'))
    print(test_model(model, x_test, y_test))


def make_prediction(attributes, layer_sizes=None, epochs=None):
    model = get_model(layer_sizes=layer_sizes, epochs=epochs)
    print(model.predict(attributes))


def random_baseline():
    _, y_test = read_data_file('testing_data')
    _, y_test_copy = randomize([0]*len(y_test), y_test)
    return sum([1 if y == y_copy else 0 for y, y_copy in zip(y_test, y_test_copy)])/float(len(y_test))


def random_baselines(n=10000):
    outs = []
    for i in range(n):
        outs += [random_baseline()]
    print(sum(outs)/n)


if __name__ == '__main__':
    # save_sets('Attrition Data.csv')
    # train_and_validate(layer_sizes=[1])
    train_and_test(layer_sizes=[1], epochs=10)
    # random_baselines()
