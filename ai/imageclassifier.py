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
    zoom_range=0.2,
    brightness_range=[-0.3, 0.3],
    channel_shift_range=0.3,
    rescale=1./255
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
# TODO: Remove save_to_dir
testingDatagenIntake.flow_from_directory(
    "sorted_data/monjan13",
    target_size=(256,144),
    class_mode="binary",    
    save_to_dir="/Users/nwaterman2022/Documents/GitHub/mischiefdetector/augmented_data"
)
#trainingDatagenIntake

# Give the normalization data generators a look at the data
# coming out of the intake data generators, so that they can
# adjust (normalize) the data properly.
# TODO: The training and testing data are normalized separately. Do we really want this?
#trainingDatagenNorm.fit(trainingDatagenIntake)
#testingDatagenNorm.fit(testingDatagenIntake)

