import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import cv2
# import tensorflow as tf
from PIL import Image
import os
import pickle

data = []
labels = []
O_sizes = []
classes = 43
cur_path = os.getcwd()
print(cur_path)
cur_path = os.path.join(cur_path, 'archive')
print(cur_path)

def training_set_pickeled_file(cur_path, name):
    data = [] # features
    labels = []
    O_sizes = []

    # Retrieving the images and their labels
    for i in range(classes):
        print(i)

        path = os.path.join(cur_path, name, str(i))
        print(path)
        images = os.listdir(path)
        for a in images:
            try:
                print("Inside the Train folder, no error")
                image = Image.open(path + '\\' + a)
                width, height = image.size
                O_sizes.append((width, height))
                image = image.resize((32, 32))
                image = np.array(image)
                # sim = Image.fromarray(image)
                data.append(image)
                labels.append(i)
            except:
                print("Error loading image")
    # Converting lists into numpy arrays
    data = np.array(data)
    labels = np.array(labels)
    O_sizes = np.array(O_sizes)
    return [data, labels, O_sizes]

training_set = training_set_pickeled_file(cur_path, 'Train')
d = {'features': training_set[0], 'labels': training_set[1], 'sizes': training_set[2]}
f = open('train.p', 'wb')
pickle.dump(d, f)
f.close()

# print(training_set[0].shape, training_set[1].shape)

def Testing_set_pickeled_file(cur_path):
    data = []
    labels = []
    O_sizes = []

    # Retrieving the images and their labels

    path = os.path.join(cur_path, 'Test')
    print(path)
    images = os.listdir(path)
    for i, a in enumerate(images):
        try:
            print("Inside the Test folder, no error")
            image = Image.open(path + '\\' + a)
            width, height = image.size
            O_sizes.append((width, height))
            image = image.resize((32, 32))
            image = np.array(image)
            # sim = Image.fromarray(image)
            data.append(image)
            labels.append(i)
        except:
            # error
            print("Error loading image")

    # Converting lists into numpy arrays
    data = np.array(data)
    labels = np.array(labels)
    O_sizes = np.array(O_sizes)

    return [data, labels, O_sizes]

testing_set = Testing_set_pickeled_file(cur_path)
d = {'features': testing_set[0], 'labels': testing_set[1], 'sizes': testing_set[2]}
test = open('test.p', 'wb')
pickle.dump(d, test)
test.close()


# sample changes
def Validing_set_pickeled_file(cur_path):
    data = []
    labels = []
    O_sizes = []

    # Retrieving the images and their labels

    path = os.path.join(cur_path, 'Test')
    print(path)
    images = os.listdir(path)
    for i, a in enumerate(images):
        try:
            print("Inside the Valid folder, no error")
            image = Image.open(path + '\\' + a)
            width, height = image.size
            O_sizes.append((width, height))
            image = image.resize((32, 32))
            image = np.array(image)
            # sim = Image.fromarray(image)
            data.append(image)
            labels.append(i)
        except:
            # error
            print("Error loading image")

    # Converting lists into numpy arrays
    data = np.array(data)
    labels = np.array(labels)
    O_sizes = np.array(O_sizes)

    return [data, labels, O_sizes]

validing_set = Validing_set_pickeled_file(cur_path)
d = {'features': validing_set[0], 'labels': validing_set[1], 'sizes': validing_set[2]}
valid = open('valid.p', 'wb')
pickle.dump(d, valid)
valid.close()