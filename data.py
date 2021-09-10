import numpy as np
import torchvision.datasets as datasets

def get_train_mnist():
    mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
    return mnist_trainset

def get_numbers_of_type(the_number):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()
    np_labels = mnist_train.train_labels.numpy()
    results = []
    for i in range(len(np_labels)):
        if np_labels[i] == the_number:
            results.append(np_images[i])
    return np.array(results)

def etalons_of1():
    np_images = get_numbers_of_type(the_number=1)
    indexes = [0,7,28,18,27,41,76,98]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars


def etalons_of3():
    np_images = get_numbers_of_type(the_number=3)
    indexes = [34,32,25,67,68,35, 210, 314,420, 496,620,659,635,667,733,715]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars

def etalons_of4():
    np_images = get_numbers_of_type(the_number=4)
    indexes = [94,101,100]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars

def etalons_of6():
    np_images = get_numbers_of_type(the_number=6)
    indexes = [220,221,222,235,330]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars

def get_diverse_set_of_numbers(n):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()[0:n]
    np_labels = mnist_train.train_labels.numpy()[0:n]
    return np_images, np_labels

def  get_all_data3():
    etalon_pic = etalons_of3()[0]
    dataset = get_numbers_of_type(3)
    n = len(dataset)
    trainset_len = int(n / 2)
    pics_train = get_numbers_of_type(3)[0:trainset_len]
    pics_test = get_numbers_of_type(3)[trainset_len + 1:n - 1]
    return etalon_pic, pics_train, pics_test