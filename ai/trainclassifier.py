import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.layers import Dropout, Dense, Flatten
from keras.layers import Conv2D, SpatialDropout2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint

# *** PARAMETERS ***



# *** DATA INTAKE ***

# Parameters for data generators which directly read
# in the images, and thus don't need to analyze the image set as a whole.
intakeDatagenConfiguration = dict(
    channel_shift_range=100,
    rescale=1./255,
    validation_split=0.1
)
intakeDatagenFlowConfig = dict(
    target_size=(288,512),
    class_mode="binary"
)

# Parameters for data generators which normalize the images,
# thus requiring a look at the whole dataset, which is given
# to them by the intake datagens, as seen above.
normalizDatagenConfiguration = dict(
    featurewise_center=True,
    featurewise_std_normalization=True,
)

# Creating the data generators from the configurations above.
print("Configuring Data-Generators ...")
trainingDatagenIntake = ImageDataGenerator(**intakeDatagenConfiguration)
testingDatagenIntake  = ImageDataGenerator(**intakeDatagenConfiguration)
trainingDatagenNorm = ImageDataGenerator(**normalizDatagenConfiguration)
testingDatagenNorm  = ImageDataGenerator(**normalizDatagenConfiguration)
print("... Done Configuring Data-Generators")

# Tell the intake data generators to take images
# from the proper folders
# TODO: These should both be moved into larger statements, not saved to variables.

#trainingIntakeIterator = trainingDatagenIntake.flow_from_directory("sorted_data/", **intakeDatagenFlowConfig)
#testingIntakeIterator = testingDatagenIntake.flow_from_directory("")

# Tell the normalization datagens to take images from the intake datagens
# TODO: Also move into larger statements, not saved to variables.

#trainingNormIterator = trainingDatagenNorm.flow(trainingIntakeIterator, save_prefix="Norm", save_to_dir="augmented_data")
#testingNormIterator = 

# Give the normalization data generators a look at the data
# coming out of the intake data generators, so that they can
# adjust (normalize) the data properly.
# TODO: The training and testing data are normalized separately. Do we really want this?

#print("Fitting Normalization Data-Generator ...")
#trainingDatagenNorm.fit(
#    trainingDatagenIntake.flow_from_directory( # Really slow! TODO: Speed up? Possible even?
#        "sorted_data/",
#        **intakeDatagenFlowConfig
#    )
#)
#print("... Done Fitting Normalization Data-Generator")
#testingDatagenNorm.fit(testingIntakeIterator)

# TODO: Delete this, or move into the input for fitting the model – this is just to test.

#print("Testing Normalization Datagen ...")
#dumpingintothisvar = trainingDatagenNorm.flow(
#    trainingDatagenIntake.flow_from_directory(
#        "sorted_data/",
#        **intakeDatagenFlowConfig
#    ),
#    save_prefix="Norm",
#    save_to_dir="augmented_data"
#)
#print("... Done Testing Normalization Datagen")

# *** ACTUAL NEURAL NET ***

print("Configuring Neural Network ... ")
deepCNN = Sequential([
    Conv2D( #1
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu',
        input_shape=(288, 512, 3)
    ),
    SpatialDropout2D(0.6),
    Conv2D( #2
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu'
    ),
    SpatialDropout2D(0.6),
    Conv2D( #3
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu'
    ),
    SpatialDropout2D(0.6),
    Conv2D( #4
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu'
    ),
    SpatialDropout2D(0.6),
    Conv2D( #5
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu'
    ),
    SpatialDropout2D(0.6),
    Conv2D( #6
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu'
    ),
    SpatialDropout2D(0.6),
    Conv2D( #7
        32, kernel_size=(3, 3), strides=(2, 2),
        activation='relu',
        input_shape=(3, 7, 32)
    ),
    Flatten(),
    Dense(672), # 3x7x32=672
    Dropout(0.5),
    Dense(300),
    Dropout(0.5),
    Dense(100),
    Dropout(0.5),
    Dense(20),
    Dense(1, activation='sigmoid')
])
print("... Done Configuring Neural Network")

# Load weights from the best performing checkpoint
print("Loading Weights ... ")
try:
    deepCNN.load_weights('checkpoints/weights.best.hdf5')
    print("... Done Loading Weights")
except Exception:
    print(Exception)
    print("... Couldn't find checkpoint file")
    pass

# Prepare the neural network for training
print("Compiling Neural Network ... ")
deepCNN.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
print("... Done Compiling Neural Network")

# Train the model!
print("Training Neural Network ... ")
deepCNN.fit_generator(
    trainingDatagenIntake.flow_from_directory(
        'sorted_data',
        subset='training',
        **intakeDatagenFlowConfig
    ),
    verbose=1,
    epochs=1000,
    steps_per_epoch=12,
    callbacks=[
        ModelCheckpoint(
            'checkpoints/weights.{epoch:02d}-{val_acc:.2f}.hdf5',
            monitor='val_acc',
            mode='max',
            save_best_only=True
        ),
        ModelCheckpoint(
            'checkpoints/weights.best.hdf5',
            monitor='val_acc',
            mode='max',
            save_best_only=True
        )
    ],
    validation_data=trainingDatagenIntake.flow_from_directory(
        'sorted_data',
        subset='validation',
        **intakeDatagenFlowConfig
    ),
    validation_steps=2,
    workers=4,
    use_multiprocessing=True
)
print("... Done Training Neural Network")