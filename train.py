# -*- coding: utf-8 -*-

"""
Based on the tflearn example located here:
https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py
"""
from __future__ import division, print_function, absolute_import

# Import tflearn and some helpers
import tflearn
from tflearn.data_utils import shuffle
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
import pickle
import tensorflow
import glob


X = []
Y = []
X_test = []
Y_test = []


import scipy
import numpy as np


dir = "datapruned/human/7070/trainsmall/*.jpg"
#dir = "people_all/*.jpg"
height = []
width = []
for img in glob.glob(dir):
    n = scipy.ndimage.imread(img, mode="RGB")

    #if n.shape[0]>= 300 and n.shape[1]>=300:
    n = scipy.misc.imresize(n, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')

    X.append(n)
    Y.append([1., 0.])
#scipy.misc.imsave('gradient2.jpg', X[0])

print("Human Train done")
dir = "datapruned/nonhuman/train/*.jpeg"
#dir = "people_all/*.jpg"
for img in glob.glob(dir):
    n = scipy.ndimage.imread(img, mode="RGB")

    n = scipy.misc.imresize(n, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')

    X.append(n)
    Y.append([0., 1.])
print("NonHuman Train done")


dir = "datapruned/human/7070/valsmall/*.jpg"
for img in glob.glob(dir):
    #print(img)
    n = scipy.ndimage.imread(img, mode="RGB")
    n = scipy.misc.imresize(n, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')

    X_test.append(n)
    Y_test.append([1., 0.])
print("Human Val done")


dir = "datapruned/nonhuman/val/*.jpeg"
for img in glob.glob(dir):
    #print(img)
    n = scipy.ndimage.imread(img, mode="RGB")
    n = scipy.misc.imresize(n, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')

    X_test.append(n)
    Y_test.append([0., 1.])
print("NonHuman Val done")




# Shuffle the data
X, Y = shuffle(X, Y)
X_test, Y_test = shuffle(X_test, Y_test)


# Make sure the data is normalized
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()

# Create extra synthetic training data by flipping, rotating and blurring the
# images on our data set.
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=25.)
img_aug.add_random_blur(sigma_max=3.)

# Define our network architecture:

# Input is a 32x32 image with 3 color channels (red, green and blue)
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)

# Step 1: Convolution
network = conv_2d(network, 8, 10, activation='relu')

# Step 2: Max pooling
network = max_pool_2d(network, 8)

# Step 3: Convolution again
network = conv_2d(network, 8, 10, activation='relu')

# Step 4: Convolution yet again
network = conv_2d(network, 8, 10, activation='relu')

# Step 5: Max pooling again
network = max_pool_2d(network, 8)

# Step 6: Fully-connected 512 node neural network
network = fully_connected(network, 512, activation='relu')

# Step 7: Dropout - throw away some data randomly during training to prevent over-fitting
network = dropout(network, 0.5)

# Step 8: Fully-connected neural network with two outputs (0=isn't a bird, 1=is a bird) to make the final prediction
network = fully_connected(network, 2, activation='softmax')

# Tell tflearn how we want to train the network
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)

# Wrap the network in a model object
model = tflearn.DNN(network, tensorboard_verbose=0, checkpoint_path='human-classifier.tfl.ckpt')

# Train it! We'll do 100 training passes and monitor it as it goes.
#model.fit(X, Y)
model.fit(X, Y, n_epoch=10, shuffle=True, validation_set=(X_test, Y_test),
          show_metric=True,
          snapshot_epoch=False,
          run_id='human-classifier')

# Save model when training is complete to a file
model.save("human-classifier.tfl")
print("Network trained and saved as human-classifier.tfl!")