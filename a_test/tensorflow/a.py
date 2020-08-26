import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import random
import cv2


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('model/disable_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('aa.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
#size = (224, 224)
#image = ImageOps.fit(image, size, Image.ANTIALIAS)
# display the resized image
#image.show()

max = [0,0,0]
max_i = [0,0,0]

for i in range(1000):
    size = random.randrange(80,110)
    x = random.randrange(0,224-size)
    y = random.randrange(0,224-size)
    cropImage = image.crop((x, y, x+size, y+size))
    cropImage.save(f"image/{i}.jpg")

    #크기 224*244로 변환
    size = (224, 224)
    cropImage = ImageOps.fit(cropImage, size, Image.ANTIALIAS)

    #이미지 numpy배열로 변환
    image_array = np.asarray(cropImage)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(f"{i} : {prediction}")
    if prediction[0][0] > max[0]:
        max[0] = prediction[0][0]
        max_i[0] = i
    if prediction[0][1] > max[1]:
        max[1] = prediction[0][1]
        max_i[1] = i
    if prediction[0][2] > max[2]:
        max[2] = prediction[0][2]
        max_i[2] = i
for i in range(3):
    correct_image = Image.open(f"image/{max_i[i]}.jpg")
    print(max_i[i],max[i])
    correct_image.show()



