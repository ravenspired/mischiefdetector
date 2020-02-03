import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

#model = Sequential([
#
#])

# Parameters for data generators which directly read
# in the images and augment each individually, and thus
# don't need to analyze the image set as a whole.
intakeDatagenConfiguration = dict(
    channel_shift_range=100,
    rescale=1./255
)
intakeDatagenFlowConfig = dict(
    target_size=(144,256),
    class_mode="binary"
)

# Parameters for data generators which normalize the images,
# thus requiring a look at the whole dataset, which is given
# to them by the intake datagens, as seen above.
normalizDatagenConfiguration = dict(
    featurewise_center=True,
    featurewise_std_normalization=True
)

# Creating the data generators from the configurations above.
trainingDatagenIntake = ImageDataGenerator(**intakeDatagenConfiguration)
testingDatagenIntake  = ImageDataGenerator(**intakeDatagenConfiguration)
trainingDatagenNorm = ImageDataGenerator(**normalizDatagenConfiguration)
testingDatagenNorm  = ImageDataGenerator(**normalizDatagenConfiguration)

# Tell the intake data generators to take images
# from the proper folders
trainingIntakeIterator = trainingDatagenIntake.flow_from_directory("sorted_data/", **intakeDatagenFlowConfig)
#testingIntakeIterator = testingDatagenIntake.flow_from_directory("")

# Tell the normalization datagens to take images from the intake datagens
# TODO: Finish this
trainingNormIterator = trainingDatagenNorm.flow
testingNormIterator = 

# Give the normalization data generators a look at the data
# coming out of the intake data generators, so that they can
# adjust (normalize) the data properly.
# TODO: The training and testing data are normalized separately. Do we really want this?
trainingDatagenNorm.fit(trainingIntakeIterator)
#testingDatagenNorm.fit(testingIntakeIterator)