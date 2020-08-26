import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import random
import cv2

np.set_printoptions(suppress=True)

#다람쥐헌쳇바퀴에타고파 문장의 각각 모델을 리스트에 불러옴
model = np.arange(11, dtype=object)
image = np.arange(11, dtype=object)
text = "다람쥐헌쳇바퀴에타고파"
for i in range(11):
    #model[i] = tensorflow.keras.models.load_model(f"model/{text[i]}.h5")  #모델파일 불러오기
    image[i] = Image.open(f"crop_image/{i}.jpg") # 이미지파일 불러오기


for i in range(3):
    model[i] = tensorflow.keras.models.load_model(f"model/{text[i]}.h5")  # 모델파일 불러오기

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

max_x_y = [0,0]

for j in range(3):
    max = [0, 0, 0]
    max_i = [0, 0, 0]
    time = 1
    for i in range(1000):
        size = random.randrange(80, 120)
        x = random.randrange(0, 224 - size)
        y = random.randrange(0, 224 - size)
        cropImage = image[j].crop((x, y, x + size, y + size))
        cropImage.save(f"glyphs/{i}.jpg")

        # 크기 224*244로 변환
        size2 = (224, 224)
        cropImage = ImageOps.fit(cropImage, size2, Image.ANTIALIAS)

        # 이미지 numpy배열로 변환
        image_array = np.asarray(cropImage)

        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        data[0] = normalized_image_array

        prediction = model[j].predict(data)
        print(f"{i} : {prediction}")
        if prediction[0][0] > max[0]:
            max[0] = prediction[0][0]
            max_i[0] = i
            if j == 2:
                max_x_y[0] = x + size
                max_x_y[1] = y + size
        if prediction[0][1] > max[1]:
            max[1] = prediction[0][1]
            max_i[1] = i
        if prediction[0][2] > max[2]:
            max[2] = prediction[0][2]
            max_i[2] = i

    for i in range(3):
        if j == 0 and i == 2:
            break
        if j == 2 and i == 1:
            img = Image.open(f'crop_image/2.jpg')
            px = img.load()
            for k in range(0,max_x_y[0]):
                for l in range(0,max_x_y[1]):
                    px[k, l] = (255, 255, 255)
            img.save(f'correct_image/{text[j]}_{i}.png')
            break
        correct_image = Image.open(f"glyphs/{max_i[i]}.jpg")
        correct_image.save(f"correct_image/{text[j]}_{i}.jpg")
        print(max_i[i], max[i])
        #correct_image.show()





