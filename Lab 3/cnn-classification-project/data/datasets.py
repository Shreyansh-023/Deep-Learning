def load_mnist():
    from tensorflow.keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255.0
    x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255.0
    return (x_train, y_train), (x_test, y_test)

def load_fashion_mnist():
    from tensorflow.keras.datasets import fashion_mnist
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255.0
    x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255.0
    return (x_train, y_train), (x_test, y_test)

def load_cifar10():
    from tensorflow.keras.datasets import cifar10
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    return (x_train, y_train), (x_test, y_test)

def get_dataset(dataset_name):
    if dataset_name == 'mnist':
        return load_mnist()
    elif dataset_name == 'fashion_mnist':
        return load_fashion_mnist()
    elif dataset_name == 'cifar10':
        return load_cifar10()
    else:
        raise ValueError("Dataset not recognized. Please choose 'mnist', 'fashion_mnist', or 'cifar10'.")