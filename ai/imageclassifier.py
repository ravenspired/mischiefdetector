import tensorflow as tf
import numpy as np
import cv2
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

# Borrowed From StackOverflow, Page Archived at:
# https://web.archive.org/web/20200203015002/http://stackoverflow.com/questions/37119071/scipy-rotate-and-zoom-an-image-without-changing-its-dimensions
def cv2_clipped_zoom(img, zoom_factor):
    """
    Center zoom in/out of the given image and returning an enlarged/shrinked view of 
    the image without changing dimensions
    Args:
        img : Image array
        zoom_factor : amount of zoom as a ratio (0 to Inf)
    """
    height, width = img.shape[:2] # It's also the final desired shape
    new_height, new_width = int(height * zoom_factor), int(width * zoom_factor)

    ### Crop only the part that will remain in the result (more efficient)
    # Centered bbox of the final desired size in resized (larger/smaller) image coordinates
    y1, x1 = max(0, new_height - height) // 2, max(0, new_width - width) // 2
    y2, x2 = y1 + height, x1 + width
    bbox = np.array([y1,x1,y2,x2])
    # Map back to original image coordinates
    bbox = (bbox / zoom_factor).astype(np.int)
    y1, x1, y2, x2 = bbox
    cropped_img = img[y1:y2, x1:x2]

    # Handle padding when downscaling
    resize_height, resize_width = min(new_height, height), min(new_width, width)
    pad_height1, pad_width1 = (height - resize_height) // 2, (width - resize_width) //2
    pad_height2, pad_width2 = (height - resize_height) - pad_height1, (width - resize_width) - pad_width1
    pad_spec = [(pad_height1, pad_height2), (pad_width1, pad_width2)] + [(0,0)] * (img.ndim - 2)

    result = cv2.resize(cropped_img, (resize_width, resize_height))
    result = np.pad(result, pad_spec, mode='constant')
    assert result.shape[0] == height and result.shape[1] == width
    return result

# Apply cv2_clipped_zoom randomly to an image
def uniform_rand_zoom(image):
    return cv2_clipped_zoom(image, ((np.random.random() * 2) + 1))

#model = Sequential([
#
#])

# Parameters for data generators which directly read
# in the images and augment each individually, and thus
# don't need to analyze the image set as a whole.
intakeDatagenConfiguration = dict(
    channel_shift_range=60,
    rescale=1./255,
    preprocessing_function=uniform_rand_zoom
)
intakeDatagenFlowConfig = dict(
    directory="sorted_data/monjan13",
    target_size=(144,256),
    class_mode="binary",
    save_prefix="Intake",
    save_to_dir="/Users/nwaterman2022/Documents/GitHub/mischiefdetector/augmented_data"
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
train_imgs, train_labels = trainingDatagenIntake.flow_from_directory(
    "sorted_data/monjan13",
    target_size=(144,256),
    class_mode="binary",
    save_prefix="Intake",
    save_to_dir="/Users/nwaterman2022/Documents/GitHub/mischiefdetector/augmented_data"
)
#testingDatagenIntake

# Give the normalization data generators a look at the data
# coming out of the intake data generators, so that they can
# adjust (normalize) the data properly.
# TODO: The training and testing data are normalized separately. Do we really want this?
trainingDatagenNorm.fit(train_imgs)
#testingDatagenNorm.fit(testingDatagenIntake)

