import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

model = Sequential([

])

intakeDatagenConfiguration = ImageDataGenerator(
    zoom_range=0.2,
    brightness_range=0.3,
    channel_shift_range=0.3,
    rescale=1./255
)

normalizDatagenConfiguration = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True
)

trainingDatagenIntake = ImageDataGenerator(**intakeDatagenConfiguration)
testingDatagenIntake  = ImageDataGenerator(**intakeDatagenConfiguration)
trainingDatagenNorm = ImageDataGenerator(**normalizDatagenConfiguration)
testingDatagenNorm  = ImageDataGenerator(**normalizDatagenConfiguration)

trainingDatagenIntake.fit()
testingDatagenNorm.fit()