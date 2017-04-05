  # -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
import scipy
import numpy as np
import argparse
import glob
import sys



# Same network definition as before
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=25.)
img_aug.add_random_blur(sigma_max=3.)

network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 8, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 8, 10, activation='relu')
network = conv_2d(network, 8, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)

model = tflearn.DNN(network, tensorboard_verbose=0, checkpoint_path='human-classifier.tfl.ckpt')
model.load("human-classifier.tfl")


if len(sys.argv) == 1:

    humancorrect = 0
    humanincorrect = 0
    dir = "datapruned/human/test/*.jpg"
    #dir = "people_all/*.jpg"
    for img in glob.glob(dir):
        try:

            n = scipy.ndimage.imread(img, mode="RGB")

            n = scipy.misc.imresize(n, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')
            prediction = model.predict([n])
            is_human = np.argmax(prediction[0]) == 0
            if is_human:
                humancorrect += 1
            else:
                humanincorrect += 1
        except:
            n = scipy.ndimage.imread(img, mode="RGB")
            print(img)
            print(n.shape)
            pass

    nonhumancorrect = 0
    nonhumanincorrect = 0
    dir = "datapruned/nonhuman/test/*.jpeg"
    #dir = "people_all/*.jpg"
    for img in glob.glob(dir):
        try:

            n = scipy.ndimage.imread(img, mode="RGB")

            n = scipy.misc.imresize(n, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')
            prediction = model.predict([n])
            is_nonhuman = np.argmax(prediction[0]) == 1
            if is_nonhuman:
                nonhumancorrect += 1
            else:
                nonhumanincorrect += 1
        except:
            pass


    print(humancorrect/(humancorrect+humanincorrect))
    print(nonhumancorrect/(nonhumancorrect+nonhumanincorrect))

else:
    parser = argparse.ArgumentParser(description='Decide if an image is a picture of a human')
    parser.add_argument('image', type=str, help='The image image file to check')
    args = parser.parse_args()

    # Load the image file
    img = scipy.ndimage.imread(args.image, mode="RGB")

    # Scale it to 32x32
    img = scipy.misc.imresize(img, (320, 320), interp="bicubic").astype(np.float32, casting='unsafe')

    # Predict
    prediction = model.predict([img])

    # Check the result.
    is_human = np.argmax(prediction[0]) == 0

    if is_human:
        print("That's a human!")
    else:
        print("That's not a human!")


