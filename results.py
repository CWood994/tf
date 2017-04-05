



small data
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 4)
network = conv_2d(network, 64, 3, activation='relu')
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 4)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
0.480952380952
0.89417989418


smalll data 100 epoch
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')

0.718089430894
0.703703703704







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

0.590280976509
0.767195767196

network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 8, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 16, 10, activation='relu')
network = conv_2d(network, 16, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)
0.441040994933
0.899470899471


network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 16, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 16, 10, activation='relu')
network = conv_2d(network, 16, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)
0.660525103639
0.719576719577

smalll data 10 epoch
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
0.864578535237
0.539682539683

smalll data 10 epoch
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 16, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 32, 10, activation='relu')
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam')
0.663519115615
0.740740740741

smalll data 10 epoch
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 1024, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')

0.650621833257
0.645502645503













all data 10 epoch
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
0.996951219512
0.10582010582 

----------------------------------------------------------------------------------------------


pruned data epoch 20
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
0.944495624136
0.687830687831

pruned data epoch 40
network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
0.945877475818
0.666666666667


network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 10, activation='relu')
network = max_pool_2d(network, 20)
network = conv_2d(network, 64, 10, activation='relu')
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 20)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)

0.982726853984
0.486772486772


network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 4)
network = conv_2d(network, 64, 3, activation='relu')
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 4)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)
1.0
0.0

network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 20, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 64, 20, activation='relu')
network = conv_2d(network, 64, 20, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)
1.0
0.0

network = input_data(shape=[None, 320, 320, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 64, 10, activation='relu')
network = max_pool_2d(network, 8)
network = conv_2d(network, 128, 10, activation='relu')
network = conv_2d(network, 128, 10, activation='relu')
network = max_pool_2d(network, 8)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)

1.0
0.0













