import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

# *** PARAMETERS ***

input_shape = (144,256)

# *** DATA INTAKE ***

# Parameters for data generators which directly read
# in the images, and thus don't need to analyze the image set as a whole.
intakeDatagenFlowConfig = dict(
    target_size=input_shape,
    class_mode="binary"
)

# Parameters for data generators which normalize the images,
# thus requiring a look at the whole dataset, which is given
# to them by the intake datagens, as seen above.
normalizDatagenConfiguration = dict(
    featurewise_center=True,
    featurewise_std_normalization=True,
    channel_shift_range=100,
    rescale=1./255
)

# Creating the data generators from the configurations above.
print("Configuring Data-Generators ...")
trainingDatagenIntake = ImageDataGenerator()
testingDatagenIntake  = ImageDataGenerator()
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

model = Sequential([
    Conv2D(
        32, kernel_size=(3, 3), strides=(1, 1),
        activation='relu',
        input_shape=input_shape
    ),
])